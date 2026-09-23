# Project 05: Give the LLM Tools

## What you will make

An assistant that asks your code to run small tools. Start with one tool, then let the
assistant read a few approved text files.

The model does not run a tool by itself. It asks your program to run a tool. Your
program checks the request, runs the function, and sends the result back to the model.

## Part 1: One simple tool

Create one function:

```text
lookup_shipment(reference)
```

Use the data in `shared/fixtures/tool_data.json`.

Then:

1. Describe the tool to the model.
2. Ask: `Where is shipment SHP-1001 going?`
3. Read the tool call returned by the model.
4. Run your function with the reference.
5. Send the function result back to the model.
6. Print the final answer.

Try an unknown reference and make sure the assistant does not invent a shipment.

## Part 2: Read approved files

Use the files in `shared/files/` and add two tools:

```text
list_files()
read_file(file_name)
```

Let the assistant list the files and read the ones that help answer a question.

Your code should:

- read only from `shared/files/`;
- allow only `.txt` and `.md` files;
- block file names containing `..` or an absolute path; and
- return a clear message when a file does not exist.

Ask questions such as:

- `When is Bright Paper open?`
- `What is its return policy?`
- `Does it sell laptops?`

The last question is not answered by the files, so the assistant should say it does
not know.

## You have finished when

- The model can ask for a tool and use its result.
- An unknown shipment does not produce an invented result.
- The assistant can answer from an approved file.
- Your code blocks a request for a file outside the approved folder.

You have now built an LLM application that can work with your own code and data.

## Try another idea

Add a calculator tool or a normal text-search tool for the approved files.
