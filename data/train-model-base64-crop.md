




Upload Base64 Image and Crop \| Stable Diffusion API Documentation








[Skip to main content](#docusaurus_skipToContent_fallback)[![Stable Diffusion Logo](/docs/img/SD-logo.png)![Stable Diffusion Logo](/docs/img/SD-logo.png)](https://stablediffusionapi.com)[Enterprise](https://stablediffusionapi.com/enterprise)[Pricing](https://stablediffusionapi.com/#pricing)[Blog](https://stablediffusionapi.com/blog)[Docs](https://stablediffusionapi.com/docs)[Playground](https://stablediffusionapi.com/playground)[Models](https://stablediffusionapi.com/models)[API Catalogue](https://stablediffusionapi.com/catalogue)* [Getting Started](/docs/)
* [Stable Diffusion API](/docs/category/stable-diffusion-api)
* [Train Model](/docs/category/train-model)
	+ [API Overview](/docs/train-model/overview)
	+ [Lora Training](/docs/train-model/lora-finetune)
	+ [Dreambooth Training (V2\)](/docs/train-model/finetune-v2)
	+ [Dreambooth Training](/docs/train-model/finetune)
	+ [Training Status](/docs/train-model/finetune-status)
	+ [Get Model List](/docs/train-model/finetune-list)
	+ [Delete Training](/docs/train-model/finetune-delete)
	+ [Cancel Training](/docs/train-model/cancel-training)
	+ [Crop Base64 Image](/docs/train-model/base64-crop)
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
* [Train Model](/docs/category/train-model)
* Crop Base64 Image
On this pageUpload Base64 Image and Crop
============================

* [fine\_tune](/docs/train-model/finetune)
* [fine\_tune\_v2](/docs/train-model/finetune-v2)
* [fine\_tune\_status](/docs/train-model/finetune-status)
* [cancle\_training](/docs/train-model/cancel-training)
* [finetune\_list](/docs/train-model/finetune-list)
* [finetune/delete](/docs/train-model/finetune-delete)
* [base64\_crop](/docs/train-model/base64-crop)
* [lora\_fine\_tune](/docs/train-model/lora-finetune)
Overview[â](#overview "Direct link to Overview")
--------------------------------------------------

Stable Diffusion V3 APIs Upload Base64 Image and Crop endpoint is used to upload an image and crop it. Pass the appropriate request parameters to the endpoint.

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
  "link": "https://pub-8b49af329fae499aa563997f5d4068a4.r2.dev/generations/2789658481681896990.png"  
}  

```
[PreviousCancel Training](/docs/train-model/cancel-training)[NextCommunity Models API](/docs/category/community-models-api)* [Overview](#overview)
* [Request](#request)
* [Body Attributes](#body-attributes)
* [Example](#example)
	+ [Body](#body)
	+ [Request](#request-1)
	+ [Response](#response)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



