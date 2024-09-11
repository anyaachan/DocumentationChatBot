




Enterprise: Load Model Endpoint \| Stable Diffusion API Documentation








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
	+ [API Overview](/docs/enterprise-plan/overview)
	+ [System Details](/docs/enterprise-plan/system-details)
	+ [Restart Server](/docs/enterprise-plan/restart-server)
	+ [Update Server](/docs/enterprise-plan/update-server)
	+ [Update S3 Details](/docs/enterprise-plan/update-s3-details)
	+ [Clear Cache](/docs/enterprise-plan/clear-cache)
	+ [List Schedulers](/docs/enterprise-plan/list-schedulers)
	+ [Load Model](/docs/enterprise-plan/load-model)
	+ [Verify Model](/docs/enterprise-plan/verify-model)
	+ [Get All Models](/docs/enterprise-plan/get-all-models)
	+ [Delete Model](/docs/enterprise-plan/delete-model)
	+ [Controlnet](/docs/enterprise-plan/controlnet-ep)
	+ [Text to Image](/docs/enterprise-plan/text2img)
	+ [Text to Video](/docs/enterprise-plan/text2video)
	+ [Image to Image](/docs/enterprise-plan/img2img)
	+ [Inpainting](/docs/enterprise-plan/inpainting)
	+ [Super Resolution](/docs/enterprise-plan/super-resolution)
	+ [Upload Image](/docs/enterprise-plan/upload-image)
	+ [Sync Model](/docs/enterprise-plan/sync-model)
	+ [Load Vae](/docs/enterprise-plan/load-vae)
	+ [NSFW Image Check](/docs/enterprise-plan/nsfw-image-check)
	+ [Fetch Queued Images](/docs/enterprise-plan/fetch-queue-image)
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
* [Enterprise Plan](/docs/category/enterprise-plan)
* Load Model
On this pageEnterprise: Load Model Endpoint
===============================

