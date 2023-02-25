from models import Author, Quote
import json
import aiofiles
import connect


async def load_authors_from_file():
    async with aiofiles.open('json_files/authors.json', mode='r') as file:
        res = await file.read()
        data = json.loads(res)

    author_list = []

    for record in data:
        author = Author(fullname=record['fullname'],
                        born_date=record['born_date'],
                        born_location=record['born_location'],
                        description=record['description'])
        author_list.append(author)

    Author.objects.insert(author_list)

async def load_quotes_from_file():
    async with aiofiles.open('json_files/quotes.json', 'r') as file:
        res = await file.read()
        data = json.loads(res)

    quote_list = []
    for record in data:

        if record['author'] == 'Alexandre Dumas fils':
            #Я про цей випадок пита в слак
            record['author'] = 'Alexandre Dumas-fils'

        author = Author.objects(fullname=record['author']).first()

        try:
            quote = Quote(tags=record['tags'],
                           author=author.id,
                           quote=record['quote'])
            quote_list.append(quote)

        except AttributeError:
            print(f'I cant find author "{record["author"]}"')

    Quote.objects.insert(quote_list)


if __name__ == '__main__':
    load_authors_from_file()