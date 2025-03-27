# Training a NER pipeline with spaCy

_Tested with Python3.12 and spaCy v3.8.4_

## Using Breton in spaCy

Copy the `br` directory to spaCy `lang` directory.

```bash
import spacy
nlp = spacy.blank("br")
doc = nlp("Demat deoc'h !")
```

```bash
import spacy
nlp = spacy.load("br")
doc = nlp("Demat deoc'h !")
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
```

## Simple NER model for breton

### Usage

### Training

Download the corpus (filtered wikipedia br dump) from HuggingFace:

```bash
python3 scripts/download_corpus.py
```

Prepare the training data:

```bash
python3 scripts/prepare_data.py
```

#### Prepare a config file

https://spacy.io/usage/training

The language id to use for languages unsupported by spaCy is "xx".

After you’ve saved the starter config to a file base_config.cfg, you can use the init fill-config command to fill in the remaining defaults. Training configs should always be complete and without hidden defaults, to keep your experiments reproducible.

```bash
python3 -m spacy init fill-config base_config.cfg config.cfg
```

#### Train

```bash
python3 -m spacy train config.cfg --output ./output
```
