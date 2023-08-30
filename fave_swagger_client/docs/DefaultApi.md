# swagger_client.DefaultApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fave_add_documents**](DefaultApi.md#fave_add_documents) | **POST** /documents | 
[**fave_create_collection**](DefaultApi.md#fave_create_collection) | **POST** /collections | 
[**fave_delete_collection**](DefaultApi.md#fave_delete_collection) | **DELETE** /collections/{collection} | 
[**fave_get_documents**](DefaultApi.md#fave_get_documents) | **GET** /documents | 
[**fave_get_nearest_documents**](DefaultApi.md#fave_get_nearest_documents) | **POST** /nearest-documents | 
[**fave_root**](DefaultApi.md#fave_root) | **GET** / | 


# **fave_add_documents**
> OKResponse fave_add_documents(body)



Add documents into a collection.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.AddDocumentsRequest() # AddDocumentsRequest | 

try:
    api_response = api_instance.fave_add_documents(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->fave_add_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddDocumentsRequest**](AddDocumentsRequest.md)|  | 

### Return type

[**OKResponse**](OKResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yaml, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fave_create_collection**
> OKResponse fave_create_collection(body)



Create a new collection.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.Collection() # Collection | 

try:
    api_response = api_instance.fave_create_collection(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->fave_create_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Collection**](Collection.md)|  | 

### Return type

[**OKResponse**](OKResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yaml, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fave_delete_collection**
> OKResponse fave_delete_collection(collection)



Delete a collection.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
collection = 'collection_example' # str | Collection name

try:
    api_response = api_instance.fave_delete_collection(collection)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->fave_delete_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Collection name | 

### Return type

[**OKResponse**](OKResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yaml, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fave_get_documents**
> Document fave_get_documents(_property, value, collection)



Retrieve a document based on query parameters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
_property = '_property_example' # str | The property to filter the document by
value = 'value_example' # str | The value of the property to filter the document by
collection = 'collection_example' # str | The collection to use for this query

try:
    api_response = api_instance.fave_get_documents(_property, value, collection)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->fave_get_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_property** | **str**| The property to filter the document by | 
 **value** | **str**| The value of the property to filter the document by | 
 **collection** | **str**| The collection to use for this query | 

### Return type

[**Document**](Document.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yaml, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fave_get_nearest_documents**
> NearestDocumentsResponse fave_get_nearest_documents(body)



Get nearest documents for a collection.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.NearestDocumentsRequest() # NearestDocumentsRequest | 

try:
    api_response = api_instance.fave_get_nearest_documents(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->fave_get_nearest_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NearestDocumentsRequest**](NearestDocumentsRequest.md)|  | 

### Return type

[**NearestDocumentsResponse**](NearestDocumentsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yaml, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fave_root**
> fave_root()



Home. Discover the REST API

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    api_instance.fave_root()
except ApiException as e:
    print("Exception when calling DefaultApi->fave_root: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/yaml, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

