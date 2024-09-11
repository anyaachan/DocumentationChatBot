




Train a Dreambooth Model with Custom Images \| Stable Diffusion API Documentation








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
* Dreambooth Training
On this pageTrain a Dreambooth Model with Custom Images
===========================================

* [fine\_tune](/docs/train-model/finetune)
* [fine\_tune\_v2](/docs/train-model/finetune-v2)
* [fine\_tune\_status](/docs/train-model/finetune-status)
* [cancle\_training](/docs/train-model/cancel-training)
* [finetune\_list](/docs/train-model/finetune-list)
* [finetune/delete](/docs/train-model/finetune-delete)
* [base64\_crop](/docs/train-model/base64-crop)
* [lora\_finetune](/docs/train-model/lora-finetune)
Overview[â](#overview "Direct link to Overview")
--------------------------------------------------

Using this endpoint you can train a Dreambooth model with your own images. You can train a model on any object or person.

Request[â](#request "Direct link to Request")
-----------------------------------------------


```
--request POST 'https://stablediffusionapi.com/api/v3/fine_tune' \  

```
Make a `POST` request to <https://stablediffusionapi.com/api/v3/fine_tune> endpoint and pass the required parameters as a request body. 

Now you can train a model on any other models used as a base model and get its style. You can choose to train on models like `midjourney`, `portraitplus` and many more. 

infoGet the **base\_model\_id** from **[here](https://stablediffusionapi.com/models)**. 

tipYou can also read our **[blog article](https://stablediffusionapi.com/blog/stable-diffusion-api/how-to-finetune-dreambooth-model)** to learn more about model training.

Body Attributes[â](#body-attributes "Direct link to Body Attributes")
-----------------------------------------------------------------------



| Parameter | Description |
| --- | --- |
| **key** | Your API Key used for request authorization |
| **instance\_prompt** | Text prompt with how you want to call your trained person/object |
| **class\_prompt** | Classification of the trained person/object |
| **base\_model\_id** | Base model ID to train your model on |
| **images** | Pass accessible direct links to images, cropped to 512 x 512 px. A good number is about 7\-8 images. |
| **training\_type** | The type of the object you are training on |
| **max\_train\_steps** | Set it at 2 times the number of images (Ni\*2; maximum value 2000\) |
| **webhook** | Get a post call when training is complete |

### Training Types[â](#training-types "Direct link to Training Types")

The table below lists all the possible values for the `training_type` parameter.



| Value | Description |
| --- | --- |
| **men** | Train on faces of men. |
| **female** | Train on faces of females. |
| **couple** | Train on couples of male and female; in images array pass images of couples, instead of images of a single person. |
| **null** | Train on object or anything. |

### Webhook Post JSON[â](#webhook-post-json "Direct link to Webhook Post JSON")

This is an example webhook post call in JSON format.


```
{  
 "status": "success",  
 "training_status": "deploying_gpu",  
 "logs": "it will take upto 25 minutes",  
 "model_id": "F5jvdzGnYi",  
}  

```
#### Training Status Values[â](#training-status-values "Direct link to Training Status Values")

The table below describes all possible training statuses.



| Status | Description |
| --- | --- |
| deploying\_gpu | Deploying GPU |
| training\_started | Training started |
| training\_success | Training completed successfully |
| trained\_model\_compressing | Compressing the trained model |
| trained\_model\_uploading | Uploading the trained model |
| trained\_model\_uploaded | Trained model uploaded |
| deploying\_model | Deploying the trained model |
| model\_ready | The trained model is ready for use |

Example[â](#example "Direct link to Example")
-----------------------------------------------

### Body[â](#body "Direct link to Body")

Body
```
{  
  "key": "",  
  "instance_prompt": "photo of adhik person",  
  "class_prompt": "photo of person",  
  "base_model_id": "portraitplus-diffusion",  
  "images": [  
    "https://stablediffusionapi.com/storage/avatars/AdhikJoshi_00001.png",  
    "https://stablediffusionapi.com/storage/avatars/AdhikJoshi_00002.png",  
    "https://stablediffusionapi.com/storage/avatars/AdhikJoshi_00003.png",  
    "https://stablediffusionapi.com/storage/avatars/AdhikJoshi_00004.png",  
    "https://stablediffusionapi.com/storage/avatars/AdhikJoshi_00005.png",  
    "https://stablediffusionapi.com/storage/avatars/AdhikJoshi_00006.png",  
    "https://stablediffusionapi.com/storage/avatars/AdhikJoshi_00007.png"  
  ],  
  "seed": "0",  
  "training_type": "men",  
  "max_train_steps": "2000",  
  "webhook": ""  
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
  "instance_prompt": "photo of adhik person",  
  "class_prompt": "photo of person",  
  "base_model_id": "portraitplus-diffusion",  
  "images": [  
    "https://stablediffusionapi.com/storage/avatars/AdhikJoshi_00001.png",  
    "https://stablediffusionapi.com/storage/avatars/AdhikJoshi_00002.png",  
    "https://stablediffusionapi.com/storage/avatars/AdhikJoshi_00003.png",  
    "https://stablediffusionapi.com/storage/avatars/AdhikJoshi_00004.png",  
    "https://stablediffusionapi.com/storage/avatars/AdhikJoshi_00005.png",  
    "https://stablediffusionapi.com/storage/avatars/AdhikJoshi_00006.png",  
    "https://stablediffusionapi.com/storage/avatars/AdhikJoshi_00007.png"  
  ],  
  "seed": "0",  
  "training_type": "men",  
  "max_train_steps": "2000",  
  "webhook": ""  
});  
  
var requestOptions = {  
  method: 'POST',  
  headers: myHeaders,  
  body: raw,  
  redirect: 'follow'  
};  
  
fetch("https://stablediffusionapi.com/api/v3/fine_tune", requestOptions)  
  .then(response => response.text())  
  .then(result => console.log(result))  
  .catch(error => console.log('error', error));  

```

```
<?php  
  
$payload = [  
  "key" => "",   
  "instance_prompt" => "photo of adhik person",   
  "class_prompt" => "photo of person",   
  "base_model_id" => "portraitplus-diffusion",   
  "images" => [  
    "https://stablediffusionapi.com/storage/avatars/AdhikJoshi_00001.png",   
    "https://stablediffusionapi.com/storage/avatars/AdhikJoshi_00002.png",   
    "https://stablediffusionapi.com/storage/avatars/AdhikJoshi_00003.png",   
    "https://stablediffusionapi.com/storage/avatars/AdhikJoshi_00004.png",   
    "https://stablediffusionapi.com/storage/avatars/AdhikJoshi_00005.png",   
    "https://stablediffusionapi.com/storage/avatars/AdhikJoshi_00006.png",   
    "https://stablediffusionapi.com/storage/avatars/AdhikJoshi_00007.png"   
  ],   
  "seed" => "0",   
  "training_type" => "men",   
  "max_train_steps" => "2000",   
  "webhook" => ""   
];  
  
$curl = curl_init();  
  
curl_setopt_array($curl, array(  
  CURLOPT_URL => 'https://stablediffusionapi.com/api/v3/fine_tune',  
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
  'url': 'https://stablediffusionapi.com/api/v3/fine_tune',  
  'headers': {  
    'Content-Type': 'application/json'  
  },  
  body: JSON.stringify({  
    "key": "",  
    "instance_prompt": "photo of adhik person",  
    "class_prompt": "photo of person",  
    "base_model_id": "portraitplus-diffusion",  
    "images": [  
      "https://stablediffusionapi.com/storage/avatars/AdhikJoshi_00001.png",  
      "https://stablediffusionapi.com/storage/avatars/AdhikJoshi_00002.png",  
      "https://stablediffusionapi.com/storage/avatars/AdhikJoshi_00003.png",  
      "https://stablediffusionapi.com/storage/avatars/AdhikJoshi_00004.png",  
      "https://stablediffusionapi.com/storage/avatars/AdhikJoshi_00005.png",  
      "https://stablediffusionapi.com/storage/avatars/AdhikJoshi_00006.png",  
      "https://stablediffusionapi.com/storage/avatars/AdhikJoshi_00007.png"  
    ],  
    "seed": "0",  
    "training_type": "men",  
    "max_train_steps": "2000",  
    "webhook": ""  
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
  
url = "https://stablediffusionapi.com/api/v3/fine_tune"  
  
payload = json.dumps({  
  "key": "",  
  "instance_prompt": "photo of adhik person",  
  "class_prompt": "photo of person",  
  "base_model_id": "portraitplus-diffusion",  
  "images": [  
    "https://stablediffusionapi.com/storage/avatars/AdhikJoshi_00001.png",  
    "https://stablediffusionapi.com/storage/avatars/AdhikJoshi_00002.png",  
    "https://stablediffusionapi.com/storage/avatars/AdhikJoshi_00003.png",  
    "https://stablediffusionapi.com/storage/avatars/AdhikJoshi_00004.png",  
    "https://stablediffusionapi.com/storage/avatars/AdhikJoshi_00005.png",  
    "https://stablediffusionapi.com/storage/avatars/AdhikJoshi_00006.png",  
    "https://stablediffusionapi.com/storage/avatars/AdhikJoshi_00007.png"  
  ],  
  "seed": "0",  
  "training_type": "men",  
  "max_train_steps": "2000",  
  "webhook": ""  
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
RequestBody body = RequestBody.create(mediaType, "{\n    \"key\": \"\",\n    \"instance_prompt\": \"a photo of adhik person\",\n    \"class_prompt\" : \"a photo of person\",\n    \"base_model_id\" : \"portraitplus-diffusion\",\n    \"images\": [\n        \"https://stablediffusionapi.com/storage/generations/AdhikJoshi_00000.png\",\n        \"https://stablediffusionapi.com/storage/generations/AdhikJoshi_00001.png\",\n        \"https://stablediffusionapi.com/storage/generations/AdhikJoshi_00002.png\",\n        \"https://stablediffusionapi.com/storage/generations/AdhikJoshi_00003.png\",\n        \"https://stablediffusionapi.com/storage/generations/AdhikJoshi_00004.png\",\n        \"https://stablediffusionapi.com/storage/generations/AdhikJoshi_00005.png\",\n        \"https://stablediffusionapi.com/storage/generations/AdhikJoshi_00006.png\",\n        \"https://stablediffusionapi.com/storage/generations/AdhikJoshi_00007.png\"\n    ],\n    \"seed\": \"0\",\n   \"training_type\": \"men\",\n  \"max_train_steps\": \"2000\",\n  \"webhook\": \"\"\n}");  
  
Request request = new Request.Builder()  
  .url("https://stablediffusionapi.com/api/v3/fine_tune")  
  .method("POST", body)  
  .addHeader("Content-Type", "application/json")  
  .build();  
Response response = client.newCall(request).execute();  

```
### Response[â](#response "Direct link to Response")


```
{  
  "status": "success",  
  "messege": "deploying_gpu",  
  "data": "it will take upto 25 minutes.",  
  "training_id": "F5jvdzGnYi"  
}  

```
[PreviousDreambooth Training (V2\)](/docs/train-model/finetune-v2)[NextTraining Status](/docs/train-model/finetune-status)* [Overview](#overview)
* [Request](#request)
* [Body Attributes](#body-attributes)
	+ [Training Types](#training-types)
	+ [Webhook Post JSON](#webhook-post-json)
* [Example](#example)
	+ [Body](#body)
	+ [Request](#request-1)
	+ [Response](#response)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



