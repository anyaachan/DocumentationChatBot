




Get Training Status (Sandbox) \| Stable Diffusion API Documentation








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
	+ [API Overview](/docs/dreambooth-sandbox/overview)
	+ [Create Request](/docs/dreambooth-sandbox/finetune)
	+ [Get Training Status](/docs/dreambooth-sandbox/finetune-status)
* [Image Editing](/docs/category/image-editing)
* [Text To 3D](/docs/category/text-to-3d)
* [Uncensored Chat](/docs/uncensored-chat)
* [A1111 Schedulers](/docs/a1111schedulers)
* [FAQ](/docs/faq)
* [Postman Collection](https://documenter.getpostman.com/view/18679074/2s83zdwReZ)
* [Support](https://discord.gg/UxqnDu7j3r)
* 
* 
* [Dreambooth Sandbox](/docs/category/dreambooth-sandbox)
* Get Training Status
On this pageGet Training Status (Sandbox)
=============================

* [sandbox/v3/fine\_tune](/docs/dreambooth-sandbox/finetune)
* [sandbox/v3/fine\_tune\_status](/docs/dreambooth-sandbox/finetune-status)
Overview[â](#overview "Direct link to Overview")
--------------------------------------------------

This endpoint returns the status of the Dreambooth request from [Create Dreambooth Request](/docs/dreambooth-sandbox/finetune).

This endpoint allows to check the current status of the model training and the estimated time remaining for its completion if not completed yet.

Request[â](#request "Direct link to Request")
-----------------------------------------------


```
--request POST 'https://stablediffusionapi.com/api/sandbox/v3/fine_tune_status/{training_id}' \  

```
Make a `POST` request to '[https://stablediffusionapi.com/api/sandbox/v3/fine\_tune\_status/{training\_id}](https://stablediffusionapi.com/api/sandbox/v3/fine_tune_status/%7Btraining_id%7D) endpoint. Where `{training_id}` is returned in the response upon initiating the model training using the [Create Dreambooth Request](/docs/dreambooth-sandbox/finetune#response) endpoint.
This endpoint only returns information for an already initiated model training.

Attributes[â](#attributes "Direct link to Attributes")
--------------------------------------------------------



| Parameter | Description |
| --- | --- |
| **key** | Your API Key used for request authorization |

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
  
fetch("https://stablediffusionapi.com/api/sandbox/v3/fine_tune_status/F5jvdzGnYi", requestOptions)  
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
  CURLOPT_URL => 'https://stablediffusionapi.com/api/sandbox/v3/fine_tune_status/F5jvdzGnYi',  
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
  'url': 'https://stablediffusionapi.com/api/sandbox/v3/fine_tune_status/F5jvdzGnYi',  
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
  
url = "https://stablediffusionapi.com/api/sandbox/v3/fine_tune_status/F5jvdzGnYi"  
  
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
  .url("https://stablediffusionapi.com/api/sandbox/v3/fine_tune_status/F5jvdzGnYi")  
  .method("POST", body)  
  .addHeader("Content-Type", "application/json")  
  .build();  
Response response = client.newCall(request).execute();  

```
### Response[â](#response "Direct link to Response")

Example Response
```
{  
  "status": "success",  
  "messege": "model_ready",  
  "data": " /n Step:1 Training Started, 5 Steps to go : ETA : 30 minutes /n Step:2 Training Done, 4 Steps to go : ETA : 15 minutes /n Step:3 Model Uploading, 3 Steps to go : ETA : 10 minutes /n  /n Step:4 Model Uploaded, 2 Steps to go : ETA : 5 minutes /n Model loaded successfully"  
}  

```
[PreviousCreate Request](/docs/dreambooth-sandbox/finetune)[NextImage Editing](/docs/category/image-editing)* [Overview](#overview)
* [Request](#request)
* [Attributes](#attributes)
* [Example](#example)
	+ [Body](#body)
	+ [Request](#request-1)
	+ [Response](#response)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



