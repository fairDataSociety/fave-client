# Fave-Client
This is a python wrapper client for [FaVe](https://github.com/fairDataSociety/FaVe)

## Introduction

Fave-Client is a Python-based client library designed to interact with the FaVe API. This project aims to simplify the process of making API calls to FaVe, providing a seamless and efficient way to manage collections and documents.

## Features

- Easy-to-use API client for FaVe
- Supports all CRUD operations for collections and documents
- Built-in error handling
- Configurable settings

## Prerequisites

- Python 3.x
- `requests` library
- FaVe instance

## Installation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/fairDataSociety/fave-client.git
cd fave-client
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```python
from fave_api import APIClient

client = APIClient()
client.create_collection("my_collection")
```


### Create Collection

```python
from fave import FaVe

_fave = FaVe(url)
try:
    _fave.create_collection(collection, [])
except ApiException as e:
    raise Exception("%s\n" % e)
```

### Add Documents

```python
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

### Get similar documents

```python
from fave import FaVe

_fave = FaVe(url)
try:
    _fave.get_nearest_documents(collection, query, number_of_docs, max_distance)
except ApiException as e:
    raise Exception("%s\n" % e)
```


## API Reference

For a detailed API reference, please visit [FaVe API Documentation]([#](https://github.com/fairDataSociety/FaVe)).

## Configuration

You can configure the API client using the `configuration.py` file. Here you can set API endpoints, authentication details, and other settings.

## Troubleshooting

If you encounter issues, please check the following:

- Make sure all prerequisites are installed.
- Ensure you have the correct API endpoint in `configuration.py`.

To report bugs or issues, please open an issue on GitHub.

## Contributing

We welcome contributions! 

### Setting Up Development Environment

```bash
# Clone and navigate
git clone https://github.com/fairDataSociety/fave-client.git
cd fave-client

# Install dependencies
pip install -r dev-requirements.txt
```



## Tests

No tests yet.

## Versioning

This is first release.

## License

This project is licensed under the AGPL License. 

## Acknowledgments

- Thanks to @asabya @fairdatasociety @datafund and @ethswarm.

## Contact

For more information or for contributions, please contact us at.

---

