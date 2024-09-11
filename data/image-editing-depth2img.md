




Depth to Image Endpoint \| Stable Diffusion API Documentation








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
	+ [API Overview](/docs/image-editing/overview)
	+ [Outpainting](/docs/image-editing/outpainting)
	+ [Blip Diffusion](/docs/image-editing/blip-diffusion)
	+ [Magic Mix](/docs/image-editing/magic-mix)
	+ [Depth to Image](/docs/image-editing/depth2img)
	+ [Image Mixer](/docs/image-editing/imagemixer)
	+ [Image Guided Editing](/docs/image-editing/pix2pix)
	+ [Remove Background](/docs/image-editing/removebg-createmask)
	+ [Super Resolution](/docs/image-editing/super-resolution)
	+ [Mixture Canvas](/docs/image-editing/mixture-canvas)
	+ [Multiview](/docs/image-editing/multiview)
	+ [Fashion (Beta)](/docs/image-editing/fashion)
* [Text To 3D](/docs/category/text-to-3d)
* [Uncensored Chat](/docs/uncensored-chat)
* [A1111 Schedulers](/docs/a1111schedulers)
* [FAQ](/docs/faq)
* [Postman Collection](https://documenter.getpostman.com/view/18679074/2s83zdwReZ)
* [Support](https://discord.gg/UxqnDu7j3r)
* 
* 
* [Image Editing](/docs/category/image-editing)
* Depth to Image
On this pageDepth to Image Endpoint
=======================

* [v5/outpainting](/docs/image-editing/outpainting)
* [v5/blip\_diffusion](/docs/image-editing/blip-diffusion)
* [v5/magic\_mix](/docs/image-editing/magic-mix)
* [v5/depth2img](/docs/image-editing/depth2img)
* [v5/image\_guided\_editing](/docs/image-editing/pix2pix)
* [v5/removebg\_createmask](/docs/image-editing/removebg-createmask)
* [v5/super\_resolution](/docs/image-editing/super-resolution)
* [v5/image\_mixer](/docs/image-editing/imagemixer)
* [v5/mixture\-canvas](/docs/image-editing/mixture-canvas)
* [v5/multiview](/docs/image-editing/multiview)
* [v5/fashion](/docs/image-editing/fashion)
Overview[â](#overview "Direct link to Overview")
--------------------------------------------------

The V5 API Depth to Image endpoint allows for depth to generate a picture.

Pass the image URL with the `init_image` parameter and add your description of the desired modification to the `prompt` parameter.

![Depth to image endpoint result](/docs/assets/images/v5-depth2img-action-sm-813d79e2a873da9f14bd3ad4d736a9cb.png)Request[â](#request "Direct link to Request")
-----------------------------------------------


```
--request POST 'https://stablediffusionapi.com/api/v5/depth2img' \  

```
Make a `POST` request to <https://stablediffusionapi.com/api/v5/depth2img> endpoint and pass the required parameters in the request body. 

Watch the how\-to video to see it in action.

Body Attributes[â](#body-attributes "Direct link to Body Attributes")
-----------------------------------------------------------------------



| Parameter | Description |
| --- | --- |
| **key** | Your API Key used for request authorization |
| **prompt** | Text prompt with description of the things you want in the image to be generated |
| **init\_image** | Link to the initial image |

Example[â](#example "Direct link to Example")
-----------------------------------------------

### Body[â](#body "Direct link to Body")

Body
```
{  
  "key": "",  
  "init_image" : "https://d1okzptojspljx.cloudfront.net/generations/b3341a09-082e-474e-989f-72ec3f3bf7aa-0.png",  
  "prompt" : "give him glasses"  
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
  "init_image" : "https://d1okzptojspljx.cloudfront.net/generations/b3341a09-082e-474e-989f-72ec3f3bf7aa-0.png",  
  "prompt" : "give him glasses"  
});  
  
var requestOptions = {  
  method: 'POST',  
  headers: myHeaders,  
  body: raw,  
  redirect: 'follow'  
};  
  
fetch("https://stablediffusionapi.com/api/v5/depth2img", requestOptions)  
  .then(response => response.text())  
  .then(result => console.log(result))  
  .catch(error => console.log('error', error));  

```

```
<?php  
  
$payload = [  
  "key" => "",   
  "init_image" => "https://d1okzptojspljx.cloudfront.net/generations/b3341a09-082e-474e-989f-72ec3f3bf7aa-0.png",   
  "prompt" => "give him glasses"  
];  
  
$curl = curl_init();  
  
curl_setopt_array($curl, array(  
  CURLOPT_URL => 'https://stablediffusionapi.com/api/v5/depth2img',  
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
  'url': 'https://stablediffusionapi.com/api/v5/depth2img',  
  'headers': {  
    'Content-Type': 'application/json'  
  },  
  body: JSON.stringify({  
    "key": "",  
    "init_image" : "https://d1okzptojspljx.cloudfront.net/generations/b3341a09-082e-474e-989f-72ec3f3bf7aa-0.png",  
    "prompt" : "give him glasses"  
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
  
url = "https://stablediffusionapi.com/api/v5/depth2img"  
  
payload = json.dumps({  
  "key": "",  
  "init_image" : "https://d1okzptojspljx.cloudfront.net/generations/b3341a09-082e-474e-989f-72ec3f3bf7aa-0.png",  
  "prompt" : "give him glasses"  
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
RequestBody body = RequestBody.create(mediaType, "{\n  \"key\": \"\",\n  \"init_image\" : \"https://d1okzptojspljx.cloudfront.net/generations/b3341a09-082e-474e-989f-72ec3f3bf7aa-0.png\",\n    \"prompt\" : \"give him glasses\"\n}");  
Request request = new Request.Builder()  
  .url("https://stablediffusionapi.com/api/v5/depth2img")  
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
    "generationTime": 1.322338581085205,  
    "id": 14754476,  
    "output": "https://pub-8b49af329fae499aa563997f5d4068a4.r2.dev/generations/87e450a1-f0e6-4f95-a6c5-c081fd80f635-0.png"  
}  

```
[PreviousMagic Mix](/docs/image-editing/magic-mix)[NextImage Mixer](/docs/image-editing/imagemixer)* [Overview](#overview)
* [Request](#request)
* [Body Attributes](#body-attributes)
* [Example](#example)
	+ [Body](#body)
	+ [Request](#request-1)
	+ [Response](#response)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



