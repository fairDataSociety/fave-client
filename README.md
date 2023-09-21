## fave client

This is a python wrapper client for [FaVe](https://github.com/fairDataSociety/FaVe)

## How to use

#### Create Collection

```
from fave import FaVe

_fave = FaVe(url)
try:
    _fave.create_collection(collection, [])
except ApiException as e:
    raise Exception("%s\n" % e)
```

#### Add Documents

```
from fave import FaVe

_fave = FaVe(url)
embeddings: Optional[List[List[float]]] = None
properties_to_vectorize = ["text"]
documents = []
for i, text in enumerate(texts):
    data_properties = {"text": text}
    data_properties["vector"] = embeddings[i] if embeddings else None
    _id = str(uuid.uuid4())
    document = fave_api.Document()
    document.properties = data_properties
    document.id = _id
    documents.append(document)
try:
    _fave.add_documents(collection, documents, properties_to_vectorize)
except ApiException as e:
    raise Exception("%s\n" % e)
```

#### Get similar documents

```
from fave import FaVe

_fave = FaVe(url)
try:
    _fave.get_nearest_documents(collection, query, number_of_docs, max_distance)
except ApiException as e:
    raise Exception("%s\n" % e)
```