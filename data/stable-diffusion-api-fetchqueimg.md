




Fetch Queued Images Endpoint \| Stable Diffusion API Documentation








[Skip to main content](#docusaurus_skipToContent_fallback)[![Stable Diffusion Logo](/docs/img/SD-logo.png)![Stable Diffusion Logo](/docs/img/SD-logo.png)](https://stablediffusionapi.com)[Enterprise](https://stablediffusionapi.com/enterprise)[Pricing](https://stablediffusionapi.com/#pricing)[Blog](https://stablediffusionapi.com/blog)[Docs](https://stablediffusionapi.com/docs)[Playground](https://stablediffusionapi.com/playground)[Models](https://stablediffusionapi.com/models)[API Catalogue](https://stablediffusionapi.com/catalogue)* [Getting Started](/docs/)
* [Stable Diffusion API](/docs/category/stable-diffusion-api)
	+ [API Overview](/docs/stable-diffusion-api/overview)
	+ [Text to Image](/docs/stable-diffusion-api/text2img)
	+ [Image to Image](/docs/stable-diffusion-api/img2img)
	+ [Inpainting](/docs/stable-diffusion-api/inpainting)
	+ [Fetch Queued Images](/docs/stable-diffusion-api/fetchqueimg)
	+ [System Load](/docs/stable-diffusion-api/system-load)
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
* [Stable Diffusion API](/docs/category/stable-diffusion-api)
* Fetch Queued Images
On this pageFetch Queued Images Endpoint
============================

* [text2img](/docs/stable-diffusion-api/text2img)
* [img2img](/docs/stable-diffusion-api/img2img)
* [inpaint](/docs/stable-diffusion-api/inpainting)
* [fetch](/docs/stable-diffusion-api/fetchqueimg)
* [system\_load](/docs/stable-diffusion-api/system-load)
Overview[â](#overview "Direct link to Overview")
--------------------------------------------------

Stable Diffusion V3 APIs Fetch Queued Images API fetches queued images from stable diffusion.

Usually more complex image generation requests take more time for processing. Such requests are being queued for processing and the output images are retrievable after some time.

![Fetch Queued Images endpoint result](/docs/assets/images/fetchimg-action-sm-8712d2f75979157ca553675040662924.png)Request[â](#request "Direct link to Request")
-----------------------------------------------


```
--request POST 'https://stablediffusionapi.com/api/v3/fetch/{id}' \  

```
Send a `POST` request to [https://stablediffusionapi.com/api/v3/fetch/{id}](https://stablediffusionapi.com/api/v3/fetch/%7Bid%7D) endpoint to return the corresponding queued images. Where `{id}` is the ID returned together with the image URL in the response upon its generation.
This endpoint does not generate new images, it returns already generated/queued images.

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
  
fetch("https://stablediffusionapi.com/api/v3/fetch/12202888", requestOptions)  
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
  CURLOPT_URL => 'https://stablediffusionapi.com/api/v3/fetch/12202888',  
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
  'url': 'https://stablediffusionapi.com/api/v3/fetch/12202888',  
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
  
url = "https://stablediffusionapi.com/api/v3/fetch/12202888"  
  
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
  .url("https://stablediffusionapi.com/api/v3/fetch/12202888")  
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
    "id": 12202888,  
    "output": [  
        "https://pub-8b49af329fae499aa563997f5d4068a4.r2.dev/generations/e5cd86d3-7305-47fc-82c1-7d1a3b130fa4-0.png"  
    ]  
}  

```
[PreviousInpainting](/docs/stable-diffusion-api/inpainting)[NextSystem Load](/docs/stable-diffusion-api/system-load)* [Overview](#overview)
* [Request](#request)
* [Attributes](#attributes)
* [Example](#example)
	+ [Body](#body)
	+ [Request](#request-1)
	+ [Response](#response)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



