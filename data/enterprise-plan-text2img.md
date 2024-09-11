




Enterprise: Text to Image Endpoint \| Stable Diffusion API Documentation








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
* Text to Image
On this pageEnterprise: Text to Image Endpoint
==================================

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
* [enterprise/fetch\_queue\_image](/docs/enterprise-plan/fetch-queue-image)
Overview[â](#overview "Direct link to Overview")
--------------------------------------------------

This endpoint is used to create an image from a text prompt based on trained or on public models.

You can make an API call using your trained models as well as any public model.

tipYou can find a list of the public models available and their IDs **[here](https://stablediffusionapi.com/models)**.

This endpoint generates and returns an image from a text passed in the request body.

![Text to image endpoint result](/docs/assets/images/ep-txt2img-action-sm-6f01f34d73558a77c54ae8d8559492a3.png)Request[â](#request "Direct link to Request")
-----------------------------------------------


```
--request POST 'https://stablediffusionapi.com/api/v1/enterprise/text2img' \  

```
Make a `POST` request to <https://stablediffusionapi.com/api/v1/enterprise/text2img> endpoint and pass the required parameters as a request body. 

Watch the how\-to video to see it in action.

Body Attributes[â](#body-attributes "Direct link to Body Attributes")
-----------------------------------------------------------------------



| Parameter | Description |
| --- | --- |
| **key** | Your enterprise API Key used for request authorization |
| **model\_id** | The ID of the model to be used. It can be public or your trained model. |
| **prompt** | Text prompt with description of the things you want in the image to be generated |
| **negative\_prompt** | Items you don't want in the image |
| **width** | Max Height: Width: 1024x1024 |
| **height** | Max Height: Width: 1024x1024 |
| **samples** | Number of images to be returned in response. The maximum value is 4\. |
| **num\_inference\_steps** | Number of denoising steps (minimum: 1; maximum: 50\) |
| **safety\_checker** | A checker for NSFW images. If such an image is detected, it will be replaced by a blank image. |
| **safety\_checker\_type** | Modify image if NSFW images are found; **default**: sensitive\_content\_text, **options**: blur/sensitive\_content\_text/pixelate/black |
| **enhance\_prompt** | Enhance prompts for better results; **default**: yes, **options**: yes/no |
| **seed** | Seed is used to reproduce results, same seed will give you same image in return again. Pass *null* for a random number. |
| **guidance\_scale** | Scale for classifier\-free guidance (minimum: 1; maximum: 20\) |
| **multi\_lingual** | Allow multi lingual prompt to generate images. Set this to "yes" if you use a [language](#multi_lingual-supported-languages) different from English in your text prompts. |
| **panorama** | Set this parameter to "yes" to generate a panorama image. |
| **self\_attention** | If you want a high quality image, set this parameter to "yes". In this case the image generation will take more time. |
| **upscale** | Set this parameter to "yes" if you want to upscale the given image resolution two times (2x). If the requested resolution is 512 x 512 px, the generated image will be 1024 x 1024 px. |
| **embeddings\_model** | Use it to pass an embeddings model. |
| **tomesd** | Enable tomesd to generate images: gives really fast results, **default**: yes, **options**: yes/no |
| **use\_karras\_sigmas** | Use keras sigmas to generate images. gives nice results, **default**: yes, **options**: yes/no |
| **algorithm\_type** | Used in DPMSolverMultistepScheduler scheduler, **default**: none, **options**: dpmsolver\+\+\+ |
| **vae** | use custom vae in generating images **default**: null |
| **lora\_strength** | Strength of lora model you are using. If using multi lora, pass each values as comma saparated |
| **lora\_model** | multi lora is supported, pass comma saparated values . Example contrast\-fix,yae\-miko\-genshin |
| **scheduler** | Use it to set a [scheduler](#schedulers). |
| **webhook** | Set an URL to get a POST API call once the image generation is complete. |
| **track\_id** | This ID is returned in the response to the webhook API call. This will be used to identify the webhook request. |
| **loadbalancer** | Enable load balancer; **options**: yes/no, **default**: no. |
| **clip\_skip** | Clip Skip (minimum: 1; maximum: 8\) |
| **base64** | Get response as base64 string, **default**: "no", **options**: yes/no |
| **highres\_fix** | highres fix for generated image, **default**: "no", **options**: yes/no |
| **temp** | Create temp image link. This link is valid for 24 hours. **temp**: yes, **options**: yes/no |

infoTo use the **load balancer**, you need to have **more than 1 server**. Pass the first server's API key, and it will handle the load balancing with the other servers.

tipYou can also use multi Lora. Just make sure to pass comma saparated lora model ids to the `lora_model` as `"more_details,animie"` in the request body.

### Multi\_lingual Supported Languages[â](#multi_lingual-supported-languages "Direct link to Multi_lingual Supported Languages")

If you use a language different from English in you text prompts, pass the "multi\_lingual" parameter with "yes" value in the request body. This will trigger an automatic language detection and translation during the processing of your request.

The following languages are supported:

Arabic (ar\_AR), Czech (cs\_CZ), German (de\_DE), English (en\_XX), Spanish (es\_XX), Estonian (et\_EE), Finnish (fi\_FI), French (fr\_XX), Gujarati (gu\_IN), Hindi (hi\_IN), Italian (it\_IT), Japanese (ja\_XX), Kazakh (kk\_KZ), Korean (ko\_KR), Lithuanian (lt\_LT), Latvian (lv\_LV), Burmese (my\_MM), Nepali (ne\_NP), Dutch (nl\_XX), Romanian (ro\_RO), Russian (ru\_RU), Sinhala (si\_LK), Turkish (tr\_TR), Vietnamese (vi\_VN), Chinese (zh\_CN), Afrikaans (af\_ZA), Azerbaijani (az\_AZ), Bengali (bn\_IN), Persian (fa\_IR), Hebrew (he\_IL), Croatian (hr\_HR), Indonesian (id\_ID), Georgian (ka\_GE), Khmer (km\_KH), Macedonian (mk\_MK), Malayalam (ml\_IN), Mongolian (mn\_MN), Marathi (mr\_IN), Polish (pl\_PL), Pashto (ps\_AF), Portuguese (pt\_XX), Swedish (sv\_SE), Swahili (sw\_KE), Tamil (ta\_IN), Telugu (te\_IN), Thai (th\_TH), Tagalog (tl\_XX), Ukrainian (uk\_UA), Urdu (ur\_PK), Xhosa (xh\_ZA), Galician (gl\_ES), Slovene (sl\_SI)

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
  "key": "enterprise_api_key",  
  "model_id": "model_id",  
  "prompt": "ultra realistic close up portrait ((beautiful pale cyberpunk female with heavy black eyeliner)), blue eyes, shaved side haircut, hyper detail, cinematic lighting, magic neon, dark red city, Canon EOS R3, nikon, f/1.4, ISO 200, 1/160s, 8K, RAW, unedited, symmetrical balance, in-frame, 8K",  
  "negative_prompt": "painting, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, deformed, ugly, blurry, bad anatomy, bad proportions, extra limbs, cloned face, skinny, glitchy, double torso, extra arms, extra hands, mangled fingers, missing lips, ugly face, distorted face, extra legs, anime",  
  "width": "512",  
  "height": "512",  
  "samples": "1",  
  "num_inference_steps": "20",  
  "safety_checker": "no",  
  "enhance_prompt": "yes",  
  "seed": null,  
  "guidance_scale": 7.5,  
  "multi_lingual": "no",  
  "panorama": "no",  
  "self_attention": "no",  
  "upscale": "no",  
  "embeddings_model": null,  
  "lora_model": null,  
  "clip_skip": "2",  
  "tomesd": "yes",  
  "use_karras_sigmas": "yes",  
  "vae": null,  
  "lora_strength": null,  
  "scheduler": "UniPCMultistepScheduler",  
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
  "model_id": "model_id",  
  "prompt": "ultra realistic close up portrait ((beautiful pale cyberpunk female with heavy black eyeliner)), blue eyes, shaved side haircut, hyper detail, cinematic lighting, magic neon, dark red city, Canon EOS R3, nikon, f/1.4, ISO 200, 1/160s, 8K, RAW, unedited, symmetrical balance, in-frame, 8K",  
  "negative_prompt": "painting, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, deformed, ugly, blurry, bad anatomy, bad proportions, extra limbs, cloned face, skinny, glitchy, double torso, extra arms, extra hands, mangled fingers, missing lips, ugly face, distorted face, extra legs, anime",  
  "width": "512",  
  "height": "512",  
  "samples": "1",  
  "num_inference_steps": "30",  
  "safety_checker": "no",  
  "enhance_prompt": "yes",  
  "seed": null,  
  "guidance_scale": 7.5,  
  "multi_lingual": "no",  
  "panorama": "no",  
  "self_attention": "no",  
  "upscale": "no",  
  "embeddings_model": null,  
  "lora_model": null,  
  "tomesd": "yes",  
  "use_karras_sigmas": "yes",  
  "vae": null,  
  "lora_strength": null,  
  "scheduler": "UniPCMultistepScheduler",  
  "webhook": null,  
  "track_id": null  
});  
  
var requestOptions = {  
  method: 'POST',  
  headers: myHeaders,  
  body: raw,  
  redirect: 'follow'  
};  
  
fetch("https://stablediffusionapi.com/api/v1/enterprise/text2img", requestOptions)  
  .then(response => response.text())  
  .then(result => console.log(result))  
  .catch(error => console.log('error', error));  

```

```
<?php  
  
$payload = [  
  "key" => "",   
  "model_id" => "model_id",   
  "prompt" => "ultra realistic close up portrait ((beautiful pale cyberpunk female with heavy black eyeliner)), blue eyes, shaved side haircut, hyper detail, cinematic lighting, magic neon, dark red city, Canon EOS R3, nikon, f/1.4, ISO 200, 1/160s, 8K, RAW, unedited, symmetrical balance, in-frame, 8K",  
  "negative_prompt" => "painting, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, deformed, ugly, blurry, bad  anatomy, bad proportions, extra limbs, cloned face, skinny, glitchy, double torso, extra arms, extra hands, mangled fingers,   missing lips, ugly face, distorted face, extra legs, anime",   
  "width" => "512",   
  "height" => "512",   
  "samples" => "1",   
  "num_inference_steps" => "30",   
  "safety_checker" => "no",   
  "enhance_prompt" => "yes",   
  "seed" => null,   
  "guidance_scale" => 7.5,   
  "multi_lingual" => "no",   
  "panorama" => "no",   
  "self_attention" => "no",   
  "upscale" => "no",   
  "embeddings_model" => null,   
  "lora_model" => null,  
  "tomesd" => "yes",  
  "use_karras_sigmas" => "yes",  
  "vae" => null,  
  "lora_strength" => null,  
  "scheduler" => "UniPCMultistepScheduler",  
  "webhook" => null,   
  "track_id" => null   
];  
  
$curl = curl_init();  
  
curl_setopt_array($curl, array(  
  CURLOPT_URL => 'https://stablediffusionapi.com/api/v1/enterprise/text2img',  
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
  'url': 'https://stablediffusionapi.com/api/v1/enterprise/text2img',  
  'headers': {  
    'Content-Type': 'application/json'  
  },  
  body: JSON.stringify({  
    "key": "",  
    "model_id": "model_id",  
    "prompt": "ultra realistic close up portrait ((beautiful pale cyberpunk female with heavy black eyeliner)), blue eyes, shaved side haircut, hyper detail, cinematic lighting, magic neon, dark red city, Canon EOS R3, nikon, f/1.4, ISO 200, 1/160s, 8K, RAW, unedited, symmetrical balance, in-frame, 8K",  
    "negative_prompt": "painting, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, deformed, ugly, blurry, bad  anatomy, bad proportions, extra limbs, cloned face, skinny, glitchy, double torso, extra arms, extra hands, mangled fingers,   missing lips, ugly face, distorted face, extra legs, anime",  
    "width": "512",  
    "height": "512",  
    "samples": "1",  
    "num_inference_steps": "30",  
    "safety_checker": "no",  
    "enhance_prompt": "yes",  
    "seed": null,  
    "guidance_scale": 7.5,  
    "multi_lingual": "no",  
    "panorama": "no",  
    "self_attention": "no",  
    "upscale": "no",  
    "embeddings_model": null,  
    "tomesd": "yes",  
    "use_karras_sigmas": "yes",  
    "vae": null,  
    "lora_strength": null,  
    "lora_model": null,  
    "scheduler": "UniPCMultistepScheduler",  
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
  
url = "https://stablediffusionapi.com/api/v1/enterprise/text2img"  
  
payload = json.dumps({  
  "key": "",  
  "model_id": "model_id",  
  "prompt": "ultra realistic close up portrait ((beautiful pale cyberpunk female with heavy black eyeliner)), blue eyes, shaved side haircut, hyper detail, cinematic lighting, magic neon, dark red city, Canon EOS R3, nikon, f/1.4, ISO 200, 1/160s, 8K, RAW, unedited, symmetrical balance, in-frame, 8K",  
  "negative_prompt": "painting, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, deformed, ugly, blurry, bad anatomy, bad proportions, extra limbs, cloned face, skinny, glitchy, double torso, extra arms, extra hands, mangled fingers, missing lips, ugly face, distorted face, extra legs, anime",  
  "width": "512",  
  "height": "512",  
  "samples": "1",  
  "num_inference_steps": "30",  
  "safety_checker": "no",  
  "enhance_prompt": "yes",  
  "seed": None,  
  "guidance_scale": 7.5,  
  "multi_lingual": "no",  
  "panorama": "no",  
  "self_attention": "no",  
  "upscale": "no",  
  "embeddings_model": None,  
  "tomesd": "yes",  
  "use_karras_sigmas": "yes",  
  "vae": None,  
  "lora_strength": None,  
  "lora_model": None,  
  "scheduler": "UniPCMultistepScheduler",  
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
RequestBody body = RequestBody.create(mediaType, "{\n    \"key\": \"\",\n  \"model_id\": \"model_id\",\n  \"prompt\": \"ultra realistic close up portrait ((beautiful pale cyberpunk female with heavy black eyeliner)), blue eyes, shaved side haircut, hyper detail, cinematic lighting, magic neon, dark red city, Canon EOS R3, nikon, f/1.4, ISO 200, 1/160s, 8K, RAW, unedited, symmetrical balance, in-frame, 8K\",\n  \"negative_prompt\": \"painting, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, deformed, ugly, blurry, bad anatomy, bad proportions, extra limbs, cloned face, skinny, glitchy, double torso, extra arms, extra hands, mangled fingers, missing lips, ugly face, distorted face, extra legs, anime\",\n  \"width\": \"512\",\n  \"height\": \"512\",\n  \"samples\": \"1\",\n  \"num_inference_steps\": \"20\",\n  \"safety_checker\": \"no\",\n  \"enhance_prompt\": \"yes\",\n  \"seed\": null,\n  \"guidance_scale\": 7.5,\n  \"multi_lingual\": \"no\",\n  \"panorama\": \"no\",\n  \"self_attention\": \"no\",\n  \"upscale\": \"no\",\n  \"embeddings_model\": \"embeddings_model_id\",\n  \"lora_model\": \"lora_model_id\",\n  \"tomesd\": \"yes\",\n  \"use_karras_sigmas\": \"yes\",\n  \"vae\": null,\n  \"lora_strength\": null,\n  \"scheduler\": \"UniPCMultistepScheduler\",\n  \"webhook\": null,\n  \"track_id\": null\n}");  
Request request = new Request.Builder()  
  .url("https://stablediffusionapi.com/api/v1/enterprise/text2img")  
  .method("POST", body)  
  .addHeader("Content-Type", "application/json")  
  .build();  
Response response = client.newCall(request).execute();  

```
### Response[â](#response "Direct link to Response")


```
{  
  "status": "success",  
  "generationTime": 2.920767068862915,  
  "id": 302455,  
  "output": [  
    "https://d1okzptojspljx.cloudfront.net/generations/05c3260d-6a2e-4aa5-82f0-e952f2a5fa10-0.png"  
  ],  
  "meta": {  
    "prompt": "ultra realistic close up portrait ((beautiful pale cyberpunk female with heavy black eyeliner)), blue eyes, shaved side haircut, hyper detail, cinematic lighting, magic neon, dark red city, Canon EOS R3, nikon, f/1.4, ISO 200, 1/160s, 8K, RAW, unedited, symmetrical balance, in-frame, 8K",  
    "model_id": "runwayml/stable-diffusion-v1-5",  
    "negative_prompt": "painting, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, deformed, ugly, blurry, bad anatomy, bad proportions, extra limbs, cloned face, skinny, glitchy, double torso, extra arms, extra hands, mangled fingers, missing lips, ugly face, distorted face, extra legs, anime ((out of frame)), ((extra fingers)), mutated hands, ((poorly drawn hands)), ((poorly drawn face)), (((mutation))), (((deformed))), (((tiling))), ((naked)), ((tile)), ((fleshpile)), ((ugly)), (((abstract))), blurry, ((bad anatomy)), ((bad proportions)), ((extra limbs)), cloned face, glitchy, ((extra breasts)), ((double torso)), ((extra arms)), ((extra hands)), ((mangled fingers)), ((missing breasts)), (missing lips), ((ugly face)), ((fat)), ((extra legs))",  
    "scheduler": "UniPCMultistepScheduler",  
    "revision": "fp16",  
    "safetychecker": "no",  
    "W": 512,  
    "H": 512,  
    "enable_attention_slicing": "true",  
    "file_prefix": "05c3260d-6a2e-4aa5-82f0-e952f2a5fa10",  
    "guidance_scale": 7.5,  
    "seed": 1793745243,  
    "steps": 20,  
    "n_samples": 1,  
    "upscale": "no",  
    "multi_lingual": "no",  
    "panorama": "no",  
    "self_attention": "no",  
    "embeddings": null,  
    "lora": null,  
    "outdir": "out",  
    "vae": "stabilityai/sd-vae-ft-mse"  
  }  
}  

```
[PreviousControlnet](/docs/enterprise-plan/controlnet-ep)[NextText to Video](/docs/enterprise-plan/text2video)* [Overview](#overview)
* [Request](#request)
* [Body Attributes](#body-attributes)
	+ [Multi\_lingual Supported Languages](#multi_lingual-supported-languages)
	+ [Schedulers](#schedulers)
* [Example](#example)
	+ [Body](#body)
	+ [Request](#request-1)
	+ [Response](#response)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



