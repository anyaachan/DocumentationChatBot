




Get Public Models List \| Stable Diffusion API Documentation








[Skip to main content](#docusaurus_skipToContent_fallback)[![Stable Diffusion Logo](/docs/img/SD-logo.png)![Stable Diffusion Logo](/docs/img/SD-logo.png)](https://stablediffusionapi.com)[Enterprise](https://stablediffusionapi.com/enterprise)[Pricing](https://stablediffusionapi.com/#pricing)[Blog](https://stablediffusionapi.com/blog)[Docs](https://stablediffusionapi.com/docs)[Playground](https://stablediffusionapi.com/playground)[Models](https://stablediffusionapi.com/models)[API Catalogue](https://stablediffusionapi.com/catalogue)* [Getting Started](/docs/)
* [Stable Diffusion API](/docs/category/stable-diffusion-api)
* [Train Model](/docs/category/train-model)
* [Community Models API](/docs/category/community-models-api)
* [Text To Video](/docs/category/text-to-video)
* [Community Models API V4](/docs/category/community-models-api-v4)
* [MISCS](/docs/category/miscs)
	+ [Overview](/docs/miscs/overview)
	+ [Crop Base64 Image](/docs/miscs/base64-crop)
	+ [Delete Image](/docs/miscs/delete-image)
	+ [Get Trained Models List](/docs/miscs/finetune-list)
	+ [Get Public Models List](/docs/miscs/model-list)
	+ [Clear User Cache](/docs/miscs/clear-cache)
	+ [Buy Dreambooth Model](/docs/miscs/buy-model)
	+ [Buy Subscription Plan](/docs/miscs/buy-subscription)
	+ [Cancel Subscription Plan](/docs/miscs/cancel-subscription)
	+ [NSFW Image Check](/docs/miscs/nsfw-image-check)
	+ [Upload Model](/docs/miscs/upload-model)
	+ [Create Room Interior](/docs/miscs/interior)
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
* [MISCS](/docs/category/miscs)
* Get Public Models List
On this pageGet Public Models List
======================

* [v3/base64\_crop](/docs/miscs/base64-crop)
* [v3/delete\_image](/docs/miscs/delete-image)
* [v3/finetune\_list](/docs/miscs/finetune-list)
* [v4/dreambooth/model\_list](/docs/miscs/model-list)
* [v5/clear\_cach](/docs/miscs/clear-cache)
* [v3/dreambooth/buy\_model](/docs/miscs/buy-model)
* [v3/buy\_subscription](/docs/miscs/buy-subscription)
* [v3/cancel\_subscription](/docs/miscs/cancel-subscription)
* [v3/nsfw\_image\_check](/docs/miscs/nsfw-image-check)
* [v3/upload\_model](/docs/miscs/upload-model)
* [v5/interior](/docs/miscs/interior)
Overview[â](#overview "Direct link to Overview")
--------------------------------------------------

This endpoint returns a list of all the public models available.

This endpoint returns an array with the IDs of the public models and information about them: status, name, description, etc.

Request[â](#request "Direct link to Request")
-----------------------------------------------


```
--request POST 'https://stablediffusionapi.com/api/v4/dreambooth/model_list' \  

```
Send a `POST` request to <https://stablediffusionapi.com/api/v4/dreambooth/model_list> endpoint to obtain a list with the available public models and their IDs.

Attributes[â](#attributes "Direct link to Attributes")
--------------------------------------------------------



| Parameter | Type | Description |
| --- | --- | --- |
| **key** | String | Your API Key used for request authorization |

Example[â](#example "Direct link to Example")
-----------------------------------------------

### Body[â](#body "Direct link to Body")

Body Raw
```
{  
 "key": ""  
}  

```
### Request[â](#request-1 "Direct link to Request")

* JS
* PHP
* NODE
* PYTHON
* JAVA


```
var myHeaders = new Headers();  
myHeaders.append("Content-Type", "application/json");  
  
var raw = JSON.stringify({  
 "key": ""  
});  
  
var requestOptions = {  
  method: 'POST',  
  headers: myHeaders,  
  body: raw,  
  redirect: 'follow'  
};  
  
fetch("https://stablediffusionapi.com/api/v4/dreambooth/model_list", requestOptions)  
  .then(response => response.text())  
  .then(result => console.log(result))  
  .catch(error => console.log('error', error));  

```

```
<?php  
  
$payload = [  
  "key" => ""  
];  
  
$curl = curl_init();  
  
curl_setopt_array($curl, array(  
  CURLOPT_URL => 'https://stablediffusionapi.com/api/v4/dreambooth/model_list',  
  CURLOPT_RETURNTRANSFER => true,  
  CURLOPT_ENCODING => '',  
  CURLOPT_MAXREDIRS => 10,  
  CURLOPT_TIMEOUT => 0,  
  CURLOPT_FOLLOWLOCATION => true,  
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,  
  CURLOPT_CUSTOMREQUEST => 'POST',  
  CURLOPT_POSTFIELDS => json_encode($payload),  
  CURLOPT_HTTPHEADER => array(  
    'Content-Type: application/json'  
  ),  
));  
  
$response = curl_exec($curl);  
  
curl_close($curl);  
echo $response;  

```

```
var request = require('request');  
var options = {  
  'method': 'POST',  
  'url': 'https://stablediffusionapi.com/api/v4/dreambooth/model_list',  
  'headers': {  
    'Content-Type': 'application/json'  
  },  
  body: JSON.stringify({  
    "key": ""  
  })  
};  
  
request(options, function (error, response) {  
  if (error) throw new Error(error);  
  console.log(response.body);  
});  

```

```
import requests  
import json  
  
url = "https://stablediffusionapi.com/api/v4/dreambooth/model_list"  
  
payload = json.dumps({  
 "key": ""  
})  
  
headers = {  
  'Content-Type': 'application/json'  
}  
  
response = requests.request("POST", url, headers=headers, data=payload)  
  
print(response.text)  

```

```
OkHttpClient client = new OkHttpClient().newBuilder()  
  .build();  
MediaType mediaType = MediaType.parse("application/json");  
RequestBody body = RequestBody.create(mediaType, "{\n    \"key\": \"\"\n}");  
Request request = new Request.Builder()  
  .url("https://stablediffusionapi.com/api/v4/dreambooth/model_list")  
  .method("POST", body)  
  .addHeader("Content-Type", "application/json")  
  .build();  
Response response = client.newCall(request).execute();  

```
### Response[â](#response "Direct link to Response")

The example response below is truncated after the initial 3 model entries; the list is too long to show it completely.


```
[  
    {  
        "model_id": "midjourney",  
        "status": "model_ready",  
        "created_at": null,  
        "instance_prompt": "mdjrny-v4 style",  
        "model_name": "MidJourney V4",  
        "description": "Openjourney is an open source Stable Diffusion fine tuned model on Midjourney images, by PromptHero",  
        "screenshots": "https://d1okzptojspljx.cloudfront.net/generations/14853540911669470514.png"  
    },  
    {  
        "model_id": "anything-v3",  
        "status": "model_ready",  
        "created_at": null,  
        "instance_prompt": null,  
        "model_name": "Anything V3",  
        "description": "This model is intended to produce high-quality, highly detailed anime style with just a few prompts.",  
        "screenshots": "https://d1okzptojspljx.cloudfront.net/generations/8589140601669473451.png"  
    },  
    {  
        "model_id": "wifu-diffusion",  
        "status": "model_ready",  
        "created_at": null,  
        "instance_prompt": null,  
        "model_name": "Wifu Diffusion",  
        "description": "waifu-diffusion is a latent text-to-image diffusion model that has been conditioned on high-quality anime images through fine-tuning.",  
        "screenshots": "https://d1okzptojspljx.cloudfront.net/generations/21468819471669474933.png"  
    },  
  
    ...  
]  

```
[PreviousGet Trained Models List](/docs/miscs/finetune-list)[NextClear User Cache](/docs/miscs/clear-cache)* [Overview](#overview)
* [Request](#request)
* [Attributes](#attributes)
* [Example](#example)
	+ [Body](#body)
	+ [Request](#request-1)
	+ [Response](#response)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



