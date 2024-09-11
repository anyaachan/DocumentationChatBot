




Train Text to Video Endpoint \| Stable Diffusion API Documentation








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
* Train Text to Video
On this pageTrain Text to Video Endpoint
============================

* [v4/traintexttovideo](/docs/text-to-video/traintexttovideo)
* [v5/text2video](/docs/text-to-video/texttovideo)
Overview[â](#overview "Direct link to Overview")
--------------------------------------------------

This endpoint is used to create video from a text prompt based on trained or on public models.

You can make an API call to your trained models as well as to any public model. 

This endpoint generates and returns a video from a text passed in the request body.

![Text to video endpoint result](/docs/assets/images/db-v4-txt2vid-action-sm-0242dcadd7b6341c8f812468c42b0a62.png)Request[â](#request "Direct link to Request")
-----------------------------------------------


```
--request POST 'https://stablediffusionapi.com/api/v4/dreambooth/text2video' \  

```
Make a `POST` request to <https://stablediffusionapi.com/api/v4/dreambooth/text2video> endpoint and pass the required parameters as a request body. 

Body Attributes[â](#body-attributes "Direct link to Body Attributes")
-----------------------------------------------------------------------



| Parameter | Description |
| --- | --- |
| **key** | Your API Key used for request authorization. |
| **model\_id** | The ID of the model to be used. It can be public or your trained model. |
| **prompt** | Text prompt with description of the things you want in the video to be generated. |
| **negative\_prompt** | Items you don't want in the video. |
| **width** | Max Height: Width: 1024x1024\. |
| **height** | Max Height: Width: 1024x1024\. |
| **scheduler** | Use it to set a [scheduler](#schedulers). |
| **num\_inference\_steps** | Number of denoising steps (minimum: 1; maximum: 50\). |
| **enhance\_prompt** | Enhance prompts for better results; **default**: yes, **options**: yes/no. |
| **guidance\_scale** | Scale for classifier\-free guidance (minimum: 1; maximum: 20\). |
| **strength** | Prompt strength when using **init** image. 1\.0 corresponds to full destruction of information in the init image. |
| **seed** | Seed is used to reproduce results, same seed will give you same result in return again. Pass *null* for a random number. |
| **webhook** | Set an URL to get a POST API call once the video generation is complete. |
| **track\_id** | This ID is returned in the response to the webhook API call. This will be used to identify the webhook request. |

### Schedulers[â](#schedulers "Direct link to Schedulers")

This endpoint also supports schedulers. Use the "scheduler" parameter in the request body to pass a specific scheduler from the list below:

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
  "model_id": "your_model_id",  
  "prompt": "a cat sitting on a bench",  
  "negative_prompt": null,  
  "width": "512",  
  "height": "512",  
  "scheduler": null,  
  "num_inference_steps": "30",  
  "enhance_prompt": "yes",  
  "guidance_scale": 7.5,  
  "strength": 0.7,  
  "seed": null,  
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
  "model_id": "your_model_id",  
  "prompt": "a cat sitting on a bench",  
  "negative_prompt": null,  
  "width": "512",  
  "height": "512",  
  "scheduler": null,  
  "num_inference_steps": "30",  
  "enhance_prompt": "yes",  
  "guidance_scale": 7.5,  
  "strength": 0.7,  
  "seed": null,  
  "webhook": null,  
  "track_id": null  
});  
  
var requestOptions = {  
  method: 'POST',  
  headers: myHeaders,  
  body: raw,  
  redirect: 'follow'  
};  
  
fetch("https://stablediffusionapi.com/api/v4/dreambooth/text2video", requestOptions)  
  .then(response => response.text())  
  .then(result => console.log(result))  
  .catch(error => console.log('error', error));  

```

```
<?php  
  
$payload = [  
  "key" => "",   
  "model_id" => "your_model_id",   
  "prompt" => "a cat sitting on a bench",   
  "negative_prompt" => null,   
  "width" => "512",   
  "height" => "512",   
  "scheduler" => null,   
  "num_inference_steps" => "30",   
  "enhance_prompt" => "yes",   
  "guidance_scale" => 7.5,   
  "strength" => 0.7,   
  "seed" => null,   
  "webhook" => null,   
  "track_id" => null   
];  
  
$curl = curl_init();  
  
curl_setopt_array($curl, array(  
  CURLOPT_URL => 'https://stablediffusionapi.com/api/v4/dreambooth/text2video',  
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
  'url': 'https://stablediffusionapi.com/api/v4/dreambooth/text2video',  
  'headers': {  
    'Content-Type': 'application/json'  
  },  
  body: JSON.stringify({  
    "key": "",  
    "model_id": "your_model_id",  
    "prompt": "a cat sitting on a bench",  
    "negative_prompt": null,  
    "width": "512",  
    "height": "512",  
    "scheduler": null,  
    "num_inference_steps": "30",  
    "enhance_prompt": "yes",  
    "guidance_scale": 7.5,  
    "strength": 0.7,  
    "seed": null,  
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
  
url = "https://stablediffusionapi.com/api/v4/dreambooth/text2video"  
  
payload = json.dumps({  
  "key": "",  
  "model_id": "your_model_id",  
  "prompt": "a cat sitting on a bench",  
  "negative_prompt": None,  
  "width": "512",  
  "height": "512",  
  "scheduler": None,  
  "num_inference_steps": "30",  
  "enhance_prompt": "yes",  
  "guidance_scale": 7.5,  
  "strength": 0.7,  
  "seed": None,  
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
RequestBody body = RequestBody.create(mediaType, "{\n    \"key\": \"\",\n    \"model_id\": \"your_model_id\",\n    \"prompt\": \"a cat sitting on a bench\",\n    \"negative_prompt\": null,\n    \"width\": \"512\",\n    \"height\": \"512\",\n    \"scheduler\": null,\n    \"num_inference_steps\": \"30\",\n    \"enhance_prompt\": \"yes\",\n    \"guidance_scale\": 7.5,\n    \"strength\": 0.7,\n    \"seed\": null,\n    \"webhook\": null,\n    \"track_id\": null\n}");  
Request request = new Request.Builder()  
  .url("https://stablediffusionapi.com/api/v4/dreambooth/text2video")  
  .method("POST", body)  
  .addHeader("Content-Type", "application/json")  
  .build();  
Response response = client.newCall(request).execute();  

```
### Response[â](#response "Direct link to Response")


```
{  
  "status": "processing",  
  "tip": "for faster speed, keep resolution upto 512x512",  
  "eta": 21.880000000000003,  
  "messege": "Try to fetch request after given estimated time",  
  "fetch_result": "https://stablediffusionapi.com/api/v3/dreambooth/fetch/13801718",  
  "id": 13801718,  
  "output": [],  
  "meta": {  
    "prompt": "mdjrny-v4 style a cat sitting on a bench DSLR photography, sharp focus, Unreal Engine 5, Octane Render, Redshift, ((cinematic lighting)), f/1.4, ISO 200, 1/160s, 8K, RAW, unedited, symmetrical balance, in-frame",  
    "model_id": "midjourney",  
    "scheduler": "UniPCMultistepScheduler",  
    "safetychecker": "no",  
    "negative_prompt": " ((out of frame)), ((extra fingers)), mutated hands, ((poorly drawn hands)), ((poorly drawn face)), (((mutation))), (((deformed))), (((tiling))), ((naked)), ((tile)), ((fleshpile)), ((ugly)), (((abstract))), blurry, ((bad anatomy)), ((bad proportions)), ((extra limbs)), cloned face, glitchy, ((extra breasts)), ((double torso)), ((extra arms)), ((extra hands)), ((mangled fingers)), ((missing breasts)), (missing lips), ((ugly face)), ((fat)), ((extra legs))",  
    "W": 512,  
    "H": 512,  
    "guidance_scale": 7.5,  
    "steps": 20,  
    "strength": 0.55,  
    "full_url": "no",  
    "seconds": 5,  
    "multi_lingual": "no",  
    "seed": 3532512439,  
    "outdir": "out",  
    "file_prefix": "d06b5499-eb10-4292-8256-9c269c36199f",  
    "num_frames": 40  
  }  
}  

```
[PreviousCreate Video](/docs/text-to-video/texttovideo)[NextCommunity Models API V4](/docs/category/community-models-api-v4)* [Overview](#overview)
* [Request](#request)
* [Body Attributes](#body-attributes)
	+ [Schedulers](#schedulers)
* [Example](#example)
	+ [Body](#body)
	+ [Request](#request-1)
	+ [Response](#response)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



