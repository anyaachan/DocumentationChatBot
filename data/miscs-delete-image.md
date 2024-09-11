




Delete Image \| Stable Diffusion API Documentation








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
* Delete Image
On this pageDelete Image
============

* [v3/base64\_crop](/docs/miscs/base64-crop)
* [v3/delete\_image](/docs/miscs/delete-image)
* [v3/finetune\_list](/docs/miscs/finetune-list)
* [v4/dreambooth/model\_list](/docs/miscs/model-list)
* [v5/clear\_cach](/docs/miscs/clear-cache)
* [v3/dreambooth/buy\_model](/docs/miscs/buy-model)
* [v3/buy\_subscription](/docs/miscs/buy-subscription)
* [v3/nsfw\_image\_check](/docs/miscs/nsfw-image-check)
* [v3/upload\_model](/docs/miscs/upload-model)
* [v5/interior](/docs/miscs/interior)
Overview[â](#overview "Direct link to Overview")
--------------------------------------------------

This endpoint is used to delete an image using the image name.

Request[â](#request "Direct link to Request")
-----------------------------------------------


```
--request POST 'https://stablediffusionapi.com/api/v3/delete_image' \  

```
Send a `POST` request to <https://stablediffusionapi.com/api/v3/delete_image> endpoint and pass the name of the image you want to delete to the **image** parameter of the request body.

Watch the how\-to video to see it in action.

Body Attributes[â](#body-attributes "Direct link to Body Attributes")
-----------------------------------------------------------------------



| Parameter | Type | Description |
| --- | --- | --- |
| **key** | String | Your API Key used for request authorization |
| **request\_id** | Int | The request id gotten while [uploading image](/docs/miscs/base64-crop#response) |

Example[â](#example "Direct link to Example")
-----------------------------------------------

### Body[â](#body "Direct link to Body")

Body Raw
```
{  
  "key": "",  
  "request_id": 2398  
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
  "key": "",  
  "request_id": 2398  
});  
  
var requestOptions = {  
  method: 'POST',  
  headers: myHeaders,  
  body: raw,  
  redirect: 'follow'  
};  
  
fetch("https://stablediffusionapi.com/api/v3/delete_image", requestOptions)  
  .then(response => response.text())  
  .then(result => console.log(result))  
  .catch(error => console.log('error', error));  

```

```
<?php  
  
$payload = [  
  "key" => "",  
  "request_id" => 2398  
];  
  
$curl = curl_init();  
  
curl_setopt_array($curl, array(  
  CURLOPT_URL => 'https://stablediffusionapi.com/api/v3/delete_image',  
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
  'url': 'https://stablediffusionapi.com/api/v3/delete_image',  
  'headers': {  
    'Content-Type': 'application/json'  
  },  
  body: JSON.stringify({  
    "key": "",  
    "request_id": 2398  })  
};  
  
request(options, function (error, response) {  
  if (error) throw new Error(error);  
  console.log(response.body);  
});  

```

```
import requests  
import json  
  
url = "https://stablediffusionapi.com/api/v3/delete_image"  
  
payload = json.dumps({  
  "key": "",  
  "request_id": 2398  
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
RequestBody body = RequestBody.create(mediaType, "{\n   \"key\": \"\",\n   \"request_id\": \"2398\"\n}");  
Request request = new Request.Builder()  
  .url("https://stablediffusionapi.com/api/v3/delete_image")  
  .method("POST", body)  
  .addHeader("Content-Type", "application/json")  
  .build();  
Response response = client.newCall(request).execute();  

```
Response[â](#response "Direct link to Response")
--------------------------------------------------


```
{  
  "status": "success",  
  "messege":"image deleted"  
}  

```
[PreviousCrop Base64 Image](/docs/miscs/base64-crop)[NextGet Trained Models List](/docs/miscs/finetune-list)* [Overview](#overview)
* [Request](#request)
* [Body Attributes](#body-attributes)
* [Example](#example)
	+ [Body](#body)
	+ [Request](#request-1)
* [Response](#response)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



