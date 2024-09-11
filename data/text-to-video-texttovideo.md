




Text to Video Endpoint \| Stable Diffusion API Documentation








[Skip to main content](#docusaurus_skipToContent_fallback)[![Stable Diffusion Logo](/docs/img/SD-logo.png)![Stable Diffusion Logo](/docs/img/SD-logo.png)](https://stablediffusionapi.com)[Enterprise](https://stablediffusionapi.com/enterprise)[Pricing](https://stablediffusionapi.com/#pricing)[Blog](https://stablediffusionapi.com/blog)[Docs](https://stablediffusionapi.com/docs)[Playground](https://stablediffusionapi.com/playground)[Models](https://stablediffusionapi.com/models)[API Catalogue](https://stablediffusionapi.com/catalogue)* [Getting Started](/docs/)
* [Stable Diffusion API](/docs/category/stable-diffusion-api)
* [Train Model](/docs/category/train-model)
* [Community Models API](/docs/category/community-models-api)
* [Text To Video](/docs/category/text-to-video)
	+ [API Overview](/docs/text-to-video/overview)
	+ [Create Video](/docs/text-to-video/texttovideo)
	+ [Train Text to Video](/docs/text-to-video/traintexttovideo)
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
* [Text To Video](/docs/category/text-to-video)
* Create Video
On this pageText to Video Endpoint
======================

* [v4/traintexttovideo](/docs/text-to-video/traintexttovideo)
* [v5/text2video](/docs/text-to-video/texttovideo)
Overview[â](#overview "Direct link to Overview")
--------------------------------------------------

Text to Video endpoint generates and returns a video based on a text description.

![Text to video endpoint result](/docs/assets/images/v5-txt2vid-action-sm-15e0b41c9d54bedfe1c6a9238f7349cc.png)Request[â](#request "Direct link to Request")
-----------------------------------------------


```
--request POST 'https://stablediffusionapi.com/api/v5/text2video' \  

```
Make a `POST` request to <https://stablediffusionapi.com/api/v5/text2video> endpoint and pass the required parameters in the request body. 

Body Attributes[â](#body-attributes "Direct link to Body Attributes")
-----------------------------------------------------------------------



| Parameter | Description |
| --- | --- |
| **key** | Your API Key used for request authorization. |
| **prompt** | Text prompt with description of the things you want in the video to be generated. |
| **negative\_prompt** | Items you don't want in the video. |
| **scheduler** | Use it to set a [scheduler](#schedulers) for video creation. |
| **seconds** | Duration of the video in seconds. |

### Schedulers[â](#schedulers "Direct link to Schedulers")

This endpoint also supports schedulers. Use the "scheduler" parameter in the request body to set a specific scheduler to be used from the list below:

* DDPMScheduler
* DDIMScheduler
* PNDMScheduler
* LMSDiscreteScheduler
* EulerDiscreteScheduler
* EulerAncestralDiscreteScheduler
* DPMSolverMultistepScheduler
* HeunDiscreteScheduler
* KDPM2DiscreteScheduler
* DPMSolverSinglestepScheduler
* KDPM2AncestralDiscreteScheduler
* UniPCMultistepScheduler
* DDIMInverseScheduler
* DEISMultistepScheduler
* IPNDMScheduler
* KarrasVeScheduler
* ScoreSdeVeScheduler
* LCMScheduler

Example[â](#example "Direct link to Example")
-----------------------------------------------

### Body[â](#body "Direct link to Body")

Body
```
{  
  "key": "",  
  "prompt": "man walking on the road, ultra HD video",  
  "negative_prompt": "Low Quality",  
  "scheduler": "UniPCMultistepScheduler",  
  "seconds": 3  
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
  "prompt": "man walking on the road, ultra HD video",  
  "negative_prompt": "Low Quality",  
  "scheduler": "UniPCMultistepScheduler",  
  "seconds": 3  
});  
  
var requestOptions = {  
  method: 'POST',  
  headers: myHeaders,  
  body: raw,  
  redirect: 'follow'  
};  
  
fetch("https://stablediffusionapi.com/api/v5/text2video", requestOptions)  
  .then(response => response.text())  
  .then(result => console.log(result))  
  .catch(error => console.log('error', error));  

```

```
<?php  
  
$payload = [  
  "key" => "",   
  "prompt" => "man walking on the road, ultra HD video",   
  "negative_prompt" => "Low Quality",   
  "scheduler" => "UniPCMultistepScheduler",   
  "seconds" => 3   
];  
  
$curl = curl_init();  
  
curl_setopt_array($curl, array(  
  CURLOPT_URL => 'https://stablediffusionapi.com/api/v5/text2video',  
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
  'url': 'https://stablediffusionapi.com/api/v5/text2video',  
  'headers': {  
    'Content-Type': 'application/json'  
  },  
  body: JSON.stringify({  
    "key": "",  
    "prompt": "man walking on the road, ultra HD video",  
    "negative_prompt": "Low Quality",  
    "scheduler": "UniPCMultistepScheduler",  
    "seconds": 3  
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
  
url = "https://stablediffusionapi.com/api/v5/text2video"  
  
payload = json.dumps({  
  "key": "",  
  "prompt": "man walking on the road, ultra HD video",  
  "negative_prompt": "Low Quality",  
  "scheduler": "UniPCMultistepScheduler",  
  "seconds": 3  
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
RequestBody body = RequestBody.create(mediaType, "{\n   \"key\": \"\",\n   \"prompt\" : \"man walking on the road, ultra HD video\",\n   \"negative_prompt\" : \"Low Quality\",\n   \"scheduler\" : \"UniPCMultistepScheduler\",\n   \"seconds\" : 3\n}");  
Request request = new Request.Builder()  
  .url("https://stablediffusionapi.com/api/v5/text2video")  
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
  "generationTime": 9.029465913772583,  
  "id": 14758180,  
  "output": [  
    "https://pub-8b49af329fae499aa563997f5d4068a4.r2.dev/generations/ee3e20f4-adf7-4cb2-9733-3c3b6bae8813.mp4"  
  ]  
}  

```
[PreviousAPI Overview](/docs/text-to-video/overview)[NextTrain Text to Video](/docs/text-to-video/traintexttovideo)* [Overview](#overview)
* [Request](#request)
* [Body Attributes](#body-attributes)
	+ [Schedulers](#schedulers)
* [Example](#example)
	+ [Body](#body)
	+ [Request](#request-1)
	+ [Response](#response)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



