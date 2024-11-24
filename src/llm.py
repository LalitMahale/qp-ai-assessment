from transformers import AutoModelForCausalLM, AutoTokenizer


class LLM:
    def __init__(self,model_name:str = "EleutherAI/gpt-neo-1.3B" ) -> None:
        self.model_name = model_name

    def generate_output(prompt:str):
        try:
            tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            model = AutoModelForCausalLM.from_pretrained(self.model_name)
            inputs = tokenizer(prompt, return_tensors="pt")
            outputs = model.generate(**inputs, max_new_tokens=500)
            return tokenizer.decode(outputs[0])
        except Exception as e:
            print(e)