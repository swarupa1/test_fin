class LLM:
    def __init__(self, model_id, tokenizer, device):
        self.model_id = model_id
        self.tokenizer = tokenizer
        self.device = device
        self.model = self.load_model()

    def load_model(self):
        from transformers import AutoModelForCausalLM
        model = AutoModelForCausalLM.from_pretrained(self.model_id)
        model.to(self.device)
        return model

    def generate_response(self, prompt, max_length=150):
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        outputs = self.model.generate(**inputs, max_length=max_length)
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response