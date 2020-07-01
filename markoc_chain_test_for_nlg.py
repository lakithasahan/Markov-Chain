import pandas as pd
import markovify

inp = pd.read_csv('test.csv')
inp.head(3)

text_model = markovify.NewlineText(inp.headline_text, state_size = 2)
for i in range(5):
    print(text_model.make_sentence())
