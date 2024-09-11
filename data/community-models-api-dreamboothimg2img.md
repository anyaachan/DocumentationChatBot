




Dreambooth Image to Image Endpoint \| Stable Diffusion API Documentation








[Skip to main content](#docusaurus_skipToContent_fallback)[![Stable Diffusion Logo](/docs/img/SD-logo.png)![Stable Diffusion Logo](/docs/img/SD-logo.png)](https://stablediffusionapi.com)[Enterprise](https://stablediffusionapi.com/enterprise)[Pricing](https://stablediffusionapi.com/#pricing)[Blog](https://stablediffusionapi.com/blog)[Docs](https://stablediffusionapi.com/docs)[Playground](https://stablediffusionapi.com/playground)[Models](https://stablediffusionapi.com/models)[API Catalogue](https://stablediffusionapi.com/catalogue)* [Getting Started](/docs/)
* [Stable Diffusion API](/docs/category/stable-diffusion-api)
* [Train Model](/docs/category/train-model)
* [Community Models API](/docs/category/community-models-api)
	+ [API Overview](/docs/community-models-api/overview)
	+ [Text to Image](/docs/community-models-api/dreamboothtext2img)
	+ [Image to Image](/docs/community-models-api/dreamboothimg2img)
	+ [Inpainting](/docs/community-models-api/dreamboothinpainting)
	+ [Fetch Queued Images](/docs/community-models-api/dreamboothfetchqueimg)
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
* [Community Models API](/docs/category/community-models-api)
* Image to Image
On this pageDreambooth Image to Image Endpoint
==================================

* [v3/dreambooth](/docs/community-models-api/dreamboothtext2img)
* [v3/dreambooth/img2img](/docs/community-models-api/dreamboothimg2img)
* [v3/dreambooth/inpaint](/docs/community-models-api/dreamboothinpainting)
* [v3/dreambooth/fetch](/docs/community-models-api/dreamboothfetchqueimg)
Overview[â](#overview "Direct link to Overview")
--------------------------------------------------

Dreambooth Image to Image API is used to generate an image from an image. Pass the appropriate request parameters to the endpoint to generate image from an image.

This endpoint generates and returns an image from an image passed with its URL in the request.

Together with the image you can add your description of the desired result by passing prompt and negative prompt.

![Image to image endpoint result](/docs/assets/images/dream-img2img-action-sm-7434c25b236aa6ed5af4b82e97a6ca31.png)Request[â](#request "Direct link to Request")
-----------------------------------------------


```
--request POST 'https://stablediffusionapi.com/api/v3/dreambooth/img2img' \  

```
Make a `POST` request to <https://stablediffusionapi.com/api/v3/dreambooth/img2img> endpoint and pass the required parameters as a request body to the endpoint. 

Watch the how\-to video to see it in action.

Body Attributes[â](#body-attributes "Direct link to Body Attributes")
-----------------------------------------------------------------------



| Parameter | Description |
| --- | --- |
| **key** | Your API Key used for request authorization |
| **model\_id** | The ID of the model to be used. It can be public or your trained model. |
| **prompt** | Text prompt with description of the things you want in the image to be generated |
| **negative\_prompt** | Items you don't want in the image |
| **init\_image** | Link to the Initial Image |
| **width** | Max Height: Width: 1024x1024 |
| **height** | Max Height: Width: 1024x1024 |
| **samples** | Number of images to be returned in response. The maximum value is 4\. |
| **num\_inference\_steps** | Number of denoising steps (minimum: 1; maximum: 50\) |
| **safety\_checker** | A checker for NSFW images. If such an image is detected, it will be replaced by a blank image. |
| **enhance\_prompt** | Enhance prompts for better results; **default**: yes, **options**: yes/no |
| **guidance\_scale** | Scale for classifier\-free guidance (minimum: 1; maximum: 20\) |
| **strength** | Prompt strength when using **init** image. 1\.0 corresponds to full destruction of information in the init image. |
| **seed** | Seed is used to reproduce results, same seed will give you same image in return again. Pass *null* for a random number. |
| **scheduler** | Use it to set a [scheduler](#schedulers). |
| **webhook** | Set an URL to get a POST API call once the image generation is complete. |
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
  "prompt": "papercraft, quilling, layers, landscape",  
  "negative_prompt": null,  
  "init_image": "https://pub-8b49af329fae499aa563997f5d4068a4.r2.dev/generations/d8cd0add-8cd7-40a4-802b-7b80be45a14c-0.png",  
  "width": "512",  
  "height": "512",  
  "samples": "1",  
  "num_inference_steps": "30",  
  "safety_checker": "yes",  
  "enhance_prompt": "yes",  
  "guidance_scale": 7.5,  
  "strength": 0.7,  
  "scheduler": "UniPCMultistepScheduler",  
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
  "prompt": "papercraft, quilling, layers, landscape",  
  "negative_prompt": null,  
  "init_image": "https://pub-8b49af329fae499aa563997f5d4068a4.r2.dev/generations/d8cd0add-8cd7-40a4-802b-7b80be45a14c-0.png",  
  "width": "512",  
  "height": "512",  
  "samples": "1",  
  "num_inference_steps": "30",  
  "safety_checker": "yes",  
  "enhance_prompt": "yes",  
  "guidance_scale": 7.5,  
  "strength": 0.7,  
  "scheduler": "UniPCMultistepScheduler",  
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
  
fetch("https://stablediffusionapi.com/api/v3/dreambooth/img2img", requestOptions)  
  .then(response => response.text())  
  .then(result => console.log(result))  
  .catch(error => console.log('error', error));  

```

```
<?php  
  
$payload = [  
   "key" => "",   
   "model_id" => "your_model_id",   
   "prompt" => "papercraft, quilling, layers, landscape",   
   "negative_prompt" => null,   
   "init_image" => "https://pub-8b49af329fae499aa563997f5d4068a4.r2.dev/generations/d8cd0add-8cd7-40a4-802b-7b80be45a14c-0.png",   
   "width" => "512",   
   "height" => "512",   
   "samples" => "1",   
   "num_inference_steps" => "30",   
   "safety_checker" => "yes",   
   "enhance_prompt" => "yes",   
   "guidance_scale" => 7.5,   
   "strength" => 0.7,   
   "scheduler" => "UniPCMultistepScheduler",  
   "seed" => null,   
   "webhook" => null,   
   "track_id" => null   
];  
  
$curl = curl_init();  
  
curl_setopt_array($curl, array(  
  CURLOPT_URL => 'https://stablediffusionapi.com/api/v3/dreambooth/img2img',  
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
  'url': 'https://stablediffusionapi.com/api/v3/dreambooth/img2img',  
  'headers': {  
    'Content-Type': 'application/json'  
  },  
  body: JSON.stringify({  
    "key": "",  
    "model_id": "your_model_id",  
    "prompt": "papercraft, quilling, layers, landscape",  
    "negative_prompt": null,  
    "init_image": "https://pub-8b49af329fae499aa563997f5d4068a4.r2.dev/generations/d8cd0add-8cd7-40a4-802b-7b80be45a14c-0.png",  
    "width": "512",  
    "height": "512",  
    "samples": "1",  
    "num_inference_steps": "30",  
    "safety_checker": "yes",  
    "enhance_prompt": "yes",  
    "guidance_scale": 7.5,  
    "strength": 0.7,  
    "scheduler": "UniPCMultistepScheduler",  
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
  
url = "https://stablediffusionapi.com/api/v3/dreambooth/img2img"  
  
payload = json.dumps({  
  "key": "",  
  "model_id": "your_model_id",  
  "prompt": "papercraft, quilling, layers, landscape",  
  "negative_prompt": None,  
  "init_image": "https://pub-8b49af329fae499aa563997f5d4068a4.r2.dev/generations/d8cd0add-8cd7-40a4-802b-7b80be45a14c-0.png",  
  "width": "512",  
  "height": "512",  
  "samples": "1",  
  "num_inference_steps": "30",  
  "safety_checker": "yes",  
  "enhance_prompt": "yes",  
  "guidance_scale": 7.5,  
  "strength": 0.7,  
  "scheduler": "UniPCMultistepScheduler",  
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
RequestBody body = RequestBody.create(mediaType, "{\n    \"key\": \"\",\n   \"model_id\": \"your_model_id\",\n   \"prompt\": \"papercraft, quilling, layers, landscape\",\n    \"negative_prompt\": null,\n    \"init_image\": \"https://pub-8b49af329fae499aa563997f5d4068a4.r2.dev/generations/d8cd0add-8cd7-40a4-802b-7b80be45a14c-0.png\",\n    \"width\": \"512\",\n    \"height\": \"512\",\n    \"samples\": \"1\",\n    \"num_inference_steps\": \"30\",\n    \"safety_checker\": \"yes\",\n    \"enhance_prompt\": \"yes\",\n    \"guidance_scale\": 7.5,\n    \"strength\": 0.7,\n   \"scheduler\":\"UniPCMultistepScheduler\",\n   \"seed\": null,\n    \"webhook\": null,\n    \"track_id\": null\n}");  
Request request = new Request.Builder()  
  .url("https://stablediffusionapi.com/api/v3/dreambooth/img2img")  
  .method("POST", body)  
  .addHeader("Content-Type", "application/json")  
  .build();  
Response response = client.newCall(request).execute();  

```
### Response[â](#response "Direct link to Response")


```
{  
  "status": "success",  
  "generationTime": 2.5262653827667236,  
  "id": 12631244,  
  "output": [  
    "https://pub-8b49af329fae499aa563997f5d4068a4.r2.dev/generations/799898a5-9888-4e8a-bd05-4dcfcb690aac-0.png"  
  ],  
  "meta": {  
    "H": 512,  
    "W": 512,  
    "file_prefix": "799898a5-9888-4e8a-bd05-4dcfcb690aac",  
    "full_url": "no",  
    "guidance_scale": 7.5,  
    "init_image": "https://pub-8b49af329fae499aa563997f5d4068a4.r2.dev/generations/d8cd0add-8cd7-40a4-802b-7b80be45a14c-0.png",  
    "model_id": "midjourney-papercut",  
    "n_samples": 1,  
    "negative_prompt": " ((out of frame)), ((extra fingers)), mutated hands, ((poorly drawn hands)), ((poorly drawn face)), (((mutation))), (((deformed))), (((tiling))), ((naked)), ((tile)), ((fleshpile)), ((ugly)), (((abstract))), blurry, ((bad anatomy)), ((bad proportions)), ((extra limbs)), cloned face, glitchy, ((extra breasts)), ((double torso)), ((extra arms)), ((extra hands)), ((mangled fingers)), ((missing breasts)), (missing lips), ((ugly face)), ((fat)), ((extra legs))",  
    "outdir": "out",  
    "prompt": "mdjrny-pprct papercraft, quilling, layers, landscape DSLR photography, sharp focus, Unreal Engine 5, Octane Render, Redshift, ((cinematic lighting)), f/1.4, ISO 200, 1/160s, 8K, RAW, unedited, symmetrical balance, in-frame",  
    "safetychecker": "yes",  
    "scheduler": "UniPCMultistepScheduler",  
    "seed": 1591256096,  
    "steps": 20,  
    "strength": 0.7,  
    "upscale": "no"  
  }  
}  

```
[PreviousText to Image](/docs/community-models-api/dreamboothtext2img)[NextInpainting](/docs/community-models-api/dreamboothinpainting)* [Overview](#overview)
* [Request](#request)
* [Body Attributes](#body-attributes)
	+ [Schedulers](#schedulers)
* [Example](#example)
	+ [Body](#body)
	+ [Request](#request-1)
	+ [Response](#response)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



