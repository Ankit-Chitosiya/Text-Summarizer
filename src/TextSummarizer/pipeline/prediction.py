from TextSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer, pipeline

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        self.pipe = pipeline("summarization", model=self.config.model_path, tokenizer=self.tokenizer)
        self.gen_kwargs = {"length_penalty": 0.8, "num_beams": 8, "max_length": 128}

    def predict(self, text):
        print("Dialogue:")
        print(text)

        output = self.pipe(text, **self.gen_kwargs)[0]["summary_text"]

        print("\nModel Summary:")
        print(output)

        return output
