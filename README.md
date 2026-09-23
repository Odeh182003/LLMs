# LLM Mini-Projects

These are small projects for learning how to use LLMs from code. Each project creates
something useful and visible. You can choose the projects that interest you.

Start with the smallest working version. It does not need to be perfect. When it
works, show it to someone, explain what you learned, and celebrate the result.

## Project menu

| Project | What you will make |
| --- | --- |
| 01 | A program that asks an LLM a question |
| 02 | A chat program that remembers earlier messages |
| 03 | A program that sends an image to an LLM |
| 04 | A program that turns text into simple JSON data |
| 05 | An assistant that uses tools and reads approved files |

## What you need

- A programming language you already know.
- An OpenAI or OpenRouter API key.
- A code editor and terminal.
- Curiosity and a few test questions.

Copy `.env.example` to `.env` and put your API key there. Never place a key directly
in source code, and never commit `.env` to Git.

## Which API should you use?

- With OpenAI, use the Responses API.
- With OpenRouter, use its Chat Completions API and one of its free models.

You do not need to learn both at the same time. Pick one and start building.

Helpful links:

- [OpenAI Responses API](https://developers.openai.com/api/reference/resources/responses/methods/create)
- [OpenRouter quickstart](https://openrouter.ai/docs/quickstart)
- [OpenRouter free models](https://openrouter.ai/collections/free-models/)

Free models may have low limits or may sometimes be unavailable.

## A simple way to work

For each project:

1. Make the smallest version work.
2. Try it with two or three examples.
3. Add one improvement that interests you.
4. Write a few lines about what you learned.
5. Show it to someone.

You do not need a web interface, a database, or a large framework. A small command-line
program is enough.

See [`shared/GLOSSARY.md`](shared/GLOSSARY.md) when you find an unfamiliar word.
