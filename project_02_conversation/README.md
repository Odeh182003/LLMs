# Project 02: Build a Simple Conversation

## What you will make

A chat program that remembers what was said earlier in the conversation.

## Steps

1. Start with the program from Project 01.
2. Keep accepting new messages until the user types `exit`.
3. Keep the earlier messages and send them with the next request.
4. Add a `reset` command that starts a new conversation.
5. Keep using a simple system prompt for the assistant's role.

You can keep the messages in your own code. If your API can continue from a previous
response ID, you can try that method instead.

## Things to try

Tell the assistant:

> My favorite color is green.

Then ask:

> What is my favorite color?

After that, reset the conversation and ask again. The assistant should no longer have
the earlier message.

Also try asking the user message to ignore the system prompt. See whether the model
continues to follow its main role.

## You have finished when

- The conversation can use information from an earlier message.
- Reset starts a clean conversation.
- You can explain which old messages are sent to the model.

You have now given an LLM short-term memory.

## Try another idea

Save the conversation to a local file and load it again when the program starts.

