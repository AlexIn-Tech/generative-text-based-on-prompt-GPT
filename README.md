# generative-text based on prompt - GPT
This script allows you to generate text using a pre-trained language model. It only generates a few words at the moment, I may have better results using another pre-trained model. 

I created this script to familiarize with the tools because in the future I hope we could find some pre-trained models like chatGPT from OpenAI directly on HuggingFace. It would be awesome to be able to run locally this kind of tech without any limitations (except your hardware). 

## Requirements

- Python 3.6 or higher
- PyTorch 1.7.0 or higher
- Transformers 3.2.0 or higher

```python
# First, install the Hugging Face Transformers library
!pip install transformers
```

Moreover, you need to install pytorch in the prerequisites. For this you need a compatible CUDA GPU . Please have a look on : <https://pytorch.org/get-started/locally/> to install the right version on your computer. 
Here is mine :

```python
pip3 install torch torchvision torchaudio --extra-index-url <https://download.pytorch.org/whl/cu116>
```

## Usage

To use the script, run the following command:

```python
python generate_text.py "Your input prompt here"
```

Replace "Your input prompt here" with the text that you want to generate text from.

## Customization

You can customize the script by changing the following variables:

- `model_name`: The name of the pre-trained model to use. By default, the script uses the "asi/gpt-fr-cased-base" model, but you can choose any model that is supported by the Transformers library.

## Output

The script will print the generated text to the console.

## Limitations

The script is limited by the capabilities of the chosen pre-trained model and the quality of the input prompt. The generated text may not always be coherent or relevant to the input prompt.

