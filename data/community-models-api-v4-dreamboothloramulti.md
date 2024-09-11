




Dreambooth V4 LoRA Multi \| Stable Diffusion API Documentation








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
* LoRA Multi
On this pageDreambooth V4 LoRA Multi
========================

* [v4/dreambooth](/docs/community-models-api-v4/dreamboothtext2img)
* [v4/dreambooth/img2img](/docs/community-models-api-v4/dreamboothimg2img)
* [v4/dreambooth/inpaint](/docs/community-models-api-v4/dreamboothinpainting)
* [v4/dreambooth/fetch](/docs/community-models-api-v4/dreamboothfetchqueimg)
* [v4/dreambooth/model\_reload](/docs/community-models-api-v4/dreamboothreloadmodel)
Overview[â](#overview "Direct link to Overview")
--------------------------------------------------

The Dreambooth LoRA Multi is used to create image from text, using multiple LoRA models, based on trained or on public models.

Make an API call using your trained models or any public model by also passing multiple comma separated LoRA model IDs to the `lora_model` parameter, such as "more\_details,cinnamon" for example. 

tipYou can find a list of the public and LoRA models available and their IDs **[here](https://stablediffusionapi.com/models)**.

Request[â](#request "Direct link to Request")
-----------------------------------------------


```
--request POST 'https://stablediffusionapi.com/api/v4/dreambooth' \  

```
Make a `POST` request to <https://stablediffusionapi.com/api/v4/dreambooth> endpoint and pass the required parameters in the request body. 

Body Attributes[â](#body-attributes "Direct link to Body Attributes")
-----------------------------------------------------------------------



| Parameter | Description |
| --- | --- |
| **key** | Your API Key used for request authorization |
| **model\_id** | The ID of the model to be used. It can be public or your trained model. |
| **prompt** | Text prompt with description of the things you want in the image to be generated |
| **negative\_prompt** | Items you don't want in the image |
| **width** | Max Height: Width: 1024x1024 |
| **height** | Max Height: Width: 1024x1024 |
| **samples** | Number of images to be returned in response. The maximum value is 4\. |
| **num\_inference\_steps** | Number of denoising steps (minimum: 1; maximum: 50\) |
| **safety\_checker** | A checker for NSFW images. If such an image is detected, it will be replaced by a blank image. |
| **enhance\_prompt** | Enhance prompts for better results; **default**: yes, **options**: yes/no |
| **seed** | Seed is used to reproduce results, same seed will give you same image in return again. Pass *null* for a random number. |
| **guidance\_scale** | Scale for classifier\-free guidance (minimum: 1; maximum: 20\) |
| **multi\_lingual** | Allow multi lingual prompt to generate images. Set this to "yes" if you use a [language](#multi_lingual-supported-languages) different from English in your text prompts. |
| **panorama** | Set this parameter to "yes" to generate a panorama image. |
| **self\_attention** | If you want a high quality image, set this parameter to "yes". In this case the image generation will take more time. |
| **upscale** | Set this parameter to "yes" if you want to upscale the given image resolution two times (2x). If the requested resolution is 512 x 512 px, the generated image will be 1024 x 1024 px. |
| **embeddings\_model** | Use it to pass an embeddings model (embeddings\_model\_id). |
| **lora\_model** | Pass Lora model id, multi lora is supported, pass comma saparated values. Example "contrast\-fix,yae\-miko\-genshin" |
| **lora\_strength** | Strength of lora model you are using. If using multi lora, pass each values as comma saparated |
| **scheduler** | Use it to set a [scheduler](#schedulers). |
| **webhook** | Set an URL to get a POST API call once the image generation is complete. |
| **track\_id** | This ID is returned in the response to the webhook API call. This will be used to identify the webhook request. |
| **clip\_skip** | Clip Skip (minimum: 1; maximum: 8\) |
| **base64** | Get response as base64 string, pass init\_image, mask\_image , control\_image as base64 string, to get base64 response. **default**: "no", **options**: yes/no |
| **temp** | Create temp image link. This link is valid for 24 hours. **temp**: yes, **options**: yes/no |

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
  "key": "",  
  "model_id": "f222-diffusion",  
  "prompt": "a female model doing photoshoot, ultra realistic face, ultra high resolution, 4K image",  
  "negative_prompt": "painting, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, deformed, ugly, blurry, bad anatomy, bad proportions, extra limbs, cloned face, skinny, glitchy, double torso, extra arms, extra hands, mangled fingers, missing lips, ugly face, distorted face, extra legs, anime",  
  "width": "512",  
  "height": "512",  
  "samples": "1",  
  "num_inference_steps": "30",  
  "safety_checker": "yes",  
  "enhance_prompt": "yes",  
  "seed": null,  
  "guidance_scale": 7.5,  
  "multi_lingual": "no",  
  "panorama": "no",  
  "self_attention": "no",  
  "upscale": "no",  
  "embeddings_model": null,  
  "lora_model": "ganyu-lora,more_details",  
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
  "model_id": "f222-diffusion",  
  "prompt": "a female model doing photoshoot, ultra realistic face, ultra high resolution, 4K image",  
  "negative_prompt": "painting, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, deformed, ugly, blurry, bad anatomy, bad proportions, extra limbs, cloned face, skinny, glitchy, double torso, extra arms, extra hands, mangled fingers, missing lips, ugly face, distorted face, extra legs, anime",  
  "width": "512",  
  "height": "512",  
  "samples": "1",  
  "num_inference_steps": "30",  
  "safety_checker": "yes",  
  "enhance_prompt": "yes",  
  "seed": null,  
  "guidance_scale": 7.5,  
  "multi_lingual": "no",  
  "panorama": "no",  
  "self_attention": "no",  
  "upscale": "no",  
  "embeddings_model": null,  
  "lora_model": "ganyu-lora,more_details",  
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
  
fetch("https://stablediffusionapi.com/api/v4/dreambooth", requestOptions)  
  .then(response => response.text())  
  .then(result => console.log(result))  
  .catch(error => console.log('error', error));  

```

```
<?php  
  
$payload = [  
  "key" => "",   
  "model_id" => "f222-diffusion",   
  "prompt" => "a female model doing photoshoot, ultra realistic face, ultra high resolution, 4K image",   
  "negative_prompt" => "painting, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, deformed, ugly, blurry, bad anatomy, bad proportions, extra limbs, cloned face, skinny, glitchy, double torso, extra arms, extra hands, mangled fingers, missing lips, ugly face, distorted face, extra legs, anime",   
  "width" => "512",   
  "height" => "512",   
  "samples" => "1",   
  "num_inference_steps" => "30",   
  "safety_checker" => "yes",   
  "enhance_prompt" => "yes",   
  "seed" => null,   
  "guidance_scale" => 7.5,   
  "multi_lingual" => "no",   
  "panorama" => "no",   
  "self_attention" => "no",   
  "upscale" => "no",   
  "embeddings_model" => null,   
  "lora_model" => "ganyu-lora,more_details",   
  "scheduler" => "UniPCMultistepScheduler",   
  "webhook" => null,   
  "track_id" => null  
];  
  
$curl = curl_init();  
  
curl_setopt_array($curl, array(  
  CURLOPT_URL => 'https://stablediffusionapi.com/api/v4/dreambooth',  
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
  'url': 'https://stablediffusionapi.com/api/v4/dreambooth',  
  'headers': {  
    'Content-Type': 'application/json'  
  },  
  body: JSON.stringify({  
    "key": "",  
    "model_id": "f222-diffusion",  
    "prompt": "a female model doing photoshoot, ultra realistic face, ultra high resolution, 4K image",  
    "negative_prompt": "painting, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, deformed, ugly, blurry, bad anatomy, bad proportions, extra limbs, cloned face, skinny, glitchy, double torso, extra arms, extra hands, mangled fingers, missing lips, ugly face, distorted face, extra legs, anime",  
    "width": "512",  
    "height": "512",  
    "samples": "1",  
    "num_inference_steps": "30",  
    "safety_checker": "yes",  
    "enhance_prompt": "yes",  
    "seed": null,  
    "guidance_scale": 7.5,  
    "multi_lingual": "no",  
    "panorama": "no",  
    "self_attention": "no",  
    "upscale": "no",  
    "embeddings_model": null,  
    "lora_model": "ganyu-lora,more_details",  
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
  
url = "https://stablediffusionapi.com/api/v4/dreambooth"  
  
payload = json.dumps({  
  "key": "",  
  "model_id": "f222-diffusion",  
  "prompt": "a female model doing photoshoot, ultra realistic face, ultra high resolution, 4K image",  
  "negative_prompt": "painting, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, deformed, ugly, blurry, bad anatomy, bad proportions, extra limbs, cloned face, skinny, glitchy, double torso, extra arms, extra hands, mangled fingers, missing lips, ugly face, distorted face, extra legs, anime",  
  "width": "512",  
  "height": "512",  
  "samples": "1",  
  "num_inference_steps": "30",  
  "safety_checker": "yes",  
  "enhance_prompt": "yes",  
  "seed": None,  
  "guidance_scale": 7.5,  
  "multi_lingual": "no",  
  "panorama": "no",  
  "self_attention": "no",  
  "upscale": "no",  
  "embeddings_model": None,  
  "lora_model": "ganyu-lora,more_details",  
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
RequestBody body = RequestBody.create(mediaType, "{\n   \"key\": \"\",\n   \"model_id\": \"your_model_id\",\n   \"prompt\": \"a female model doing photoshoot, ultra realistic face, ultra high resolution, 4K image\",\n    \"negative_prompt\": \"painting, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, deformed, ugly, blurry, bad anatomy, bad proportions, extra limbs, cloned face, skinny, glitchy, double torso, extra arms, extra hands, mangled fingers, missing lips, ugly face, distorted face, extra legs, anime\",\n     \"width\": \"512\",\n \"height\": \"512\",\n \"samples\": \"1\",\n \"num_inference_steps\": \"30\",\n \"safety_checker\":\"yes\",\n \"enhance_prompt\":\"yes\",\n  \"seed\": null,\n \"guidance_scale\": 7.5,\n \"multi_lingual\":\"no\",\n  \"panorama\":\"no\",\n \"self_attention\":\"no\",\n \"upscale\":\"no\",\n \"embeddings_model\":\"no\",\n  \"lora_model\":\"ganyu-lora,more_details\",\n \"scheduler\":\"UniPCMultistepScheduler\",\n  \"webhook\": null,\n  \"track_id\": null\n}");  
Request request = new Request.Builder()  
  .url("https://stablediffusionapi.com/api/v4/dreambooth")  
  .method("POST", body)  
  .addHeader("Content-Type", "application/json")  
  .build();  
Response response = client.newCall(request).execute();  

```
### Response[â](#response "Direct link to Response")


```
{  
  "status": "processing",  
  "tip": "Your image is processing in background, you can get this image using fetch API: here is link for fetch api : https://stablediffusionapi.com/docs/community-models-api-v4/dreamboothfetchqueimg",  
  "eta": 13.067986918399999,  
  "messege": "Try to fetch request after seconds estimated",  
  "webhook_status": "",  
  "fetch_result": "https://stablediffusionapi.com/api/v3/dreambooth/fetch/29763508",  
  "id": 29763508,  
  "output": [],  
  "meta": {  
    "prompt": " a female model doing photoshoot, ultra realistic face, ultra high resolution, 4K image hyperrealistic, full body, detailed clothing, highly detailed, cinematic lighting, stunningly beautiful, intricate, sharp focus, f/1. 8, 85mm, (centered image composition), (professionally color graded), ((bright soft diffused light)), volumetric fog, trending on instagram, trending on tumblr, HDR 4K, 8K",  
    "model_id": "f222-diffusion",  
    "negative_prompt": "painting, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, deformed, ugly, blurry, bad anatomy, bad proportions, extra limbs, cloned face, skinny, glitchy, double torso, extra arms, extra hands, mangled fingers, missing lips, ugly face, distorted face, extra legs, anime(child:1.5), ((((underage)))), ((((child)))), (((kid))), (((preteen))), (teen:1.5) ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, extra limbs, disfigured, deformed, body out of frame, bad anatomy, watermark, signature, cut off, low contrast, underexposed, overexposed, bad art, beginner, amateur, distorted face, blurry, draft, grainy",  
    "scheduler": "UniPCMultistepScheduler",  
    "safety_checker": "yes",  
    "W": 512,  
    "H": 512,  
    "guidance_scale": 7.5,  
    "seed": 3361266218,  
    "steps": 20,  
    "n_samples": 1,  
    "full_url": "no",  
    "tomesd": "yes",  
    "upscale": "no",  
    "multi_lingual": "no",  
    "panorama": "no",  
    "self_attention": "no",  
    "use_karras_sigmas": "yes",  
    "embeddings": null,  
    "vae": null,  
    "lora": "ganyu-lora,more_details",  
    "lora_strength": 1,  
    "clip_skip": 1,  
    "temp": "no",  
    "base64": "no",  
    "file_prefix": "d00bf96e-8cec-40b4-a090-c87e7165f78e.png"  
  },  
  "future_links": [  
    "https://cdn.stablediffusionapi.com/generations/0-d00bf96e-8cec-40b4-a090-c87e7165f78e.png"  
  ]  
}  

```
[PreviousLoRA](/docs/community-models-api-v4/dreamboothlora)[NextImage to Image](/docs/community-models-api-v4/dreamboothimg2img)* [Overview](#overview)
* [Request](#request)
* [Body Attributes](#body-attributes)
	+ [Multi\_lingual Supported Languages](#multi_lingual-supported-languages)
	+ [Schedulers](#schedulers)
* [Example](#example)
	+ [Body](#body)
	+ [Request](#request-1)
	+ [Response](#response)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



