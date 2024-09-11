




Dreambooth V4 Image to Image Endpoint \| Stable Diffusion API Documentation








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
* Image to Image
On this pageDreambooth V4 Image to Image Endpoint
=====================================

* [v4/dreambooth](/docs/community-models-api-v4/dreamboothtext2img)
* [v4/dreambooth/img2img](/docs/community-models-api-v4/dreamboothimg2img)
* [v4/dreambooth/inpaint](/docs/community-models-api-v4/dreamboothinpainting)
* [v4/dreambooth/fetch](/docs/community-models-api-v4/dreamboothfetchqueimg)
* [v4/dreambooth/model\_reload](/docs/community-models-api-v4/dreamboothreloadmodel)
Overview[â](#overview "Direct link to Overview")
--------------------------------------------------

Dreambooth Image to Image API is used to generate an image from an image based on trained or on public models. Pass the appropriate request parameters to the endpoint to generate image from an image.

This endpoint generates and returns an image from an image passed with its URL in the request.

Together with the image you can add your description of the desired result by passing prompt and negative prompt.

![Image to image endpoint result](/docs/assets/images/db-v4-img2img-action-sm-422bfe4e9d993856418842c5a58eb134.png)Request[â](#request "Direct link to Request")
-----------------------------------------------


```
--request POST 'https://stablediffusionapi.com/api/v4/dreambooth/img2img' \  

```
Make a `POST` request to <https://stablediffusionapi.com/api/v4/dreambooth/img2img> endpoint and pass the required parameters as a request body to the endpoint. 

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
| **safety\_checker\_type** | Modify image if NSFW images are found; **default**: sensitive\_content\_text, **options**: blur/sensitive\_content\_text/pixelate/black |
| **enhance\_prompt** | Enhance prompts for better results; **default**: yes, **options**: yes/no |
| **guidance\_scale** | Scale for classifier\-free guidance (minimum: 1; maximum: 20\) |
| **tomesd** | Enable tomesd to generate images: gives really fast results, **default**: yes, **options**: yes/no |
| **use\_karras\_sigmas** | Use keras sigmas to generate images. gives nice results, **default**: yes, **options**: yes/no |
| **algorithm\_type** | Used in DPMSolverMultistepScheduler scheduler, **default**: none, **options**: dpmsolver\+\+\+ |
| **vae** | use custom vae in generating images **default**: null |
| **lora\_strength** | Strength of lora model you are using. If using multi lora, pass each values as comma saparated |
| **lora\_model** | multi lora is supported, pass comma saparated values . Example contrast\-fix,yae\-miko\-genshin |
| **strength** | Prompt strength when using **init** image. 1\.0 corresponds to full destruction of information in the init image. |
| **seed** | Seed is used to reproduce results, same seed will give you same image in return again. Pass *null* for a random number. |
| **scheduler** | Use it to set a [scheduler](#schedulers). |
| **webhook** | Set an URL to get a POST API call once the image generation is complete. |
| **track\_id** | This ID is returned in the response to the webhook API call. This will be used to identify the webhook request. |
| **clip\_skip** | Clip Skip (minimum: 1; maximum: 8\) |
| **base64** | Get response as base64 string, pass init\_image as base64 string, to get base64 response. **default**: "no", **options**: yes/no |
| **temp** | Create temp image link. This link is valid for 24 hours. **temp**: yes, **options**: yes/no |

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
  "lora_model": null,  
  "tomesd": "yes",  
  "use_karras_sigmas": "yes",  
  "vae": null,  
  "lora_strength": null,  
  "embeddings_model": null,  
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
  "lora_model": null,  
  "tomesd": "yes",  
  "use_karras_sigmas": "yes",  
  "vae": null,  
  "lora_strength": null,  
  "embeddings_model": null,  
  "webhook": null,  
  "track_id": null  
});  
  
var requestOptions = {  
  method: 'POST',  
  headers: myHeaders,  
  body: raw,  
  redirect: 'follow'  
};  
  
fetch("https://stablediffusionapi.com/api/v4/dreambooth/img2img", requestOptions)  
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
   "lora_model" => null,  
   "tomesd" => "yes",  
   "use_karras_sigmas" => "yes",  
   "vae" => null,  
   "lora_strength" => null,  
   "embeddings_model" => null,  
   "webhook" => null,   
   "track_id" => null   
];  
  
$curl = curl_init();  
  
