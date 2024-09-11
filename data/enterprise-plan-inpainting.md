




Enterprise: Inpainting Endpoint \| Stable Diffusion API Documentation








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
* Inpainting
On this pageEnterprise: Inpainting Endpoint
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

Enterprise Inpainting endpoint is used to change (inpaint) some part of an image according to specific requirements, based on trained or on public models. Pass the appropriate request parameters to the endpoint.

You can also add your description of the desired result by passing prompt and negative prompt.

![Inpainting endpoint result](/docs/assets/images/db-v4-inpaint-action-sm-98d162609bb06ddbedc37295c8f474a3.png)Request[â](#request "Direct link to Request")
-----------------------------------------------


```
--request POST 'https://stablediffusionapi.com/api/v1/enterprise/inpaint' \  

```
Make a `POST` request to <https://stablediffusionapi.com/api/v1/enterprise/inpaint> endpoint and pass the required parameters as a request body. 

Watch the how\-to video to see it in action.

Attributes[â](#attributes "Direct link to Attributes")
--------------------------------------------------------



| Parameter | Description |
| --- | --- |
| **key** | Your enterprise API Key used for request authorization |
| **model\_id** | The ID of the model to be used. It can be public or your trained model. |
| **prompt** | Text prompt with description of the things you want in the image to be generated |
| **negative\_prompt** | Items you don't want in the image |
| **init\_image** | Link to the Initial Image |
| **mask\_image** | Link to the mask image for inpainting |
| **width** | Max Height: Width: 1024x1024 |
| **height** | Max Height: Width: 1024x1024 |
| **samples** | Number of images to be returned in response. The maximum value is 4\. |
| **num\_inference\_steps** | Number of denoising steps (minimum: 1; maximum: 50\) |
| **safety\_checker** | A checker for NSFW images. If such an image is detected, it will be replaced by a blank image. |
| **safety\_checker\_type** | Modify image if NSFW images are found; **default**: sensitive\_content\_text, **options**: blur/sensitive\_content\_text/pixelate/black |
| **enhance\_prompt** | Enhance prompts for better results; **default**: yes, **options**: yes/no |
| **guidance\_scale** | Scale for classifier\-free guidance (minimum: 1; maximum: 20\) |
| **strength** | Prompt strength when using **init** image. 1\.0 corresponds to full destruction of information in the init image. |
| **tomesd** | Enable tomesd to generate images: gives really fast results, **default**: yes, **options**: yes/no |
| **use\_karras\_sigmas** | Use keras sigmas to generate images. gives nice results, **default**: yes, **options**: yes/no |
| **algorithm\_type** | Used in DPMSolverMultistepScheduler scheduler, **default**: none, **options**: dpmsolver\+\+\+ |
| **vae** | use custom vae in generating images **default**: null |
| **lora\_strength** | Strength of lora model you are using. If using multi lora, pass each values as comma saparated |
| **lora\_model** | multi lora is supported, pass comma saparated values . Example contrast\-fix,yae\-miko\-genshin |
| **scheduler** | Use it to set a [scheduler](#schedulers). |
| **seed** | Seed is used to reproduce results, same seed will give you same image in return again. Pass *null* for a random number. |
| **webhook** | Set an URL to get a POST API call once the image generation is complete. |
| **track\_id** | This ID is returned in the response to the webhook API call. This will be used to identify the webhook request. |
| **loadbalancer** | Enable load balancer; **options**: yes/no, **default**: no. |
| **clip\_skip** | Clip Skip (minimum: 1; maximum: 8\) |
| **base64** | Get response as base64 string, pass init\_image, mask\_image as base64 string, to get base64 response. **default**: "no", **options**: yes/no |
| **temp** | Create temp image link. This link is valid for 24 hours. **temp**: yes, **options**: yes/no |

infoTo use the **load balancer**, you need to have **more than 1 server**. Pass the first server's API key, and it will handle the load balancing with the other servers.

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

Body Raw
```
{  
  "key": "enterprise_api_key",  
  "model_id": "your_model_id",  
  "prompt": "a cat sitting on a bench",  
  "negative_prompt": null,  
  "init_image": "https://raw.githubusercontent.com/CompVis/stable-diffusion/main/data/inpainting_examples/overture-creations-5sI6fQgYIuo.png",  
  "mask_image": "https://raw.githubusercontent.com/CompVis/stable-diffusion/main/data/inpainting_examples/overture-creations-5sI6fQgYIuo_mask.png",  
  "width": "512",  
  "height": "512",  
  "samples": "1",  
  "num_inference_steps": "30",  
  "safety_checker": "no",  
  "enhance_prompt": "yes",  
  "guidance_scale": 7.5,  
  "strength": 0.7,  
  "scheduler": "PNDMScheduler",  
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
  "prompt": "a cat sitting on a bench",  
  "negative_prompt": null,  
  "init_image": "https://raw.githubusercontent.com/CompVis/stable-diffusion/main/data/inpainting_examples/overture-creations-5sI6fQgYIuo.png",  
  "mask_image": "https://raw.githubusercontent.com/CompVis/stable-diffusion/main/data/inpainting_examples/overture-creations-5sI6fQgYIuo_mask.png",  
  "width": "512",  
  "height": "512",  
  "samples": "1",  
  "steps": "30",  
  "safety_checker": "no",  
  "enhance_prompt": "yes",  
  "guidance_scale": 7.5,  
  "strength": 0.7,  
  "scheduler": "PNDMScheduler",  
  "lora_model": null,  
  "tomesd": "yes",  
  "use_karras_sigmas": "yes",  
  "vae": null,  
  "lora_strength": null,  
  "embeddings_model": null,  
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
  
fetch("https://stablediffusionapi.com/api/v1/enterprise/inpaint", requestOptions)  
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
  "init_image" => "https://raw.githubusercontent.com/CompVis/stable-diffusion/main/data/inpainting_examples/overture-creations-5sI6fQgYIuo.png",   
  "mask_image" => "https://raw.githubusercontent.com/CompVis/stable-diffusion/main/data/inpainting_examples/overture-creations-5sI6fQgYIuo_mask.png",   
  "width" => "512",   
  "height" => "512",   
  "samples" => "1",   
  "steps" => "30",   
  "safety_checker" => "no",   
  "enhance_prompt" => "yes",   
  "guidance_scale" => 7.5,   
  "strength" => 0.7,   
  "scheduler" => "PNDMScheduler",  
  "lora_model" => null,  
  "tomesd" => "yes",  
  "use_karras_sigmas" => "yes",  
  "vae" => null,  
  "lora_strength" => null,  
  "embeddings_model" => null,  
  "seed" => null,   
  "webhook" => null,   
  "track_id" => null   
];  
  
$curl = curl_init();  
  
curl_setopt_array($curl, array(  
  CURLOPT_URL => 'https://stablediffusionapi.com/api/v1/enterprise/inpaint',  
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
  'url': 'https://stablediffusionapi.com/api/v1/enterprise/inpaint',  
  'headers': {  
    'Content-Type': 'application/json'  
  },  
  body: JSON.stringify({  
    "key": "",  
    "model_id": "your_model_id",  
    "prompt": "a cat sitting on a bench",  
    "negative_prompt": null,  
    "init_image": "https://raw.githubusercontent.com/CompVis/stable-diffusion/main/data/inpainting_examples/overture-creations-5sI6fQgYIuo.png",  
    "mask_image": "https://raw.githubusercontent.com/CompVis/stable-diffusion/main/data/inpainting_examples/overture-creations-5sI6fQgYIuo_mask.png",  
    "width": "512",  
    "height": "512",  
    "samples": "1",  
    "steps": "30",  
    "safety_checker": "no",  
    "enhance_prompt": "yes",  
    "guidance_scale": 7.5,  
    "strength": 0.7,  
    "scheduler": "PNDMScheduler",  
    "lora_model": null,  
    "tomesd": "yes",  
    "use_karras_sigmas": "yes",  
    "vae": null,  
    "lora_strength": null,  
    "embeddings_model": null,  
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
  
url = "https://stablediffusionapi.com/api/v1/enterprise/inpaint"  
  
payload = json.dumps({  
  "key": "",  
  "prompt": "a cat sitting on a bench",  
  "negative_prompt": None,  
  "init_image": "https://raw.githubusercontent.com/CompVis/stable-diffusion/main/data/inpainting_examples/overture-creations-5sI6fQgYIuo.png",  
  "mask_image": "https://raw.githubusercontent.com/CompVis/stable-diffusion/main/data/inpainting_examples/overture-creations-5sI6fQgYIuo_mask.png",  
  "width": "512",  
  "height": "512",  
  "samples": "1",  
  "steps": "30",  
  "safety_checker": "no",  
  "enhance_prompt": "yes",  
  "guidance_scale": 7.5,  
  "strength": 0.7,  
  "scheduler": "PNDMScheduler",  
   "lora_model": null,  
  "tomesd": "yes",  
  "use_karras_sigmas": "yes",  
  "vae": None,  
  "lora_strength": None,  
  "embeddings_model": None,  
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
RequestBody body = RequestBody.create(mediaType, "{\n     \"key\": \"\",\n  \"model_id\": \"your_model_id\",\n  \"prompt\": \"a cat sitting on a bench\",\n  \"negative_prompt\": null,\n  \"init_image\": \"https://raw.githubusercontent.com/CompVis/stable-diffusion/main/data/inpainting_examples/overture-creations-5sI6fQgYIuo.png\",\n  \"mask_image\": \"https://raw.githubusercontent.com/CompVis/stable-diffusion/main/data/inpainting_examples/overture-creations-5sI6fQgYIuo_mask.png\",\n  \"width\": \"512\",\n  \"height\": \"512\",\n  \"samples\": \"1\",\n  \"num_inference_steps\": \"30\",\n  \"safety_checker\": \"no\",\n  \"enhance_prompt\": \"yes\",\n  \"guidance_scale\": 7.5,\n  \"strength\": 0.7,\n  \"scheduler\": \"PNDMScheduler\",\n  \"seed\": null,\n  \"lora_model\": \"lora_model_id\",\n  \"tomesd\": \"yes\",\n  \"use_karras_sigmas\": \"yes\",\n  \"vae\": null,\n  \"lora_strength\": null,\n  \"embeddings_model\": null,\n  \"webhook\": null,\n  \"track_id\": null\n}");  
Request request = new Request.Builder()  
  .url("https://stablediffusionapi.com/api/v1/enterprise/inpaint")  
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
  "generationTime": 20.970642805099487,  
  "id": 13446970,  
  "output": [  
    "https://pub-8b49af329fae499aa563997f5d4068a4.r2.dev/generations/dc639bd6-d605-42c7-950e-48c531124d0d-0.png"  
  ],  
  "meta": {  
    "prompt": " a cat sitting on a bench DSLR photography, sharp focus, Unreal Engine 5, Octane Render, Redshift, ((cinematic lighting)), f/1.4, ISO 200, 1/160s, 8K, RAW, unedited, symmetrical balance, in-frame",  
    "model_id": "midjourney-v4-painta",  
    "scheduler": "PNDMScheduler",  
    "safetychecker": "no",  
    "negative_prompt": " ((out of frame)), ((extra fingers)), mutated hands, ((poorly drawn hands)), ((poorly drawn face)), (((mutation))), (((deformed))), (((tiling))), ((naked)), ((tile)), ((fleshpile)), ((ugly)), (((abstract))), blurry, ((bad anatomy)), ((bad proportions)), ((extra limbs)), cloned face, glitchy, ((extra breasts)), ((double torso)), ((extra arms)), ((extra hands)), ((mangled fingers)), ((missing breasts)), (missing lips), ((ugly face)), ((fat)), ((extra legs))",  
    "W": 512,  
    "H": 512,  
    "guidance_scale": 7.5,  
    "init_image": "https://raw.githubusercontent.com/CompVis/stable-diffusion/main/data/inpainting_examples/overture-creations-5sI6fQgYIuo.png",  
    "mask_image": "https://raw.githubusercontent.com/CompVis/stable-diffusion/main/data/inpainting_examples/overture-creations-5sI6fQgYIuo_mask.png",  
    "multi_lingual": "no",  
    "steps": 50,  
    "n_samples": 1,  
    "full_url": "no",  
    "upscale": "no",  
    "seed": 1343687916,  
    "outdir": "out",  
    "file_prefix": "dc639bd6-d605-42c7-950e-48c531124d0d"  
  }  
}  

```
[PreviousImage to Image](/docs/enterprise-plan/img2img)[NextSuper Resolution](/docs/enterprise-plan/super-resolution)* [Overview](#overview)
* [Request](#request)
* [Attributes](#attributes)
	+ [Schedulers](#schedulers)
* [Example](#example)
	+ [Body](#body)
	+ [Request](#request-1)
	+ [Response](#response)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



