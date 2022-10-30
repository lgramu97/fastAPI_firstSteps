# FastAPI

## Introduction
* Framework to develop web apps with python.
* Created by Sebastian Ramirez.
* Open source.

## Ecosystem
* **Uvicorn**: is an ASGI web server implementation for Python.
* **Starlette**: is a lightweight ASGI framework/toolkit, which is ideal for building async web services in Python.
* **Pydantic**: Data validation and settings management using Python type annotations. pydantic enforces type hints at runtime, and provides user friendly errors when data is invalid. Define how data should be in pure, canonical Python; validate it with pydantic. We define here the models.

## Document FastAPI Interactive
* **OpenAPI**: The OpenAPI Initiative (OAI) was created by a consortium of forward-looking industry experts who recognize the immense value of standardizing on how APIs are described. As an open governance structure under the Linux Foundation, the OAI is focused on creating, evolving and promoting a vendor neutral description format. The OpenAPI Specification was originally based on the Swagger Specification, donated by SmartBear Software.
* **Swagger**: Simplify API development for users, teams, and enterprises with the Swagger open source and professional toolset. Find out how Swagger can help you design and document your APIs at scale.  
* Access Swagger documentation:  

        {localhost}/docs  
* Access Redoc documentation:

        {localhost}/redoc

## Request Body and Response Body
When you need to send data from a client (let's say, a browser) to your API, you send it as a request body. A request body is data sent by the client to your API. A response body is the data your API sends to the client. Your API almost always has to send a response body. But clients don't necessarily need to send request bodies all the time.

To declare a request body, you use Pydantic models with all their power and benefits.

## Validations
* https://pydantic-docs.helpmanual.io/usage/types/#pydantic-types

## Status Code HTTP
* Status code with images :) https://http.cat/
* 100: Informative.
* 200: Ok.
* 300: Redirecting.
* 400: Client Error.
* 500: Internal Server Error.

## Types Entry Data

* Path Parameters: URL obligatory.
* Query Parameters: URL optional.
* Request Body: JSON
* Forms: inputs frontend.
* Headers: http headers.
* Cookies: save data.
* Files: files like img, txt, video, audio, etc.
