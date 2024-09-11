




Text to 3D \| Stable Diffusion API Documentation








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
	+ [API Overview](/docs/text-to-3d/overview)
	+ [Text to 3D](/docs/text-to-3d/textto3d)
	+ [Image to 3D](/docs/text-to-3d/imageto3d)
* [Uncensored Chat](/docs/uncensored-chat)
* [A1111 Schedulers](/docs/a1111schedulers)
* [FAQ](/docs/faq)
* [Postman Collection](https://documenter.getpostman.com/view/18679074/2s83zdwReZ)
* [Support](https://discord.gg/UxqnDu7j3r)
* 
* 
* [Text To 3D](/docs/category/text-to-3d)
* Text to 3D
On this pageText to 3D
==========

* [text\-to\-3d](/docs/text-to-3d/textto3d)
* [image\-to\-3d](/docs/text-to-3d/imageto3d)
Overview[â](#overview "Direct link to Overview")
--------------------------------------------------

This endpoint generates 3D image from text prompt while passing appropriate parameters

Request[â](#request "Direct link to Request")
-----------------------------------------------


```
--request POST 'https://stablediffusionapi.com/api/v3/txt_to_3d' \  

```
Make a `POST` request to <https://stablediffusionapi.com/api/v3/txt_to_3d> endpoint and pass the required parameters as a request body. 

Body Attributes[â](#body-attributes "Direct link to Body Attributes")
-----------------------------------------------------------------------



| Parameter | Description |
| --- | --- |
| **key** | Your API Key used for request authorization. |
| **prompt** | Text prompt with description of the things you want in the image to be generated. |
| **negative\_prompt** | Items you don't want in the image. |
| **steps** | Number of denoising steps (minimum: 1; maximum: 50\) |
| **guidance\_scale** | Scale for classifier\-free guidance (minimum: 1; maximum: 20\) |
| **frame\_size** | Number of frame size) |
| **seed** | Seed is used to reproduce results, same seed will give you same image in return again. Pass *null* for a random number. |
| **seconds** | Number of seconds |
| **output\_type** | This is the type of the 3D image you want to generate. It accepts gif or ply. |
| **webhook** | Set an URL to get a POST API call once the image generation is complete. |
| **track\_id** | This ID is returned in the response to the webhook API call. This will be used to identify the webhook request. |

Example[â](#example "Direct link to Example")
-----------------------------------------------

### Body[â](#body "Direct link to Body")

Body
```
{  
    "key":"",  
    "prompt":"beautiful man",  
    "guidance_scale":20,  
    "steps":64,  
    "frame_size":256,  
    "output_type":"gif",  
    "webhook": null,  
    "track_id": null  
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
  "prompt":"rose",  
  "guidance_scale":20,  
  "steps":64,  
  "frame_size":256,  
  "output_type":"gif",  
  "webhook": null,  
  "track_id": null  
});  
  
var requestOptions = {  
  method: 'POST',  
  headers: myHeaders,  
  body: raw,  
  redirect: 'follow'  
};  
  
fetch("https://stablediffusionapi.com/api/v3/txt_to_3d", requestOptions)  
  .then(response => response.text())  
  .then(result => console.log(result))  
  .catch(error => console.log('error', error));  

```

```
<?php  
  
$payload = [  
  "key" => "",   
  "prompt" => "rose",  
  "guidance_scale" => 20,  
  "steps" => 64,  
  "frame_size" => 256,  
  "output_type" => "gif",  
  "webhook" => null,  
  "track_id" => null  
];  
  
$curl = curl_init();  
  
curl_setopt_array($curl, array(  
  CURLOPT_URL => 'https://stablediffusionapi.com/api/v3/txt_to_3d',  
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
  'url': 'https://stablediffusionapi.com/api/v3/txt_to_3d',  
  'headers': {  
    'Content-Type': 'application/json'  
  },  
  body: JSON.stringify({  
    "key": "",  
    "prompt":"rose",  
    "guidance_scale":20,  
    "steps":64,  
    "frame_size":256,  
    "output_type":"gif",  
    "webhook": null,  
    "track_id": null  
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
  
url = "https://stablediffusionapi.com/api/v3/txt_to_3d"  
  
payload = json.dumps({  
   "key": "",  
  "prompt":"rose",  
  "guidance_scale":20,  
  "steps":64,  
  "frame_size":256,  
  "output_type":"gif",  
  "webhook": None,  
  "track_id": None  
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
RequestBody body = RequestBody.create(mediaType, "{\n        \"key\":\"QAlQs5I2I9orW5mkhXU2uPio8dRO1x3UqHzvj46cXFeixb7HLwyQGeIG7sKI\",\n        \"prompt\":\"rose\",\n        \"guidance_scale\":20,\n        \"steps\":64,\n        \"frame_size\":256,\n        \"output_type\":\"gif\"\n}");  
Request request = new Request.Builder()  
  .url("https://stablediffusionapi.com/api/v3/txt_to_3d")  
  .method("POST", body)  
  .addHeader("Content-Type", "application/json")  
  .build();  
Response response = client.newCall(request).execute();  

```
### Response[â](#response "Direct link to Response")


```
{  
    "status": "success",  
    "generationTime": 6,  
    "id": 326,  
    "output": [  
        "https://cdn.stablediffusionapi.com/generations/2d74af44-825c-4cff-9fe9-3716bd40c9fd.gif"  
    ],  
    "meta": {  
        "file_prefix": "2d74af44-825c-4cff-9fe9-3716bd40c9fd",  
        "frame_size": 256,  
        "guidance_scale": 15,  
        "negative_prompt": "",  
        "outdir": "out",  
        "output_type": "gif",  
        "prompt": "A birthday cupcake",  
        "safetychecker": "no",  
        "seconds": 3,  
        "seed": 1110454524,  
        "steps": 64  
    }  
}  
  

```
[PreviousAPI Overview](/docs/text-to-3d/overview)[NextImage to 3D](/docs/text-to-3d/imageto3d)* [Overview](#overview)
* [Request](#request)
* [Body Attributes](#body-attributes)
* [Example](#example)
	+ [Body](#body)
	+ [Request](#request-1)
	+ [Response](#response)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



