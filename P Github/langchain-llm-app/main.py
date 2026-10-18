from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def genrate_pet_name():
    llm =OpenAI(temperature=0.7)

    prompt_template_name = PromptTemplate(
        input_variables=['animals_type'],
        template="I have a {animal_type} pet and I want a cool name for it suggest me fivr cool names for pet. "
    )

    name =llm
    
    return name

if __name__ == "__main__":
    print (genrate_pet_name())