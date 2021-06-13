# REST APIs with Azure functions

Implementation of basic REST APIs with Azure functions and MongoDB using Python.
Four separate HTTPTrigger functions are created to store, retrieve and manipulate the data in Mongo Database through HTTP Get, Post, Put/Patch and Delete requests.

## Dependencies

1. Azure functions: func tools CLI and VScode extension
2. MongoDB: Azure CosmosDB or Local Connection
3. Python dependencies stored in the requirements.txt file. To install them, run `pip install -r requirements.txt`
4. Postman

## Demo
### App
`func start`
![func_app_demo](./example_images/func_app.png)
___
### POST Request - addTask
![post_req](./example_images/post_req.png)
___
### GET Request - getTask
![get_1_req](./example_images/get_1_req.png)
___
### GET Request - getTasks
![get_all_req](./example_images/get_req.png)
___
### PUT Request - updateTask
![put_req](./example_images/put_req.png)
___
### PATCH Request - updateTask
![patch_req](./example_images/patch_req.png)
___
### DELETE Request - deleteTask
![delete_req](./example_images/delete_req.png)
