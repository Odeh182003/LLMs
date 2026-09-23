# Simple LLM Glossary

## API

A way for one program to send a request to another program and receive a result.

## Model

The AI system that reads the input and creates the output.

## Prompt

The text, image, or other input sent to a model.

## System prompt

The main instructions for the model. It can set the model's role, rules, and writing
style. Some APIs call it `instructions`, a `developer` message, or a `system` message.

## User prompt

The user's question or request.

## Token

A small part of text used by a model. API cost and input limits are often measured
in tokens.

## Context

Everything the model can see for the current request. This can include the system
prompt, user prompt, earlier messages, an image, and tool results.

## JSON

A common text format for sending data between programs.

## Schema

A description of the fields and types that data should contain.

## Structured Outputs

An API feature that helps a model return data in a chosen JSON shape.

## Tool calling

The model asks the application to run a named function. The application checks the
request, runs the function, and returns the result.

## Streaming

Showing parts of the answer as they arrive instead of waiting for the complete answer.

