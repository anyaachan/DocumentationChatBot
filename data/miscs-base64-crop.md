




Upload Base64 Image and Crop \| Stable Diffusion API Documentation








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
* Crop Base64 Image
On this pageUpload Base64 Image and Crop
============================

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

Stable Diffusion V3 APIs Upload Base64 Image and Crop endpoint is used to upload an image and crop it. Pass the appropriate request parameters to the endpoint. Note that the maximum file size for upload is 5MB 

Request[â](#request "Direct link to Request")
-----------------------------------------------


```
--request POST 'https://stablediffusionapi.com/api/v3/base64_crop' \  

```
Send a `POST` request to <https://stablediffusionapi.com/api/v3/base64_crop> endpoint. 

noteMake sure you are passing the image in **base64** format.

Body Attributes[â](#body-attributes "Direct link to Body Attributes")
-----------------------------------------------------------------------



| Parameter | Type | Description |
| --- | --- | --- |
| **key** | String | Your API Key used for request authorization |
| **image** | String | Image to be uploaded converted in base64 format |
| **crop** | String | A (true/false) flag for cropping the image upon uploading |

Example[â](#example "Direct link to Example")
-----------------------------------------------

### Body[â](#body "Direct link to Body")

Body Raw
```
{  
  "key": "",  
  "image": "data:image/png;base64,your_base_64_string",  
  "crop": "true"  
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
  "image": "data:image/png;base64,your_base_64_string",  
  "crop": "true"  
});  
  
var requestOptions = {  
  method: 'POST',  
  headers: myHeaders,  
  body: raw,  
  redirect: 'follow'  
};  
  
fetch("https://stablediffusionapi.com/api/v3/base64_crop", requestOptions)  
  .then(response => response.text())  
  .then(result => console.log(result))  
  .catch(error => console.log('error', error));  

```

```
<?php  
  
$payload = [  
   "key" => "",   
   "image" => "data:image/png;base64,your_base_64_string",   
   "crop" => "true"  
];  
  
$curl = curl_init();  
  
curl_setopt_array($curl, array(  
  CURLOPT_URL => 'https://stablediffusionapi.com/api/v3/base64_crop',  
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
  'url': 'https://stablediffusionapi.com/api/v3/base64_crop',  
  'headers': {  
    'Content-Type': 'application/json'  
  },  
  body: JSON.stringify({  
    "key": "",  
    "image": "data:image/png;base64,your_base_64_string",  
    "crop": "true"  
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
  
url = "https://stablediffusionapi.com/api/v3/base64_crop"  
  
payload = json.dumps({  
  "key": "",  
  "image": "data:image/png;base64,your_base_64_string",  
  "crop": "true"  
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
RequestBody body = RequestBody.create(mediaType, "{\n  \"key\": \"\",\n  \"image\": \"data:image/png;base64,your_base_64_string\",\n  \"crop\": \"true\"\n}");  
Request request = new Request.Builder()  
  .url("https://stablediffusionapi.com/api/v3/base64_crop")  
  .method("POST", body)  
  .addHeader("Content-Type", "application/json")  
  .build();  
Response response = client.newCall(request).execute();  

```
### Response[â](#response "Direct link to Response")


```
{  
  "status": "success",  
  "messege": "image uploaded",  
  "link": "https://pub-8b49af329fae499aa563997f5d4068a4.r2.dev/generations/2789658481681896990.png",  
  "request_id": 2398  
}  

```
[PreviousOverview](/docs/miscs/overview)[NextDelete Image](/docs/miscs/delete-image)* [Overview](#overview)
* [Request](#request)
* [Body Attributes](#body-attributes)
* [Example](#example)
	+ [Body](#body)
	+ [Request](#request-1)
	+ [Response](#response)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



