import os
import openai
import json
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_MODEL = os.getenv("OPENAI_API_MODEL")

openai.api_key = OPENAI_API_KEY

def compile_to_gpt_patois(user_input):
    gpt_patois_format_definition = """
    Full Formal Specification:
    1. General Structure

    A typical GPT-Patois control block looks like this:

    BLOCK_TYPE {
        Parameter1: "Value",
        Parameter2: "Value",
        ...
    }

    There is not parent block.

    The following sections outline each block type, its purpose, and the possible parameters it may contain.

    2.1 Conversation Block (CB)
    This block sets the overall context for the conversation. It includes the parameters for Personality, Topic, Focus, Detail, Characters, and Event.

    2.2 Role Block (RB)
    This block defines the role the AI should take in the conversation, with parameters such as Role to define the assistant's role.

    2.3 Prompt Block (PB)
    This block contains the user's prompt or command, including the parameter Prompt which holds the user's question or instruction.

    2.4 Emotion Block (EB)
    The block sets the emotional tone for the AI's responses, containing the Emotion parameter to set the emotional tone of the assistant.

    2.5 Knowledge Block (KB)
    This block specifies the domain of knowledge from which the assistant should draw. It contains the Domain parameter which sets the knowledge domain.

    2.6 Time Block (TB)
    This block sets a temporal context for the assistant's responses, with a Time parameter to define a specific time or time period.

    2.7 Location Block (LB)
    This block sets a location context for the AI's responses, containing a Location parameter to set a specific geographical context.

    2.8 Factuality Block (FB)
    This block controls the level of factual accuracy in the assistant's responses, with Factuality as its parameter to set the level of factual accuracy.

    2.9 Style Block (SB)
    This block controls stylistic aspects of the assistant's responses, with Style and Verbosity as its parameters.

    2.10 Detail Level Block (DLB)
    This block controls the level of detail in the assistant's responses, with Detail as its parameter to control the level of detail in the assistant's responses.

    2.11 Language Block (LangB)
    This block sets the language of the assistant's responses, containing Language as its parameter.

    2.12 Bias Control Block (BCB)
    This block allows controlling any potential bias in the assistant's responses, with Bias as its parameter.

    2.13 Genre Block (GB)
    This block sets a specific genre for story generation or other creative writing tasks, containing Genre as its parameter.

    2.14 Sensory Detail Block (SDB)
    This block sets the level of sensory detail in the assistant's responses, containing SensoryDetail as its parameter.

    2.15 Imagination Block (IB)
    This block controls the level of imagination and creativity in the assistant's responses, with Imagination as its parameter.

    2.16 Fact Check Block (FCB)
    This block instructs the assistant to fact-check a piece of information, containing Fact as its parameter.

    2.17 Temporal Control Block (TCB)
    This block sets a time context for the assistant's responses, containing Time as its parameter to specify a time period.

    2.18 Contextual Block (CtxB)
    This block provides detailed contextual information for the AI's responses, containing CurrentEvent as its parameter.

    2.19 Sociolinguistic Block (SLB)
    This block influences the politeness level, formality, or dialect in responses, containing Politeness as its parameter.

    2.20 Sentiment Analysis Block (SAB)
    This block influences the overall sentiment of the model's responses, containing Sentiment as its parameter.

    2.21 Interactive Block (IB)
    This block generates interactive elements in the conversation, containing InteractiveElement as its parameter.


    3. Nesting Feature

    The nesting feature allows users to nest multiple blocks within each other to create complex sub-contexts. This offers more nuanced control over AI responses.

    A typical nesting syntax looks like this:

    BLOCK_TYPE {
        Parameter1: "Value",
        BLOCK_TYPE {
            Parameter1: "Value",
            Parameter2: "Value",
            ...
        },
        Parameter2: "Value",
        ...
    }

    To explain further, let's take a practical example:

    PB {
        Prompt: "Describe the social and economic changes that occurred during the Industrial Revolution."
    }
    CB {
        Personality: "historian",
        Topic: "history",
        RB {
            Role: "Teacher"
        },
        Focus: "industrial revolution",
    }

    In this example, a Role Block (RB) is nested inside a Conversation Block (CB). This means that within the conversation context defined by the Conversation Block, the assistant takes on a specific role as defined by the nested Role Block.

    The nesting feature adds another dimension to the specificity and complexity of instructions you can give to the AI model.

    Compile the following input into strict GPT-Patois format, adding as many blocks as possible. Input:\n
    """
    
    gpt_patois_string = get_response(gpt_patois_format_definition + user_input)

    return gpt_patois_string


def get_response(prompt):
    response = openai.ChatCompletion.create(
        model=OPENAI_API_MODEL,
        messages=[
            {'role': 'user', 'content': prompt}
        ]
    )
    return response.choices[0].message.content.strip()