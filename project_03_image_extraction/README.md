# Project 03: Send an Image to an LLM

## What you will make

A program that sends an image to an LLM and asks questions about it.

Open `shared/fixtures/practice_invoice.html` in a browser and take a screenshot to
create your test image.

## Steps

1. Read an image from the computer.
2. Send it to a model that supports image input.
3. Ask: `What kind of document is this?`
4. Ask for the invoice number, date, and total.
5. Print the answer.

## Things to try

- Make a smaller or blurry copy of the image and compare the result.
- Rotate the image and try again.
- Ask a question that the image cannot answer. Check whether the model admits that
  the information is missing.

## You have finished when

- Your program can send an image successfully.
- It can read at least three correct details from the test invoice.

You have now built an application that can see an image.

## Try another idea

Ask the model to give both the extracted value and the text it used as evidence.
