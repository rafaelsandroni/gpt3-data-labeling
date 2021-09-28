import pandas as pd
from AutoLabeling import GPT

class AutoLabeling():
    def __init__(self, few_shot_df: pd.DataFrame, text_col: str, label_col: str):
        self.few_shot_df = few_shot_df
        self.pre_prompt = None
        self.api = GPT()
        self.text_col = text_col
        self.label_col = label_col
        
    def generate_prompt(self, text: str, few_shot_df: pd.DataFrame, text_col: str, label_col: str, max_examples = 4):
        """
        Generates the prompt to few shot learning
        """
        def _pre_prompt():

            few_shot_texts = few_shot_df[text_col].values[:max_examples]
            few_shot_labels = few_shot_df[label_col].values[:max_examples]

            prompt_txt = []
            
            # add few shot examples
            for text_example, label_example in list(zip(few_shot_texts, few_shot_labels)):
                prompt_txt.append(f"""Text: "{text_example}"\nCategory: {label_example}\n""")
            return prompt_txt
        
        if not self.pre_prompt:
            self.pre_prompt = _pre_prompt()
            
        # add text to generate the label
        return "\n".join(self.pre_prompt + [f"""Text: "{text}"\nCategory:"""])

    def execute(self, text: str):
        """
        Generate the prompt and use GPT to complete with a category to the text, following the examples in few_shot_df
        """
        prompt = self.generate_prompt(text, self.few_shot_df, self.text_col, self.label_col)

        label_suggestion = self.api.completion(prompt)
        return label_suggestion.strip().lower()




