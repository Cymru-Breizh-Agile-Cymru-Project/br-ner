from pathlib import Path
import warnings

import spacy
from spacy.tokens import DocBin

from ostilhou.text.tokenizer import (
    tokenize, detokenize,
    generate_person_tokens,
    TokenType,
)


def parse_line(line: str):
    """
    Pre-annotate the dataset using ostilhou POS tagger
    
    Metadata format:
        training_data = [
            ("Tokyo Tower is 333m tall.", [(0, 11, "BUILDING")]),
            ...
        ]
    """
    persons = []
    for token in generate_person_tokens(tokenize(line)):
        if token.type == TokenType.PERSON:
            persons.append(token.data)
    if persons:
        line = detokenize(tokenize(line))
        ne_with_span = []
        offset = 0
        for ne in persons:
            loc = line[offset:].find(ne)
            ne_with_span.append( (offset+loc, offset+loc+len(ne), "PERSON") )
            assert line[offset+loc:offset+loc+len(ne)] == ne, f"{line=} {ne=}, {line[offset:offset+len(ne)]=}"
            offset += loc+len(ne)
        # print(line.strip())
        # print(ne_with_span)
        return (line, ne_with_span)
    return (line, [])


def prepare_dataset(lines: list) -> DocBin:
    nlp = spacy.blank("fr")
    db = DocBin()
    for text, annot in data:
        doc = nlp.make_doc(text)
        ents = []
        for start, end, label in annot:
            span = doc.char_span(start, end, label=label)
            if span is None:
                msg = f"Skipping entity [{start}, {end}, {label}] in the following text because the character span '{doc.text[start:end]}' does not align with token boundaries:\n\n{repr(text)}\n"
                warnings.warn(msg)
            else:
                ents.append(span)
        doc.ents = ents
        db.add(doc)
    return db


if __name__ == "__main__":
    data = []
    with open("corpus.txt", 'r', encoding="utf-8") as _f:
        while line := _f.readline():
            # line = line.replace('\xa0', ' ')
            data.append(parse_line(line))

    assert len(data) > 1000
    train_split = data[:len(data)-1000]
    dev_split = data[-1000:]
    assert len(dev_split) == 1000
    print("Preparing train corpus...")
    db = prepare_dataset(train_split)
    db.to_disk("./train.spacy")

    print("Preparing dev corpus...")
    db = prepare_dataset(dev_split)
    db.to_disk("./dev.spacy")
    
    print("Done")
