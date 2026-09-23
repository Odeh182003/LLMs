# Project 04: Turn Text into JSON

## What you will make

A program that reads normal text and returns data in a clear JSON shape.

Use the examples in `shared/fixtures/extraction_cases.json`.

## Output shape

```json
{
  "document_type": "invoice",
  "document_number": "2837",
  "organization": "Example Trading",
  "document_date": "2026-09-12",
  "currency": "SAR",
  "total": 4820.0
}
```

## Steps

1. Send one example text to the model.
2. Ask for the output shape shown above.
3. Use Structured Outputs or a JSON schema if your model supports it.
4. Read the JSON in your code and print each field.
5. Use `null` when the text does not contain a value. Do not ask the model to guess.

## Things to try

- Test all three examples in the fixture file.
- Remove the date from one example and check that the result uses `null`.
- Return a fake broken response in your code and show a friendly error instead of
  crashing.

## You have finished when

- Your program returns JSON that your code can read.
- Missing information becomes `null` instead of a guessed value.
- You can explain why checked JSON is easier for an application to use than normal text.

You have now connected an LLM response to normal application data.

## Try another idea

Use the image from Project 03 and return the same JSON shape from the invoice image.
