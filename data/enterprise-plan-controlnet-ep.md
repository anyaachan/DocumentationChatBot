




Enterprise: Controlnet Endpoint \| Stable Diffusion API Documentation








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
* Controlnet
On this pageEnterprise: Controlnet Endpoint
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

This endpoint is used to generate ControlNet images.

tipYou can also use this endpoint to inpaint images with ControlNet. Just make sure to pass the link to the `mask_image` in the request body. and use controlnet\_model as "inpaint"

Request[â](#request "Direct link to Request")
-----------------------------------------------


```
--request POST 'https://stablediffusionapi.com/api/v1/enterprise/controlnet' \  

```
Send a `POST` request to <https://stablediffusionapi.com/api/v1/enterprise/controlnet> endpoint. 

Body Attributes[â](#body-attributes "Direct link to Body Attributes")
-----------------------------------------------------------------------



| Parameter | Description |
| --- | --- |
| **key** | Your enterprise API Key used for request authorization |
| **model\_id** | The ID of the model to be used. It can be public or your trained model. |
| **controlnet\_model** | ControlNet model ID. It can be from the [models](#models) list or user trained. |
| **controlnet\_type** | ControlNet model type. It can be from the [models](#models) list. |
| **auto\_hint** | Auto hint image;**options**: yes/no |
| **guess\_mode** | Set this to *yes* if you don't pass any prompt. The model will try to guess what's in the **init\_image** and create best variations on its own. **Options**: yes/no |
| **prompt** | Text prompt with description of required image modifications. Make it as detailed as possible for best results. |
| **negative\_prompt** | Items you don't want in the image |
| **init\_image** | Link to the Initial Image |
| **control\_image** | Link to the Controlnet Image |
| **mask\_image** | Link to the mask image for inpainting |
| **width** | Max Height: Width: 1024x1024 |
| **height** | Max Height: Width: 1024x1024 |
| **samples** | Number of images to be returned in response. The maximum value is 4\. |
| **scheduler** | Use it to set a [scheduler](#schedulers). |
| **tomesd** | Enable tomesd to generate images: gives really fast results, **default**: yes, **options**: yes/no |
| **use\_karras\_sigmas** | Use keras sigmas to generate images. gives nice results, **default**: yes, **options**: yes/no |
| **algorithm\_type** | Used in DPMSolverMultistepScheduler scheduler, **default**: none, **options**: dpmsolver\+\+\+ |
| **vae** | use custom vae in generating images **default**: null |
| **lora\_strength** | Strength of lora model you are using. If using multi lora, pass each values as comma saparated |
| **lora\_model** | multi lora is supported, pass comma saparated values. Example contrast\-fix,yae\-miko\-genshin |
| **num\_inference\_steps** | Number of denoising steps (minimum: 1; maximum: 50\) |
| **safety\_checker** | A checker for NSFW images. If such an image is detected, it will be replaced by a blank image. |
| **embeddings\_model** | Use it to pass an embeddings model. |
| **enhance\_prompt** | Enhance prompts for better results; **default**: yes, **options**: yes/no |
| **multi\_lingual** | Use different language then english; **default**: yes, **options**: yes/no |
| **guidance\_scale** | Scale for classifier\-free guidance (minimum: 1; maximum: 20\) |
| **controlnet\_conditioning\_scale** | Scale for controlnet guidance (minimum: 1; maximum: 20\) |
| **strength** | Prompt strength when using **init\_image**. 1\.0 corresponds to full destruction of information in the init image. |
| **seed** | Seed is used to reproduce results, same seed will give you same image in return again. Pass *null* for a random number. |
| **webhook** | Set an URL to get a POST API call once the image generation is complete. |
| **track\_id** | This ID is returned in the response to the webhook API call. This will be used to identify the webhook request. |
| **upscale** | Set this parameter to "yes" if you want to upscale the given image resolution two times (2x). If the requested resolution is 512 x 512 px, the generated image will be 1024 x 1024 px. |
| **clip\_skip** | Clip Skip (minimum: 1; maximum: 8\) |
| **base64** | Get response as base64 string, pass init\_image, mask\_image , control\_image as base64 string, to get base64 response. **default**: "no", **options**: yes/no |
| **temp** | Create temp image link. This link is valid for 24 hours. **temp**: yes, **options**: yes/no |

infoTo use the **load balancer**, you need to have **more than 1 server**. Pass the first server's API key, and it will handle the load balancing with the other servers.

tipYou can also use multi ControlNet. Just make sure to pass comma saparated controlnet models to the `controlnet_model` as "canny,depth" and `init_image` in the request body.

### ControlNet Models[â](#controlnet-models "Direct link to ControlNet Models")

ControlNet API using Controlnet 1\.1 as default:
Suported controlnet\_model:

* canny
* depth
* hed
* mlsd
* normal
* openpose
* scribble
* segmentation
* aesthetic\-controlnet
* inpaint
* softedge
* lineart
* shuffle
* tile
* face\_detector

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

tipYou can also use multi Lora. Just make sure to pass comma saparated lora model ids to the `lora_model` as `"more_details,animie"` in the request body.

Example[â](#example "Direct link to Example")
-----------------------------------------------

### Body[â](#body "Direct link to Body")

Body Raw
```
{  
  "key": "enterprise_api_key",  
  "controlnet_model": "canny",  
  "controlnet_type" :"canny",  
  "model_id": "midjourney",  
  "auto_hint": "yes",  
  "guess_mode" : "no",  
  "prompt": "a model doing photoshoot, ultra high resolution, 4K image",  
  "negative_prompt": null,  
  "init_image": "https://huggingface.co/datasets/diffusers/test-arrays/resolve/main/stable_diffusion_imgvar/input_image_vermeer.png",  
  "mask_image": null,  
  "width": "512",  
  "height": "512",  
  "samples": "1",  
  "scheduler": "UniPCMultistepScheduler",  
  "num_inference_steps": "30",  
  "safety_checker": "no",  
  "enhance_prompt": "yes",  
  "guidance_scale": 7.5,  
  "strength": 0.55,  
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
  "controlnet_model": "canny",  
  "controlnet_type" :"canny",  
  "model_id": "midjourney",  
  "auto_hint": "yes",  
  "guess_mode" : "no",  
  "prompt": "a model doing photoshoot, ultra high resolution, 4K image",  
  "negative_prompt": null,  
  "init_image": "https://huggingface.co/datasets/diffusers/test-arrays/resolve/main/stable_diffusion_imgvar/input_image_vermeer.png",  
  "mask_image": null,  
  "width": "512",  
  "height": "512",  
  "samples": "1",  
  "scheduler": "UniPCMultistepScheduler",  
  "num_inference_steps": "30",  
  "safety_checker": "no",  
  "enhance_prompt": "yes",  
  "guidance_scale": 7.5,  
  "strength": 0.55,  
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
  
fetch("https://stablediffusionapi.com/api/v1/enterprise/controlnet", requestOptions)  
  .then(response => response.text())  
  .then(result => console.log(result))  
  .catch(error => console.log('error', error));  

```

```
<?php  
  
$payload = [  
  "key" => "",   
  "controlnet_model" => "canny",   
  "controlnet_type" => "canny",   
  "model_id" => "midjourney",   
  "auto_hint" => "yes",   
  "guess_mode" => "no",   
  "prompt" => "a model doing photoshoot, ultra high resolution, 4K image",   
  "negative_prompt" => null,   
  "init_image" => "https://huggingface.co/datasets/diffusers/test-arrays/resolve/main/stable_diffusion_imgvar/input_image_vermeer.png",   
  "mask_image" => null,  
  "width" => "512",   
  "height" => "512",   
  "samples" => "1",   
  "scheduler" => "UniPCMultistepScheduler",   
  "num_inference_steps" => "30",   
  "safety_checker" => "no",   
  "enhance_prompt" => "yes",   
  "guidance_scale" => 7.5,   
  "strength" => 0.55,   
  "seed" => null,   
  "webhook" => null,   
  "track_id" => null   
];  
  
$curl = curl_init();  
  
curl_setopt_array($curl, array(  
  CURLOPT_URL => 'https://stablediffusionapi.com/api/v1/enterprise/controlnet',  
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
  'url': 'https://stablediffusionapi.com/api/v1/enterprise/controlnet',  
  'headers': {  
    'Content-Type': 'application/json'  
  },  
  body: JSON.stringify({  
    "key": "",  
    "controlnet_model": "canny",  
    "controlnet_type": "canny",  
    "model_id": "midjourney",  
    "auto_hint": "yes",  
    "guess_mode": "no",  
    "prompt": "a model doing photoshoot, ultra high resolution, 4K image",  
    "negative_prompt": null,  
    "init_image": "https://huggingface.co/datasets/diffusers/test-arrays/resolve/main/stable_diffusion_imgvar/input_image_vermeer.png",  
    "mask_image": null,  
    "width": "512",  
    "height": "512",  
    "samples": "1",  
    "scheduler": "UniPCMultistepScheduler",  
    "num_inference_steps": "30",  
    "safety_checker": "no",  
    "enhance_prompt": "yes",  
    "guidance_scale": 7.5,  
    "strength": 0.55,  
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
  
url = "https://stablediffusionapi.com/api/v1/enterprise/controlnet"  
  
payload = json.dumps({  
  "key": "",  
  "controlnet_model": "canny",  
  "controlnet_type": "canny",  
  "model_id": "midjourney",  
  "auto_hint": "yes",  
  "guess_mode": "no",  
  "prompt": "a model doing photoshoot, ultra high resolution, 4K image",  
  "negative_prompt": None,  
  "init_image": "https://huggingface.co/datasets/diffusers/test-arrays/resolve/main/stable_diffusion_imgvar/input_image_vermeer.png",  
  "mask_image": None,  
  "width": "512",  
  "height": "512",  
  "samples": "1",  
  "scheduler": "UniPCMultistepScheduler",  
  "num_inference_steps": "30",  
  "safety_checker": "no",  
  "enhance_prompt": "yes",  
  "guidance_scale": 7.5,  
  "strength": 0.55,  
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
RequestBody body = RequestBody.create(mediaType, "{\n    \"key\": \"\",\n    \"controlnet_model\": \"canny\",\n    \"type\": \"canny\",\n   \"model_id\": \"midjourney\",\n    \"auto_hint\" : \"yes\",\n    \"guess_mode\" : \"no\",\n    \"prompt\": \"a model doing photoshoot, ultra high resolution, 4K image\",\n    \"negative_prompt\": null,\n    \"init_image\": \"https://huggingface.co/datasets/diffusers/test-arrays/resolve/main/stable_diffusion_imgvar/input_image_vermeer.png\",\n  \"mask_image\": null,\n   \"width\": \"512\",\n    \"height\": \"512\",\n    \"samples\": \"1\",\n    \"scheduler\": \"UniPCMultistepScheduler\",\n    \"num_inference_steps\": \"30\",\n    \"safety_checker\": \"no\",\n    \"enhance_prompt\": \"yes\",\n    \"guidance_scale\": 7.5,\n    \"strength\": 0.55,\n    \"seed\": null,\n    \"webhook\": null,\n    \"track_id\": null\n}");  
Request request = new Request.Builder()  
  .url("https://stablediffusionapi.com/api/v1/enterprise/controlnet")  
  .method("POST", body)  
  .addHeader("Content-Type", "application/json")  
  .build();  
Response response = client.newCall(request).execute();  

```
### Response[â](#response "Direct link to Response")


```
{  
    "status": "success",  
    "generationTime": 3.6150574684143066,  
    "id": 14905468,  
    "output": [  
        "https://pub-8b49af329fae499aa563997f5d4068a4.r2.dev/generations/b989586c-0a5f-41fa-91de-1c5ed5498349-0.png"  
    ],  
    "meta": {  
        "prompt": "mdjrny-v4 style a model doing photoshoot, ultra high resolution, 4K image",  
        "model_id": "midjourney",  
        "controlnet_model": "canny",  
        "controlnet_type": "canny",  
        "negative_prompt": "",  
        "scheduler": "UniPCMultistepScheduler",  
        "safetychecker": "no",  
        "auto_hint": "yes",  
        "guess_mode": "no",  
        "strength": 0.55,  
        "W": 512,  
        "H": 512,  
        "guidance_scale": 3,  
        "seed": 254638058,  
        "multi_lingual": "no",  
        "init_image": "https://huggingface.co/datasets/diffusers/test-arrays/resolve/main/stable_diffusion_imgvar/input_image_vermeer.png",  
        "mask_image": null,  
        "steps": 20,  
        "full_url": "no",  
        "upscale": "no",  
        "n_samples": 1,  
        "embeddings": null,  
        "lora": null,  
        "outdir": "out",  
        "file_prefix": "b989586c-0a5f-41fa-91de-1c5ed5498349"  
    }  
}  

```
[PreviousDelete Model](/docs/enterprise-plan/delete-model)[NextText to Image](/docs/enterprise-plan/text2img)* [Overview](#overview)
* [Request](#request)
* [Body Attributes](#body-attributes)
	+ [ControlNet Models](#controlnet-models)
	+ [Schedulers](#schedulers)
* [Example](#example)
	+ [Body](#body)
	+ [Request](#request-1)
	+ [Response](#response)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



