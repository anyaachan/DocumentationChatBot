




Image Guided Editing Endpoint \| Stable Diffusion API Documentation








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
* Image Guided Editing
On this pageImage Guided Editing Endpoint
=============================

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

V5 Picture to Picture endpoint is used to edit an image using a text prompt with the description of the desired changes.

Pass the image URL with the `init_image` parameter and add your description of the expected result to the `prompt` parameter.

![Picture to picture endpoint result](/docs/assets/images/v5-pix2pix-action-sm-3c8d81aab219063de5d407ca1d98b05e.png)Request[â](#request "Direct link to Request")
-----------------------------------------------


```
--request POST 'https://stablediffusionapi.com/api/v5/pix2pix' \  

```
Make a `POST` request to <https://stablediffusionapi.com/api/v5/pix2pix> endpoint and pass the required parameters in the request body. 

Watch the how\-to video to see it in action.

Body Attributes[â](#body-attributes "Direct link to Body Attributes")
-----------------------------------------------------------------------



| Parameter | Description |
| --- | --- |
| **key** | Your API Key used for request authorization |
| **prompt** | Text prompt with description of the things you want in the image to be generated |
| **init\_image** | Link to the initial image |
| **image\_guidance\_scale** | Image guidance scale |
| **steps** | Number of denoising steps |
| **guidance\_scale** | Scale for classifier\-free guidance (minimum: 1; maximum: 20\) |

Example[â](#example "Direct link to Example")
-----------------------------------------------

### Body[â](#body "Direct link to Body")

Body
```
{  
  "key": "",  
  "init_image" : "https://d1okzptojspljx.cloudfront.net/generations/b3341a09-082e-474e-989f-72ec3f3bf7aa-0.png",  
  "prompt" : "make him woman",  
  "image_guidance_scale" : 1,  
  "steps" : 50,  
  "guidance_scale" : 7  
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
  "prompt" : "make him woman",  
  "image_guidance_scale" : 1,  
  "steps" : 50,  
  "guidance_scale" : 7  
});  
  
var requestOptions = {  
  method: 'POST',  
  headers: myHeaders,  
  body: raw,  
  redirect: 'follow'  
};  
  
fetch("https://stablediffusionapi.com/api/v5/pix2pix", requestOptions)  
  .then(response => response.text())  
  .then(result => console.log(result))  
  .catch(error => console.log('error', error));  

```

```
<?php  
  
$payload = [  
  "key" => "",   
  "init_image" => "https://d1okzptojspljx.cloudfront.net/generations/b3341a09-082e-474e-989f-72ec3f3bf7aa-0.png",   
  "prompt" => "make him woman",   
  "image_guidance_scale" => 1,   
  "steps" => 50,   
  "guidance_scale" => 7  
];  
  
$curl = curl_init();  
  
curl_setopt_array($curl, array(  
  CURLOPT_URL => 'https://stablediffusionapi.com/api/v5/pix2pix',  
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
  'url': 'https://stablediffusionapi.com/api/v5/pix2pix',  
  'headers': {  
    'Content-Type': 'application/json'  
  },  
  body: JSON.stringify({  
    "key": "",  
    "init_image" : "https://d1okzptojspljx.cloudfront.net/generations/b3341a09-082e-474e-989f-72ec3f3bf7aa-0.png",  
    "prompt" : "make him woman",  
    "image_guidance_scale" : 1,  
    "steps" : 50,  
    "guidance_scale" : 7  
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
  
url = "https://stablediffusionapi.com/api/v5/pix2pix"  
  
payload = json.dumps({  
  "key": "",  
  "init_image" : "https://d1okzptojspljx.cloudfront.net/generations/b3341a09-082e-474e-989f-72ec3f3bf7aa-0.png",  
  "prompt" : "make him woman",  
  "image_guidance_scale" : 1,  
  "steps" : 50,  
  "guidance_scale" : 7  
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
RequestBody body = RequestBody.create(mediaType, "{\n  \"key\": \"\",\n  \"init_image\" : \"https://d1okzptojspljx.cloudfront.net/generations/b3341a09-082e-474e-989f-72ec3f3bf7aa-0.png\",\n    \"prompt\" : \"make him woman\",\n  \"image_guidance_scale\" : 1,\n  \"steps\" : 50,\n  \"guidance_scale\" : 7\n}");  
Request request = new Request.Builder()  
  .url("https://stablediffusionapi.com/api/v5/pix2pix")  
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
    "generationTime": 4.5880513191223145,  
    "id": 14624464,  
    "output": "https://pub-8b49af329fae499aa563997f5d4068a4.r2.dev/generations/186bd505-607d-4627-bf00-dcf3b35bfdab-0.png"  
}  

```
[PreviousImage Mixer](/docs/image-editing/imagemixer)[NextRemove Background](/docs/image-editing/removebg-createmask)* [Overview](#overview)
* [Request](#request)
* [Body Attributes](#body-attributes)
* [Example](#example)
	+ [Body](#body)
	+ [Request](#request-1)
	+ [Response](#response)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



