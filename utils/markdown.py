import pandas as pd

def generate_title_markdown(text, level=1):
    return f'\n{"#" * level} {text}\n'

def generate_image_markdown(image_path, alt_text=''):
    return f'\n![{alt_text}]({image_path})\n'

def generate_paragraph_markdown(text):
    return f'\n{text}\n'

def generate_results_table_markdown(results):
    df = pd.DataFrame(results)
    if 'params' in df.columns:
      for key in df['params'].iloc[0].keys():
          df[key] = df['params'].apply(lambda x: x[key])
      df = df.drop('params', axis=1)
    return f'\n{df.head(10).to_markdown(index=False)}\n'

def generate_separation_markdown():
    return '\n-----------------------\n'