curl_setopt_array($curl, array(  
  CURLOPT_URL => 'https://stablediffusionapi.com/api/v4/dreambooth/img2img',  
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
  'url': 'https://stablediffusionapi.com/api/v4/dreambooth/img2img',  
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
    "lora_model": null,  
    "tomesd": "yes",  
    "use_karras_sigmas": "yes",  
    "vae": null,  
    "lora_strength": null,  
    "embeddings_model": null,  
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
  
url = "https://stablediffusionapi.com/api/v4/dreambooth/img2img"  
  
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
  "lora_model": None,  
  "tomesd": "yes",  
  "use_karras_sigmas": "yes",  
  "vae": None,  
  "lora_strength": None,  
  "embeddings_model": None,  
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
RequestBody body = RequestBody.create(mediaType, "{\n    \"key\": \"\",\n  \"model_id\": \"your_model_id\",\n  \"prompt\": \"papercraft, quilling, layers, landscape\",\n  \"negative_prompt\": null,\n  \"init_image\": \"https://pub-8b49af329fae499aa563997f5d4068a4.r2.dev/generations/d8cd0add-8cd7-40a4-802b-7b80be45a14c-0.png\",\n  \"width\": \"512\",\n  \"height\": \"512\",\n  \"samples\": \"1\",\n  \"num_inference_steps\": \"30\",\n  \"safety_checker\": \"yes\",\n  \"enhance_prompt\": \"yes\",\n  \"guidance_scale\": 7.5,\n  \"strength\": 0.7,\n  \"scheduler\": \"UniPCMultistepScheduler\",\n  \"seed\": null,\n  \"lora_model\": \"lora_model_id\",\n  \"tomesd\": \"yes\",\n  \"use_karras_sigmas\": \"yes\",\n  \"vae\": null,\n  \"lora_strength\": null,\n  \"embeddings_model\": null,\n  \"webhook\": null,\n  \"track_id\": null\n}");  
Request request = new Request.Builder()  
  .url("https://stablediffusionapi.com/api/v4/dreambooth/img2img")  
  .method("POST", body)  
  .addHeader("Content-Type", "application/json")  
  .build();  
Response response = client.newCall(request).execute();  
  

```
### Response[â](#response "Direct link to Response")


```
{  
  "status": "success",  
  "generationTime": 11.025346279144287,  
  "id": 13443927,  
  "output": [  
    "https://pub-8b49af329fae499aa563997f5d4068a4.r2.dev/generations/6ef3f81f-14e1-4835-b07a-e00dbe80b6ff-0.png"  
  ],  
  "meta": {  
    "prompt": " papercraft, quilling, layers, landscape DSLR photography, sharp focus, Unreal Engine 5, Octane Render, Redshift, ((cinematic lighting)), f/1.4, ISO 200, 1/160s, 8K, RAW, unedited, symmetrical balance, in-frame",  
    "model_id": "midjourney-v4-painta",  
    "scheduler": "UniPCMultistepScheduler",  
    "safetychecker": "yes",  
    "negative_prompt": " ((out of frame)), ((extra fingers)), mutated hands, ((poorly drawn hands)), ((poorly drawn face)), (((mutation))), (((deformed))), (((tiling))), ((naked)), ((tile)), ((fleshpile)), ((ugly)), (((abstract))), blurry, ((bad anatomy)), ((bad proportions)), ((extra limbs)), cloned face, glitchy, ((extra breasts)), ((double torso)), ((extra arms)), ((extra hands)), ((mangled fingers)), ((missing breasts)), (missing lips), ((ugly face)), ((fat)), ((extra legs))",  
    "W": 512,  
    "H": 512,  
    "guidance_scale": 7.5,  
    "init_image": "https://pub-8b49af329fae499aa563997f5d4068a4.r2.dev/generations/4118bb93-2c49-4d1d-9837-f43a0801e42e-0.png",  
    "steps": 20,  
    "n_samples": 1,  
    "strength": 0.7,  
    "multi_lingual": "no",  
    "full_url": "no",  
    "upscale": "no",  
    "seed": 2916174600,  
    "outdir": "out",  
    "file_prefix": "6ef3f81f-14e1-4835-b07a-e00dbe80b6ff"  
  }  
}  

```
[PreviousLoRA Multi](/docs/community-models-api-v4/dreamboothloramulti)[NextInpainting](/docs/community-models-api-v4/dreamboothinpainting)* [Overview](#overview)
* [Request](#request)
* [Body Attributes](#body-attributes)
	+ [Schedulers](#schedulers)
* [Example](#example)
	+ [Body](#body)
	+ [Request](#request-1)
	+ [Response](#response)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



