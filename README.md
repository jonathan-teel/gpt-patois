# GPT-Patois: A Powerful Pseudo-Language for Guiding GPT Models

GPT-Patois is a structured pseudo-language designed to enhance the control over interactions with GPT models. It offers a robust and flexible way to guide model behavior and customize responses with precision.

-- 

## Specifications 

GPT-Patois uses control blocks to define the model's conversation context, role, and more. Each block follows this general structure:

BLOCK_TYPE {
Parameter1: "Value",
Parameter2: "Value",
...
}

The following sections outline each block type, its purpose, and the possible parameters it may contain.

Conversation Block (CB)
This block sets the overall context for the conversation. It includes the parameters for Personality, Topic, Focus, Detail, Characters, and Event.
Example:

```json
CB {
    "Personality": "friendly",
    "Topic": "technology",
    "Focus": "artificial intelligence",
    "Detail": "deep learning",
    "Characters": ["AI researcher", "Software engineer"],
    "Event": "Tech conference"
}
```

Role Block (RB)
This block defines the role the AI should take in the conversation, with parameters such as Role to define the assistant's role.
Example:

```json
RB {
    "Role": "guide"
}
```

Prompt Block (PB)
This block contains the user's prompt or command, including the parameter Prompt which holds the user's question or instruction.
Example:

```json
PB {
    "Prompt": "Explain the concept of deep learning."
}
```

Emotion Block (EB)
The block sets the emotional tone for the AI's responses, containing the Emotion parameter to set the emotional tone of the assistant.
Example:

```json
EB {
    "Emotion": "enthusiastic"
}
```

Knowledge Block (KB)
This block specifies the domain of knowledge from which the assistant should draw. It contains the Domain parameter which sets the knowledge domain.
Example:

```json
KB {
    "Domain": "machine learning"
}
```

Time Block (TB)
This block sets a temporal context for the assistant's responses, with a Time parameter to define a specific time or time period.
Example:

```json
TB {
    "Time": "21st Century"
}
```

Location Block (LB)
This block sets a location context for the AI's responses, containing a Location parameter to set a specific geographical context.
Example:

```json
LB {
    "Location": "Silicon Valley, USA"
}
```

Factuality Block (FB)
This block controls the level of factual accuracy in the assistant's responses, with Factuality as its parameter to set the level of factual accuracy.
Example:

```json
FB {
    "Factuality": "high"
}
```

Style Block (SB)
This block controls stylistic aspects of the assistant's responses, with Style and Verbosity as its parameters.
Example:

```json
SB {
    "Style": "formal",
    "Verbosity": "concise"
}
```

Detail Level Block (DLB)
This block controls the level of detail in the assistant's responses, with Detail as its parameter to control the level of detail in the assistant's responses.
Example:

```json
DLB {
    "Detail": "high"
}
```

Language Block (LangB)
This block sets the language of the assistant's responses, containing Language as its parameter.
Example:

```json
LangB {
    "Language": "English"
}
```

Bias Control Block (BCB)
This block allows controlling any potential bias in the assistant's responses, with Bias as its parameter.
Example:

```json
BCB {
    "Bias": "neutral"
}
```

Genre Block (GB)
This block sets a specific genre for story generation or other creative writing tasks, containing Genre as its parameter.
Example:

```json
GB {
    "Genre": "science fiction"
}
```

Sensory Detail Block (SDB)
This block sets the level of sensory detail in the assistant's responses, containing SensoryDetail as its parameter.
Example:

```json
SDB {
    "SensoryDetail": "high"
}
```

Imagination Block (IB)
This block controls the level of imagination and creativity in the assistant's responses, with Imagination as its parameter.
Example:

```json
IB {
    "Imagination": "high"
}
```

Fact Check Block (FCB)
This block instructs the assistant to fact-check a piece of information, containing Fact as its parameter.
Example:

```json
FCB {
    "Fact": "The Turing test is a measure of a machine's ability to exhibit intelligent behavior equivalent to that of a human."
}
```

Temporal Control Block (TCB)
This block sets a time context for the assistant's responses, containing Time as its parameter to specify a time period.
Example:

```json
TCB {
    "Time": "Medieval times"
}
```

Contextual Block (CtxB)
This block provides detailed contextual information for the AI's responses, containing CurrentEvent as its parameter.
Example:

```json
CtxB {
    "CurrentEvent": "The AI tech conference happening in Silicon Valley."
}
```

Sociolinguistic Block (SLB)
This block influences the politeness level, formality, or dialect in responses, containing Politeness as its parameter.
Example:

```json
SLB {
    "Politeness": "high"
}
```

Sentiment Analysis Block (SAB)
This block influences the overall sentiment of the model's responses, containing Sentiment as its parameter.
Example:

```json
SAB {
    "Sentiment": "positive"
}
```

Interactive Block (IB)
This block generates interactive elements in the conversation, containing InteractiveElement as its parameter.
Example:

```json
IB {
    "InteractiveElement": "poll"
}
```

Prompt Repetition Block (PRB)
This block manages the extent to which the AI repeats the user's prompt in its responses. It includes the parameters Repetition, ParaphraseLevel, and Echo.

```json
PRB {
    "Repetition": "low",
    "ParaphraseLevel": "low",
    "Echo": "low"
}
```

Introduction Block (IntroB)
This block controls how the assistant introduces itself or its role in the conversation. It includes the Introduction parameter.

```json
IntroB {
    "Introduction": "none"
}
```

--

## Nesting Feature

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

```json
PB {
    "Prompt": "Describe the social and economic changes that occurred during the Industrial Revolution."
}
CB {
    "Personality": "historian",
    "Topic": "history",
    "RB" {
        "Role": "Teacher"
    },
    "Focus": "industrial revolution",
}
```

In this example, a Role Block (RB) is nested inside a Conversation Block (CB). This means that within the conversation context defined by the Conversation Block, the assistant takes on a specific role as defined by the nested Role Block.

--

## Contributing

Contributions are welcome, please feel free to submit a pull request or create an issue for any bugs or feature requests.

--

## License

GPT-Patois is released under the MIT License. See LICENSE for details.