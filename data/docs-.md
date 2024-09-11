




Stable Diffusion API Docs \| Stable Diffusion API Documentation








[Skip to main content](#docusaurus_skipToContent_fallback)[![Stable Diffusion Logo](/docs/img/SD-logo.png)![Stable Diffusion Logo](/docs/img/SD-logo.png)](https://stablediffusionapi.com)[Enterprise](https://stablediffusionapi.com/enterprise)[Pricing](https://stablediffusionapi.com/#pricing)[Blog](https://stablediffusionapi.com/blog)[Docs](https://stablediffusionapi.com/docs)[Playground](https://stablediffusionapi.com/playground)[Models](https://stablediffusionapi.com/models)[API Catalogue](https://stablediffusionapi.com/catalogue)* [Getting Started](/docs/)
* [Stable Diffusion API](/docs/category/stable-diffusion-api)
* [Train Model](/docs/category/train-model)
* [Community Models API](/docs/category/community-models-api)
* [Text To Video](/docs/category/text-to-video)
* [Community Models API V4](/docs/category/community-models-api-v4)
* [MISCS](/docs/category/miscs)
* [ControlNet](/docs/category/controlnet)
* [Voice Cloning](/docs/category/voice-cloning)
* [Enterprise Plan](/docs/category/enterprise-plan)
* [Dreambooth Sandbox](/docs/category/dreambooth-sandbox)
* [Image Editing](/docs/category/image-editing)
* [Text To 3D](/docs/category/text-to-3d)
* [Uncensored Chat](/docs/uncensored-chat)
* [A1111 Schedulers](/docs/a1111schedulers)
* [FAQ](/docs/faq)
* [Postman Collection](https://documenter.getpostman.com/view/18679074/2s83zdwReZ)
* [Support](https://discord.gg/UxqnDu7j3r)
* 
* 
* Getting Started
On this pageStable Diffusion API Docs
=========================

ð Welcome
============

The Stable Diffusion V3 API comes with these features:

* Faster speed;
* Inpainting;
* Image 2 Image;
* Negative Prompts.

The Stable Diffusion API is organized around REST. Our API has predictable resource\-oriented URLs, accepts form\-encoded request bodies, returns JSON\-encoded responses, and uses standard HTTP response codes, authentication, and verbs. 

tipWe have chatbot trained on docs and codebase, click on footer chat icon and ask question, it will give you code examples as well :)

The Stable Diffusion API is equipped with a NSFW checker. Any image detected as NSFW will be replaced by a blank image.

dangerBe aware of the content of your images.
We have a filter system to remove any child pornography. Multiple attempts will result in account suspension.

The Stable Diffusion API uses keys to authenticate the requests. Pass the key you've obtained from the [API Settings](https://stablediffusionapi.com/settings/api) page to the request body and follow all the endpoint processes accordingly. 

Send JSON POST requests with data and links.

dangerDo not send files as raw format, send **publicly accessible links** to them instead.

Here you will find information about the Stable Diffusion and Multiple AI APIs.

You can pass details to generate images using this API, without the need of GPU locally.

All API requests are authorized by a **key**. You can obtain one by **[signing up](https://stablediffusionapi.com/register)**.

Features of API[â](#features-of-api "Direct link to Features of API")
-----------------------------------------------------------------------

1. Use 100\+ models to generate images with single API call.
2. Use multi lora models
3. Use embeddings models
4. Use controlnet models
5. Use multi controlnet models
6. Upscale images
7. Highres fix
8. Multiple language support
9. Self Attention process
10. Train model
11. Clipfix
12. Base64 support

cautionAll API requests **require a header** to be passed. Make sure you pass **`Content-Type: application/json`** in the header as shown in the example below:


```
--header 'Content-Type: application/json'  

```
Follow the links below for more information about Image Stable Diffusion API endpoints:

* [Stable Diffusion API](/docs/category/stable-diffusion-api);
* [Dreambooth Finetuning](/docs/category/train-model);
* [Dreamnbooth API V4](/docs/category/community-models-api-v4);
* [Text to Video](/docs/category/text-to-video);
* [ControlNet](/docs/category/controlnet);
* [Enterprise Plan](/docs/category/enterprise-plan);
* [Dreambooth Sandbox API](/docs/category/dreambooth-sandbox);
* [Image Editing](/docs/category/image-editing).

tipVisit our **[YouTube channel](https://www.youtube.com/@stablediffusionapi/videos)** to see Stable Diffusion APIs in action.

Possible Error Responses[â](#possible-error-responses "Direct link to Possible Error Responses")
--------------------------------------------------------------------------------------------------

Below are listed the most common errors that might occur while using the Stable Diffusion API.

### Rate Limit[â](#rate-limit "Direct link to Rate Limit")

This error is returned when the same request has been sent multiple times.


```
{  
    "status": "error",  
    "message": "Rate limit exceeded",  
    "tips": "you are sending same request multiple times, spam filter is enabled, please wait for 30 seconds and try again"  
}  

```
### Invalid Key[â](#invalid-key "Direct link to Invalid Key")

This error is returned when the API key used for request authentication is invalid.


```
{  
    "status": "error",  
    "message": "Invalid Api Key",  
    "tip": "1. Make sure you are passing Content-Type: application/json in header. 2. Make sure you are doing POST request with valid JSON. 3. Make sure your JSON does not have error, use jsonlint to validate json array. 4. Make sure you have valid API key."  
}  

```
### Failed Response[â](#failed-response "Direct link to Failed Response")

This error is returned when the request has failed for some reason.


```
{  
    "status": "failed",  
    "id": "",  
    "message": "Failed, Try Again",  
    "output": ""  
}  

```
### Validation Errors[â](#validation-errors "Direct link to Validation Errors")

This error is returned when one of the required fields has not been set. In this example, the **prompt** field was not set:


```
{  
    "status": "error",  
    "message": {  
        "prompt": [  
            "The prompt field is required."  
        ]  
    }  
}  

```
This error is returned when **model\_id** has not been filled for an endpoint that requires it.


```
{  
    "status": "error",  
    "message": "Model id not found"  
}  

```
[NextStable Diffusion API](/docs/category/stable-diffusion-api)* [Features of API](#features-of-api)
* [Possible Error Responses](#possible-error-responses)
	+ [Rate Limit](#rate-limit)
	+ [Invalid Key](#invalid-key)
	+ [Failed Response](#failed-response)
	+ [Validation Errors](#validation-errors)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



