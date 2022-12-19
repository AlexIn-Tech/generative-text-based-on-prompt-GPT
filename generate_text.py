import argparse

# Next, import the necessary modules
from transformers import AutoModelWithLMHead, AutoTokenizer

# Parse the command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("prompt", type=str, help="The input prompt to generate text from")
args = parser.parse_args()

# Choose a model and tokenizer
model_name = "asi/gpt-fr-cased-base"  # Replace with the model name you want to use
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelWithLMHead.from_pretrained(model_name)

# Tokenize the input prompt
input_ids = tokenizer.encode(args.prompt, return_tensors="pt")

# Set the attention mask and pad token id
attention_mask = input_ids.ne(0).long()  # Set the attention mask to 1 for all non-zero tokens
pad_token_id = tokenizer.pad_token_id  # Get the pad token id from the tokenizer

# Generate text
output = model.generate(input_ids, attention_mask=attention_mask, pad_token_id=pad_token_id, max_new_tokens=20) #Edit max_new_tokens to change the size on the output

# Decode the generated text
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

print(generated_text)
