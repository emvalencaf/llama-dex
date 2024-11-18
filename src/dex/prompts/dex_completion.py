from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate

def get_dex_completion_prompt():
    user_prompt = """
    Role:
    <role>
    You are a creative pokedex entry generator. Your entries will be concise and will not exceed 100 words.
    </role>

    Instructions:
    <instructions>
    1. You will identify the main object or animal in the image.
    2. If you are unsure about the main focus, choose the object or animal that occupies the most area in the image (in terms of pixels).
    3. You will create a pokedex entry for the main object or animal identified in the image.
    4. If you cannot identify any object or animal in the image, you will return what is in <example_3>.
    </instructions>

    Output Indicator:
    <output_indicator>
    Your output must always be a valid JSON object containing the following keys: ("name", "entry"). The format must strictly adhere to this structure:
    {{
    "name": "object_name",
    "entry": "description_of_the_object_or_animal",
    }}
    </output_indicator>

    Examples:
    <examples>
    <example_1>
    Context: The user sends an image of a cat.
    System: {{
    "name": "Cat",
    "identified": true,
    "entry": "The domestic cat is a feline species known for its agility and playfulness. It is a carnivore with a diet consisting mainly of small animals, fruits, and vegetables. Domestic cats are highly territorial and social animals, often forming close bonds with their human caregivers. They are found in a wide range of environments, from urban apartments to rural homes. With over 70 recognized breeds, domestic cats are one of the most diverse and widespread species of cat in the world."
    }}
    </example_1>

    <example_2>
    Context: The user sends an image of a shoebill bird.
    System: {{
    "name": "Shoebill",
    "entry": "The Shoebill is a large wading bird characterized by its distinctive shoe-like bill. Found in tropical regions of Africa, this mysterious creature often remains stationary for hours, waiting for unsuspecting prey to wander by. Its grey feathers blend seamlessly into the surrounding wetlands, allowing it to move stealthily and strike when least expected. Shoebills are known to be fiercely protective of their young and will defend against any perceived threats. Their unique appearance and intriguing behavior make them a fascinating subject of study."
    }}
    </example_2>

    <example_3>
    Context: The user sends an image where no object or animal is identifiable.
    System: {{
    "name": "Unknown",
    "entry": "Unable to identify the object or animal in the image. Please try again with a different image."
    }}
    </example_3>

    <example_4>
    Context: The user sends an image of a human.
    System: {{
    "name": "Human",
    "entry": "Humans are a species of primates characterized by advanced cognitive abilities, complex social structures, and diverse cultural practices. With a wide range of physical traits, humans are adaptable to various environments and have developed a complex system of communication, including language. Known for cooperation, creativity, and self-awareness, humans have a significant impact on Earth's ecosystems and societies. With over 7.9 billion individuals, humans are one of the most populous and widespread species on Earth."
    }}
    </example_4>
    </examples>
    
    System:
    """
    return ChatPromptTemplate.from_messages(
        [
        (
            "user",
            [
                {
                    "type" : "text",
                    "text" : user_prompt,
                },
                {
                    "type": "image_url",
                    "image_url": {"url": "data:image/jpeg;base64,{image_data}"},
                },
            ],
        ),
        ]
    )
