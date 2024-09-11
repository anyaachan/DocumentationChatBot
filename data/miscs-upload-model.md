




Upload Model \| Stable Diffusion API Documentation








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
* Upload Model
On this pageUpload Model
============

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
* [v5/uncensored\_chat](/docs/miscs/uncensored-chat)
* [v5/interior](/docs/miscs/interior)
Overview[â](#overview "Direct link to Overview")
--------------------------------------------------

This endpoint is used to load a private or public model

Request[â](#request "Direct link to Request")
-----------------------------------------------


```
--request POST 'https://stablediffusionapi.com/api/v3/load_model' \  

```
Send a `POST` request to <https://stablediffusionapi.com/api/v3/load_model> endpoint. 

noteTo load a private model you must have purchased model credit from [private model page.](https://stablediffusionapi.com/dashboard/models)

Attributes[â](#attributes "Direct link to Attributes")
--------------------------------------------------------



| Parameter | Description |
| --- | --- |
| **key** | Your API Key used for request authorization. |
| **url** | The URL of the **huggingface** model, **ckpt** download link, or **safetensors** model |
| **model\_id** | Choose a name(ID) for your model. The loaded model will be saved under this ID, so you can refer to it when generating images. |
| **force\_load** | Set this to "yes" if you want to reload automatically once upload fails; otherwise pass "no". |
| **model\_format** | Available options: "diffusers", "safetensors", "ckpt". |
| **revision** | Specify whether the loaded model is "fp16" or "fp32". |
| **model\_category** | The category of the model you want to upload, it accepts any of these;stable\_diffusion,stable\_diffusion\_xl, controlnet, lora, embeddings,vae |
| **model\_visibility** | It accepts **private** or **public**. |
| **model\_name** | This is the name you want to give your model. |
| **model\_image** | A valid image url of to display the model when uploaded. |
| **hf\_upload** | It accepts **yes** or **no**. |

Examples[â](#examples "Direct link to Examples")
--------------------------------------------------

### Load a ckpt or safetensors Model from Civitai[â](#load-a-ckpt-or-safetensors-model-from-civitai "Direct link to Load a ckpt or safetensors Model from Civitai")

Body Raw
```
{  
    "key": "api_key",  
    "url": "https://civitai.com/api/download/models/132760?type=Model&format=SafeTensor&size=pruned&fp=fp16",  
    "model_id": "majicmix-realistic",  
    "revision": "fp32",  
    "model_id": "stable-diffusion-1.0-inpainting-0.1",  
    "force_load": "yes",   
    "revision": "fp16",  
    "model_category": "stable_diffusion_xl",  
    "model_format": "safetensors",  
    "model_visibility": "public",  
    "model_name": "stable-diffusion-1.0-inpainting-0.1",  
    "model_image": "https://cdn2.stablediffusionapi.com/generations/1a14cab3-cc79-4cee-ab28-29379bff766b-0.png",  
    "hf_upload": "no"  
}  

```
### Load a diffusers[â](#load-a-diffusers "Direct link to Load a diffusers")

Body Raw
```
{  
    "key": "api_key",  
    "url": "diffusers/stable-diffusion-xl-1.0-inpainting-0.1",  
    "model_id": "stable-diffusion-xl-1.0-inpainting-0.1",  
    "force_load": "yes",   
    "revision": "fp16",  
    "model_category": "stable_diffusion_xl",  
    "model_format": "diffusers",  
    "model_visibility": "public",  
    "model_name": "stable-diffusion-xl-1.0-inpainting-0.1",  
    "model_image": "https://cdn2.stablediffusionapi.com/generations/1a14cab3-cc79-4cee-ab28-29379bff766b-0.png",  
    "hf_upload": "no"  
}  

```
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
    "url": "diffusers/stable-diffusion-xl-1.0-inpainting-0.1",  
    "model_id": "stable-diffusion-xl-1.0-inpainting-0.1",  
    "force_load": "yes",   
    "revision": "fp16",  
    "model_category": "stable_diffusion_xl",  
    "model_format": "diffusers",  
    "model_visibility": "private",  
    "model_name": "stable-diffusion-xl-1.0-inpainting-0.1",  
    "model_image": "https://cdn2.stablediffusionapi.com/generations/1a14cab3-cc79-4cee-ab28-29379bff766b-0.png",  
    "hf_upload": "no"  
});  
  
var requestOptions = {  
  method: 'POST',  
  headers: myHeaders,  
  body: raw,  
  redirect: 'follow'  
};  
  
model_reload("https://stablediffusionapi.com/api/v3/load_model", requestOptions)  
  .then(response => response.text())  
  .then(result => console.log(result))  
  .catch(error => console.log('error', error));  

```

```
<?php  
  
$payload = [  
    "key" => "",   
    "url" => "diffusers/stable-diffusion-xl-1.0-inpainting-0.1",  
    "model_id" => "stable-diffusion-xl-1.0-inpainting-0.1",  
    "force_load" => "yes",   
    "revision" => "fp16",  
    "model_category" => "stable_diffusion_xl",  
    "model_format" => "diffusers",  
    "model_visibility" =>  "private",  
    "model_name" =>  "stable-diffusion-xl-1.0-inpainting-0.1",  
    "model_image" =>  "https://cdn2.stablediffusionapi.com/generations/1a14cab3-cc79-4cee-ab28-29379bff766b-0.png",  
    "hf_upload" =>  "no"  
];  
  
$curl = curl_init();  
  
curl_setopt_array($curl, array(  
  CURLOPT_URL => 'https://stablediffusionapi.com/api/v3/load_model',  
  CURLOPT_RETURNTRANSFER => true,  
  CURLOPT_ENCODING => '',  
  CURLOPT_MAXREDIRS => 10,  
  CURLOPT_TIMEOUT => 0,  
  CURLOPT_FOLLOWLOCATION => true,  
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,  
  CURLOPT_CUSTOMREQUEST => 'POST',  
  CURLOPT_POSTFIELDS =>  json_encode($payload),  
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
  'url': 'https://stablediffusionapi.com/api/v3/load_model',  
  'headers': {  
    'Content-Type': 'application/json'  
  },  
  body: JSON.stringify({  
    "key": "",  
    "url": "diffusers/stable-diffusion-xl-1.0-inpainting-0.1",  
    "model_id": "stable-diffusion-xl-1.0-inpainting-0.1",  
    "force_load": "yes",   
    "revision": "fp16",  
    "model_category": "stable_diffusion_xl",  
    "model_format": "diffusers",  
    "model_visibility": "private",  
    "model_name": "stable-diffusion-xl-1.0-inpainting-0.1",  
    "model_image": "https://cdn2.stablediffusionapi.com/generations/1a14cab3-cc79-4cee-ab28-29379bff766b-0.png",  
    "hf_upload": "no"  
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
  
url = "https://stablediffusionapi.com/api/v3/load_model"  
  
payload = json.dumps({  
    "key": "",  
    "url": "diffusers/stable-diffusion-xl-1.0-inpainting-0.1",  
    "model_id": "stable-diffusion-xl-1.0-inpainting-0.1",  
    "force_load": "yes",   
    "revision": "fp16",  
    "model_category": "stable_diffusion_xl",  
    "model_format": "diffusers",  
    "model_visibility": "private",  
    "model_name": "stable-diffusion-xl-1.0-inpainting-0.1",  
    "model_image": "https://cdn2.stablediffusionapi.com/generations/1a14cab3-cc79-4cee-ab28-29379bff766b-0.png",  
    "hf_upload": "no"  
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
RequestBody body = RequestBody.create(mediaType, "{\n    \"key\": \"\",\n    \"url\": \"diffusers/stable-diffusion-xl-1.0-inpainting-0.1\",\n    \"model_id\": \"stable-diffusion-xl-1.0-inpainting-0.1\",\n    \"force_load\": \"yes\", \n    \"revision\": \"fp16\",\n    \"model_category\": \"stable_diffusion_xl\",\n    \"model_subcategory\": null,\n    \"model_format\": \"diffusers\",\n    \"model_visibility\": \"private\",\n    \"model_name\": \"stable-diffusion-xl-1.0-inpainting-0.1\",\n    \"model_image\": \"https://cdn2.stablediffusionapi.com/generations/1a14cab3-cc79-4cee-ab28-29379bff766b-0.png\",\n    \"hf_upload\": \"no\"\n}");  
Request request = new Request.Builder()  
  .url("https://stablediffusionapi.com/api/v3/load_model")  
  .method("POST", body)  
  .addHeader("Content-Type", "application/json")  
  .build();  
Response response = client.newCall(request).execute();  

```
### Response[â](#response "Direct link to Response")


```
{  
  "status": "success",  
  "message": "model load started",  
}  

```
[PreviousNSFW Image Check](/docs/miscs/nsfw-image-check)[NextCreate Room Interior](/docs/miscs/interior)* [Overview](#overview)
* [Request](#request)
* [Attributes](#attributes)
* [Examples](#examples)
	+ [Load a ckpt or safetensors Model from Civitai](#load-a-ckpt-or-safetensors-model-from-civitai)
	+ [Load a diffusers](#load-a-diffusers)
	+ [Response](#response)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



