import random
from openai import OpenAI
from django.conf import settings
from quotes.models import Quote, Author, Tag

client = OpenAI(api_key=settings.OPEN_AI_KEY)


def ask_gpt(author_name: str, prompt: str):
    print(f"Autor: {author_name}, prompt: {prompt}")
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": f"Imagine that you are {author_name}. Give a good answer."},
            {"role": "user", "content": prompt}
        ]
    )
    answer = completion.choices[0].message.content
    print(f"{answer=}")
    return answer


def generate_random_quote() -> None:
    authors = Author.objects.all()
    author = random.choice(authors)
    author_name = author.fullname
    print("Generating random quote...")  # функція рандомной цитати
    promt = f"""Write an inspirational quote that can be attributed to the person {author_name}, reflecting their inner beliefs, wisdom and impact on the world. """
    new_quote = ask_gpt(author_name=author_name, prompt=promt)
    quote = Quote.objects.create(quote=new_quote, author=author)
    all_tags = Tag.objects.all()
    random.shuffle(list(all_tags))
    tags_count = random.randint(2, 3)
    target_tags = all_tags[:tags_count]
    for tag in target_tags:
        quote.tags.add(tag)
    print(f"Successfully")