* [enterprise/system\_details](/docs/enterprise-plan/system-details)
* [enterprise/restart\_server](/docs/enterprise-plan/restart-server)
* [enterprise/update\_server](/docs/enterprise-plan/update-server)
* [enterprise/update\_s3](/docs/enterprise-plan/update-s3-details)
* [enterprise/clear\_cache](/docs/enterprise-plan/clear-cache)
* [enterprise/schedulers\_list](/docs/enterprise-plan/list-schedulers)
* [enterprise/load\_model](/docs/enterprise-plan/load-model)
* [enterprise/verify\_model](/docs/enterprise-plan/verify-model)
* [enterprise/get\_all\_models](/docs/enterprise-plan/get-all-models)
* [enterprise/delete\_model](/docs/enterprise-plan/delete-model)
* [enterprise/controlnet](/docs/enterprise-plan/controlnet-ep)
* [enterprise/text2img](/docs/enterprise-plan/text2img)
* [enterprise/text2video](/docs/enterprise-plan/img2img)
* [enterprise/text2video](/docs/enterprise-plan/text2video)
* [enterprise/inpaint](/docs/enterprise-plan/inpainting)
* [enterprise/super\_resolution](/docs/enterprise-plan/super-resolution)
* [enterprise/upload\_image](/docs/enterprise-plan/upload-image)
* [enterprise/sync\_image](/docs/enterprise-plan/sync-model)
* [enterprise/load\_vae](/docs/enterprise-plan/load-vae)
* [enterprise/nsfw\_image\_check](/docs/enterprise-plan/nsfw-image-check)
* [enterprise/fetch\_queue\_image](/docs/enterprise-plan/fetch-queue-image)
Overview[â](#overview "Direct link to Overview")
--------------------------------------------------

This endpoint is used to load a model to your dedicated server.

Request[â](#request "Direct link to Request")
-----------------------------------------------


```
--request POST 'https://stablediffusionapi.com/api/v1/enterprise/load_model' \  

```
Send a `POST` request to <https://stablediffusionapi.com/api/v1/enterprise/load_model> endpoint. 

noteThe model selected for loading has to be a **diffusers** model.

Watch the how\-to video to see it in action.

Attributes[â](#attributes "Direct link to Attributes")
--------------------------------------------------------



| Parameter | Description |
| --- | --- |
| **key** | Your enterprise API Key used for request authorization. |
| **url** | The URL of the **huggingface** model, **.ckpt** download link, or **trained** model from our Dreambooth API. |
| **model\_id** | Choose a name(ID) for your model. The loaded model will be saved under this ID, so you can refer to it when generating images. |
| **from\_safetensors** | Set this to "yes" if you are loading a **.safetensor** file; otherwise pass "no". |
| **model\_type** | Available options: "huggingface", "api\_trained", "custom\_ckpt", "lora", "embeddings", "controlnet". |
| **revision** | Specify whether the loaded model is "fp16" or "fp32". |
| **webhook** | A webhook to receive response on model load events. |
| **upcast\_attention** | Set this to "yes" **only** when you are loading a **stable diffusion 2\.1** model; otherwise keep it "no". |

### ControlNet Model url and model\_id table[â](#controlnet-model-url-and-model_id-table "Direct link to ControlNet Model url and model_id table")



| url | model\_id |
| --- | --- |
| lllyasviel/control\_v11p\_sd15\_inpaint | inpaint |
| lllyasviel/control\_v11e\_sd15\_ip2p | ip2p |
| lllyasviel/control\_v11f1e\_sd15\_tile | tile |
| lllyasviel/control\_v11e\_sd15\_shuffle | shuffle |
| lllyasviel/control\_v11p\_sd15\_softedge | softedge |
| lllyasviel/control\_v11p\_sd15\_scribble | scribble |
| lllyasviel/control\_v11p\_sd15\_lineart | lineart |
| lllyasviel/control\_v11p\_sd15\_normalbae | normalbae |
| lllyasviel/control\_v11f1p\_sd15\_depth | depth |
| lllyasviel/control\_v11p\_sd15\_mlsd | mlsd |
| lllyasviel/control\_v11p\_sd15\_canny | canny |

Examples[â](#examples "Direct link to Examples")
--------------------------------------------------

### Load a .ckpt or .safetensors Model from Civitai[â](#load-a-ckpt-or-safetensors-model-from-civitai "Direct link to Load a .ckpt or .safetensors Model from Civitai")

Body Raw
```
{  
  "key": "enterprise_api_key",  
  "url": "https://civitai.com/api/download/models/94640",  
  "model_id": "majicmix-realistic",  
  "model_type": "custom_ckpt",  
  "from_safetensors": "yes",  
  "webhook": "https://stablediffusionapi.com",  
  "revision": "fp32",  
  "upcast_attention": "no"  
}  

```
### Load a .ckpt Model from Civitai[â](#load-a-ckpt-model-from-civitai "Direct link to Load a .ckpt Model from Civitai")

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
  "url": "https://civitai.com/api/download/models/94640",  
  "model_id": "majicmix-realistic",  
  "model_type": "custom_ckpt",  
  "from_safetensors": "yes",  
  "webhook": "https://stablediffusionapi.com",  
  "revision": "fp32",  
  "upcast_attention": "no"  
});  
  
var requestOptions = {  
  method: 'POST',  
  headers: myHeaders,  
  body: raw,  
  redirect: 'follow'  
};  
  
model_reload("https://stablediffusionapi.com/api/v1/enterprise/load_model", requestOptions)  
  .then(response => response.text())  
  .then(result => console.log(result))  
  .catch(error => console.log('error', error));  

```

```
<?php  
  
$payload = [  
  "key" => "",   
  "url": "https://civitai.com/api/download/models/94640",  
  "model_id": "majicmix-realistic",  
  "model_type": "custom_ckpt",  
  "from_safetensors": "yes",  
  "webhook": "https://stablediffusionapi.com",  
  "revision": "fp32",  
  "upcast_attention": "no"  
];  
  
$curl = curl_init();  
  
curl_setopt_array($curl, array(  
  CURLOPT_URL => 'https://stablediffusionapi.com/api/v1/enterprise/load_model',  
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
  'url': 'https://stablediffusionapi.com/api/v1/enterprise/load_model',  
  'headers': {  
    'Content-Type': 'application/json'  
  },  
  body: JSON.stringify({  
    "key": "",  
    "url": "https://civitai.com/api/download/models/94640",  
    "model_id": "majicmix-realistic",  
    "model_type": "custom_ckpt",  
    "from_safetensors": "yes",  
    "webhook": "https://stablediffusionapi.com",  
    "revision": "fp32",  
    "upcast_attention": "no"  
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
  
url = "https://stablediffusionapi.com/api/v1/enterprise/load_model"  
  
payload = json.dumps({  
  "key": "",  
  "url": "https://civitai.com/api/download/models/94640",  
  "model_id": "majicmix-realistic",  
  "model_type": "custom_ckpt",  
  "from_safetensors": "yes",  
  "webhook": "https://stablediffusionapi.com",  
  "revision": "fp32",  
  "upcast_attention": "no"  
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
RequestBody body = RequestBody.create(mediaType, "{\n    \"key\": \"\",\n    \"url\": \"https://civitai.com/api/download/models/94640\",\n    \"model_id\": \"nckpt-model\",\n    \"model_type\": \"custom_ckpt\",\n    \"webhook\": \"https://stablediffusionapi.com\",\n    \"revision\": \"fp32\",\n    \"upcast_attention\": \"no\"\n}");  
Request request = new Request.Builder()  
  .url("https://stablediffusionapi.com/api/v1/enterprise/load_model")  
  .method("POST", body)  
  .addHeader("Content-Type", "application/json")  
  .build();  
Response response = client.newCall(request).execute();  

```
### Load a Huggingface Model[â](#load-a-huggingface-model "Direct link to Load a Huggingface Model")

Body Raw
```
{  
  "key": "enterprise_api_key",  
  "url": "wavymulder/Analog-Diffusion",  
  "model_id": "analog-diffusion",  
  "model_type": "huggingface",  
  "from_safetensors": "no",  
  "webhook": "https://stablediffusionapi.com",  
  "revision": "fp32",  
  "upcast_attention": "no"  
}  

```
### Request: Load a Huggingface Model[â](#request-load-a-huggingface-model "Direct link to Request: Load a Huggingface Model")

* JS
* PHP
* NODE
* PYTHON
* JAVA


```
var myHeaders = new Headers();  
myHeaders.append("Content-Type", "application/json");  
  
var raw = JSON.stringify({  
  "key": "enterprise_api_key",  
  "url": "wavymulder/Analog-Diffusion",  
  "model_id": "analog-diffusion",  
  "model_type": "huggingface",  
  "from_safetensors": "no",  
  "webhook": "https://stablediffusionapi.com",  
  "revision": "fp32",  
  "upcast_attention": "no"  
});  
  
var requestOptions = {  
  method: 'POST',  
  headers: myHeaders,  
  body: raw,  
  redirect: 'follow'  
};  
  
model_reload("https://stablediffusionapi.com/api/v1/enterprise/load_model", requestOptions)  
  .then(response => response.text())  
  .then(result => console.log(result))  
  .catch(error => console.log('error', error));  

```

```
<?php  
  
$payload = [  
  "key" => "enterprise_api_key",   
  "url" => "wavymulder/Analog-Diffusion",   
  "model_id" => "analog-diffusion",   
  "model_type" => "huggingface",   
  "from_safetensors": "no",  
  "webhook" => "https://stablediffusionapi.com",   
  "revision" => "fp32",   
  "upcast_attention" => "no"   
];  
  
$curl = curl_init();  
  
curl_setopt_array($curl, array(  
  CURLOPT_URL => 'https://stablediffusionapi.com/api/v1/enterprise/load_model',  
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
  'url': 'https://stablediffusionapi.com/api/v1/enterprise/load_model',  
  'headers': {  
    'Content-Type': 'application/json'  
  },  
  body: JSON.stringify({  
    "key": "enterprise_api_key",  
    "url": "wavymulder/Analog-Diffusion",  
    "model_id": "analog-diffusion",  
    "model_type": "huggingface",  
    "from_safetensors": "no",  
    "webhook": "https://stablediffusionapi.com",  
    "revision": "fp32",  
    "upcast_attention": "no"  
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
  
url = "https://stablediffusionapi.com/api/v1/enterprise/load_model"  
  
payload = json.dumps({  
  "key": "enterprise_api_key",  
  "url": "wavymulder/Analog-Diffusion",  
  "model_id": "analog-diffusion",  
  "model_type": "huggingface",  
  "from_safetensors": "no",  
  "webhook": "https://stablediffusionapi.com",  
  "revision": "fp32",  
  "upcast_attention": "no"  
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
RequestBody body = RequestBody.create(mediaType, "{\n    \"key\": \"enterprise_api_key\",\n    \"url\": \"wavymulder/Analog-Diffusion\",\n    \"model_id\": \"analog-diffusion\",\n    \"model_type\": \"huggingface\",\n    \"webhook\": \"https://stablediffusionapi.com\",\n    \"revision\": \"fp32\",\n    \"upcast_attention\": \"no\"\n}");  
Request request = new Request.Builder()  
  .url("https://stablediffusionapi.com/api/v1/enterprise/load_model")  
  .method("POST", body)  
  .addHeader("Content-Type", "application/json")  
  .build();  
Response response = client.newCall(request).execute();  

```
### Request Body: Load a ControlNet Model[â](#request-body-load-a-controlnet-model "Direct link to Request Body: Load a ControlNet Model")

Body Raw
```
{  
  "key": "enterprise_api_key",  
  "url": "lllyasviel/control_v11p_sd15_canny",  
  "model_id": "canny",  
  "model_type": "controlnet",  
  "webhook": "https://stablediffusionapi.com",  
  "revision": "fp32",  
  "upcast_attention": "no"  
}  

```
### Request: Load a ControlNet Model[â](#request-load-a-controlnet-model "Direct link to Request: Load a ControlNet Model")

* JS
* PHP
* NODE
* PYTHON
* JAVA


```
var myHeaders = new Headers();  
myHeaders.append("Content-Type", "application/json");  
  
var raw = JSON.stringify({  
  "key": "enterprise_api_key",  
  "url": "lllyasviel/control_v11p_sd15_canny",  
  "model_id": "canny",  
  "model_type": "controlnet",  
  "webhook": "https://stablediffusionapi.com",  
  "revision": "fp32",  
  "upcast_attention": "no"  
});  
  
var requestOptions = {  
  method: 'POST',  
  headers: myHeaders,  
  body: raw,  
  redirect: 'follow'  
};  
  
model_reload("https://stablediffusionapi.com/api/v1/enterprise/load_model", requestOptions)  
  .then(response => response.text())  
  .then(result => console.log(result))  
  .catch(error => console.log('error', error));  

```

```
<?php  
  
$payload = [  
  "key" => "enterprise_api_key",   
  "url" => "lllyasviel/control_v11p_sd15_canny",   
  "model_id" => "hed",   
  "model_type" => "controlnet",   
  "webhook" => "https://stablediffusionapi.com",   
  "revision" => "fp32",   
  "upcast_attention" => "no"  
];  
  
$curl = curl_init();  
  
curl_setopt_array($curl, array(  
  CURLOPT_URL => 'https://stablediffusionapi.com/api/v1/enterprise/load_model',  
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
  'url': 'https://stablediffusionapi.com/api/v1/enterprise/load_model',  
  'headers': {  
    'Content-Type': 'application/json'  
  },  
  body: JSON.stringify({  
    "key": "enterprise_api_key",  
    "url": "lllyasviel/control_v11p_sd15_canny",  
    "model_id": "canny",  
    "model_type": "controlnet",  
    "webhook": "https://stablediffusionapi.com",  
    "revision": "fp32",  
    "upcast_attention": "no"  
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
  
url = "https://stablediffusionapi.com/api/v1/enterprise/load_model"  
  
payload = json.dumps({  
  "key": "enterprise_api_key",  
  "url": "lllyasviel/control_v11p_sd15_canny",  
  "model_id": "canny",  
  "model_type": "controlnet",  
  "webhook": "https://stablediffusionapi.com",  
  "revision": "fp32",  
  "upcast_attention": "no"  
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
RequestBody body = RequestBody.create(mediaType, "{\n    \"key\": \"enterprise_api_key\",\n    \"url\": \"lllyasviel/control_v11p_sd15_canny\",\n    \"model_id\": \"hed\",\n    \"model_type\": \"controlnet\",\n    \"webhook\": \"https://stablediffusionapi.com\",\n    \"revision\": \"fp32\",\n    \"upcast_attention\": \"no\"\n}");  
Request request = new Request.Builder()  
  .url("https://stablediffusionapi.com/api/v1/enterprise/load_model")  
  .method("POST", body)  
  .addHeader("Content-Type", "application/json")  
  .build();  
Response response = client.newCall(request).execute();  

```
### Response[â](#response "Direct link to Response")


```
{  
  "message": "model load started",  
  "status": "success"  
}  

```
[PreviousList Schedulers](/docs/enterprise-plan/list-schedulers)[NextVerify Model](/docs/enterprise-plan/verify-model)* [Overview](#overview)
* [Request](#request)
* [Attributes](#attributes)
	+ [ControlNet Model url and model\_id table](#controlnet-model-url-and-model_id-table)
* [Examples](#examples)
	+ [Load a .ckpt or .safetensors Model from Civitai](#load-a-ckpt-or-safetensors-model-from-civitai)
	+ [Load a .ckpt Model from Civitai](#load-a-ckpt-model-from-civitai)
	+ [Load a Huggingface Model](#load-a-huggingface-model)
	+ [Request: Load a Huggingface Model](#request-load-a-huggingface-model)
	+ [Request Body: Load a ControlNet Model](#request-body-load-a-controlnet-model)
	+ [Request: Load a ControlNet Model](#request-load-a-controlnet-model)
	+ [Response](#response)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



