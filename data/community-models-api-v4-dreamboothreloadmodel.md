




Dreambooth V4 Reload Model Endpoint \| Stable Diffusion API Documentation








[Skip to main content](#docusaurus_skipToContent_fallback)[![Stable Diffusion Logo](/docs/img/SD-logo.png)![Stable Diffusion Logo](/docs/img/SD-logo.png)](https://stablediffusionapi.com)[Enterprise](https://stablediffusionapi.com/enterprise)[Pricing](https://stablediffusionapi.com/#pricing)[Blog](https://stablediffusionapi.com/blog)[Docs](https://stablediffusionapi.com/docs)[Playground](https://stablediffusionapi.com/playground)[Models](https://stablediffusionapi.com/models)[API Catalogue](https://stablediffusionapi.com/catalogue)* [Getting Started](/docs/)
* [Stable Diffusion API](/docs/category/stable-diffusion-api)
* [Train Model](/docs/category/train-model)
* [Community Models API](/docs/category/community-models-api)
* [Text To Video](/docs/category/text-to-video)
* [Community Models API V4](/docs/category/community-models-api-v4)
	+ [API Overview](/docs/community-models-api-v4/overview)
	+ [Text to Image](/docs/community-models-api-v4/dreamboothtext2img)
	+ [LoRA](/docs/community-models-api-v4/dreamboothlora)
	+ [LoRA Multi](/docs/community-models-api-v4/dreamboothloramulti)
	+ [Image to Image](/docs/community-models-api-v4/dreamboothimg2img)
	+ [Inpainting](/docs/community-models-api-v4/dreamboothinpainting)
	+ [Fetch Queued Images](/docs/community-models-api-v4/dreamboothfetchqueimg)
	+ [Reload Model](/docs/community-models-api-v4/dreamboothreloadmodel)
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
* [Community Models API V4](/docs/category/community-models-api-v4)
* Reload Model
On this pageDreambooth V4 Reload Model Endpoint
===================================

* [v4/dreambooth](/docs/community-models-api-v4/dreamboothtext2img)
* [v4/dreambooth/img2img](/docs/community-models-api-v4/dreamboothimg2img)
* [v4/dreambooth/inpaint](/docs/community-models-api-v4/dreamboothinpainting)
* [v4/dreambooth/fetch](/docs/community-models-api-v4/dreamboothfetchqueimg)
* [v4/dreambooth/model\_reload](/docs/community-models-api-v4/dreamboothreloadmodel)
Overview[â](#overview "Direct link to Overview")
--------------------------------------------------

The Dreambooth Reload Model API is used to reload an idle model that has not been used for more than 7 days. 

After 7 days of inactivity a model will be deleted from the inference server.

To reload a model and start using it again, you can make an API call to the Reload Model endpoint. 

cautionIt will take **2 minutes** to reload a model.

Request[â](#request "Direct link to Request")
-----------------------------------------------


```
--request POST 'https://stablediffusionapi.com/api/v4/dreambooth/model_reload' \  

```
Send a `POST` request to <https://stablediffusionapi.com/api/v4/dreambooth/model_reload> endpoint to reload a specific model specified by the **model\_id** parameter in the request body.

Attributes[â](#attributes "Direct link to Attributes")
--------------------------------------------------------



| Parameter | Description |
| --- | --- |
| **key** | Your API Key used for request authorization |
| **model\_id** | The ID of the model to be reloaded. |

Example[â](#example "Direct link to Example")
-----------------------------------------------

### Body[â](#body "Direct link to Body")

Body Raw
```
{  
 "key": "",  
 "model_id": "model_id"  
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
 "model_id": "model_id"  
});  
  
var requestOptions = {  
  method: 'POST',  
  headers: myHeaders,  
  body: raw,  
  redirect: 'follow'  
};  
  
model_reload("https://stablediffusionapi.com/api/v4/dreambooth/model_reload", requestOptions)  
  .then(response => response.text())  
  .then(result => console.log(result))  
  .catch(error => console.log('error', error));  

```

```
<?php  
  
$payload = [  
  "key" => "",  
  "model_id" => "model_id"  
];  
  
$curl = curl_init();  
  
curl_setopt_array($curl, array(  
  CURLOPT_URL => 'https://stablediffusionapi.com/api/v4/dreambooth/model_reload',  
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
  'url': 'https://stablediffusionapi.com/api/v4/dreambooth/model_reload',  
  'headers': {  
    'Content-Type': 'application/json'  
  },  
  body: JSON.stringify({  
    "key": "",  
    "model_id": "model_id"  
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
  
url = "https://stablediffusionapi.com/api/v4/dreambooth/model_reload"  
  
payload = json.dumps({  
 "key": "",  
 "model_id": "model_id"  
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
RequestBody body = RequestBody.create(mediaType, "{\n  \"key\": \"\",\n  \"model_id\": \"model_id\"\n}");  
Request request = new Request.Builder()  
  .url("https://stablediffusionapi.com/api/v4/dreambooth/model_reload")  
  .method("POST", body)  
  .addHeader("Content-Type", "application/json")  
  .build();  
Response response = client.newCall(request).execute();  

```
[PreviousFetch Queued Images](/docs/community-models-api-v4/dreamboothfetchqueimg)[NextMISCS](/docs/category/miscs)* [Overview](#overview)
* [Request](#request)
* [Attributes](#attributes)
* [Example](#example)
	+ [Body](#body)
	+ [Request](#request-1)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



