# Project 01: Ask an LLM a Question

## What you will make

A small program that sends a question to an LLM and prints the answer.

## Steps

1. Read the API key from an environment variable.
2. Send this question to the model: `Why is the sky blue?`
3. Print the answer.
4. Let the user type a different question.
5. Add a clear error message if the request fails.

Next, add a **system prompt**. A system prompt gives the model its main role and rules.
For example:

> You are a friendly teacher. Use simple English and answer in no more than three sentences.

Ask the same question with and without this system prompt. Compare the answers.

Depending on the API, the system prompt may be called `instructions`, a `developer`
message, or a `system` message.

## You have finished when

- You can type a question and see an answer.
- The API key is not written in the source code.
- Changing the system prompt changes the style of the answer.

You have now built your first LLM application.

## Try another idea

Print the answer as it arrives instead of waiting for the full answer. This is called
streaming.

