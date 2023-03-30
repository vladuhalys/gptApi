import openai
openai.api_key = "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"

filename = "data.txt"
filename_filter = "filter.txt"
with open(filename, encoding="utf8") as file:
    text = file.read()
with open(filename_filter, encoding="utf8") as file:
    _filter = file.read()
requst_content = _filter + text
completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "assistant", "content": requst_content}])
print(f'{completion.choices[0].message.content}')

