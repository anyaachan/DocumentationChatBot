




ControlNet Multi Endpoint \| Stable Diffusion API Documentation








[Skip to main content](#docusaurus_skipToContent_fallback)[![Stable Diffusion Logo](/docs/img/SD-logo.png)![Stable Diffusion Logo](/docs/img/SD-logo.png)](https://stablediffusionapi.com)[Enterprise](https://stablediffusionapi.com/enterprise)[Pricing](https://stablediffusionapi.com/#pricing)[Blog](https://stablediffusionapi.com/blog)[Docs](https://stablediffusionapi.com/docs)[Playground](https://stablediffusionapi.com/playground)[Models](https://stablediffusionapi.com/models)[API Catalogue](https://stablediffusionapi.com/catalogue)* [Getting Started](/docs/)
* [Stable Diffusion API](/docs/category/stable-diffusion-api)
* [Train Model](/docs/category/train-model)
* [Community Models API](/docs/category/community-models-api)
* [Text To Video](/docs/category/text-to-video)
* [Community Models API V4](/docs/category/community-models-api-v4)
* [MISCS](/docs/category/miscs)
* [ControlNet](/docs/category/controlnet)
	+ [API Overview](/docs/controlnet/overview)
	+ [ControlNet Main](/docs/controlnet/controlnet-main)
	+ [ControlNet Multi](/docs/controlnet/controlnet-multi)
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
* [ControlNet](/docs/category/controlnet)
* ControlNet Multi
On this pageControlNet Multi Endpoint
=========================

Overview[â](#overview "Direct link to Overview")
--------------------------------------------------

You can now specify multiple ControlNet [models](#models). Just make sure to pass **comma separated** ControlNet models to the `controlnet_model` parameter as "canny,depth" and `init_image` in the request body. 

tipYou can also use this endpoint to inpaint images with ControlNet. Just make sure to pass the link to the `mask_image` in the request body and the controlnet\_model parameter with the "inpaint" value.

infoRead our detailed **[blog article](https://stablediffusionapi.com/blog/stable-diffusion-api/control-net-stable-diffusion-api)** about ControlNet.

Request[â](#request "Direct link to Request")
-----------------------------------------------


```
--request POST 'https://stablediffusionapi.com/api/v5/controlnet' \  

```
Send a `POST` request to <https://stablediffusionapi.com/api/v5/controlnet> endpoint. 

Body Attributes[â](#body-attributes "Direct link to Body Attributes")
-----------------------------------------------------------------------



| Parameter | Description |
| --- | --- |
| **key** | Your API Key used for request authorization |
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
| **lora\_strength** | use different lora strengths **default**: null |
| **lora\_model** | multi lora is supported, pass comma saparated values. Example contrast\-fix,yae\-miko\-genshin |
| **num\_inference\_steps** | Number of denoising steps (minimum: 1; maximum: 50\) |
| **safety\_checker** | A checker for NSFW images. If such an image is detected, it will be replaced by a blank image. |
| **embeddings\_model** | Use it to pass an embeddings model. |
| **enhance\_prompt** | Enhance prompts for better results; **default**: yes, **options**: yes/no |
| **multi\_lingual** | Use different language then english; **default**: yes, **options**: yes/no |
| **controlnet\_conditioning\_scale** | "guidance\_scale" for controlnet, Scale for controlnet guidance. Accepts floating values from 0\.1 to 5 (e.g. 0\.5\) |
| **strength** | Prompt strength when using **init\_image**. 1\.0 corresponds to full destruction of information in the init image. |
| **seed** | Seed is used to reproduce results, same seed will give you same image in return again. Pass *null* for a random number. |
| **webhook** | Set an URL to get a POST API call once the image generation is complete. |
| **track\_id** | This ID is returned in the response to the webhook API call. This will be used to identify the webhook request. |
| **upscale** | Set this parameter to "yes" if you want to upscale the given image resolution two times (2x). If the requested resolution is 512 x 512 px, the generated image will be 1024 x 1024 px. |
| **clip\_skip** | Clip Skip (minimum: 1; maximum: 8\) |
| **base64** | Get response as base64 string, pass init\_image, mask\_image , control\_image as base64 string, to get base64 response. **default**: "no", **options**: yes/no |
| **temp** | Create temp image link. This link is valid for 24 hours. **temp**: yes, **options**: yes/no |

tipYou can also use multi ControlNet. Just make sure to pass comma separated ControlNet models to the `controlnet_model` as "canny,depth" and `init_image` in the request body.

### Models[â](#models "Direct link to Models")

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
* qrcode

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
  "key": "",  
  "controlnet_model": "openpose,canny,face_detector",  
  "controlnet_type" :"openpose",  
  "model_id": "midjourney",  
  "auto_hint": "yes",  
  "guess_mode" : "yes",  
  "prompt": "human model doing photoshoot, ultra realistic face, ultra high resolution, 4K image",  
  "negative_prompt": null,  
  "control_image":"https://huggingface.co/takuma104/controlnet_dev/resolve/main/gen_compare/control_images/converted/control_human_openpose.png",  
  "init_image": "https://cdn.stablediffusionapi.com/generations/0-4957a91a-a45e-459e-b4cd-b3ca4013b847.png",  
  "mask_image": null,  
  "width": "512",  
  "height": "512",  
  "samples": "1",  
  "scheduler": "UniPCMultistepScheduler",  
  "num_inference_steps": "30",  
  "safety_checker": "no",  
  "enhance_prompt": "yes",  
  "guidance_scale": 7.5,  
  "controlnet_conditioning_scale": 0.7,  
  "strength": 0.55,  
  "lora_model": "yae-miko-genshin,more_details",  
  "clip_skip": "2",  
  "tomesd": "yes",  
  "use_karras_sigmas": "yes",  
  "vae": null,  
  "lora_strength": null,  
  "embeddings_model": null,  
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
  "controlnet_model": "openpose,canny,face_detector",  
  "controlnet_type" :"openpose",  
  "model_id": "midjourney",  
  "auto_hint": "yes",  
  "guess_mode" : "yes",  
  "prompt": "human model doing photoshoot, ultra realistic face, ultra high resolution, 4K image",  
  "negative_prompt": null,  
  "control_image":"https://huggingface.co/takuma104/controlnet_dev/resolve/main/gen_compare/control_images/converted/control_human_openpose.png",  
  "init_image": "https://cdn.stablediffusionapi.com/generations/0-4957a91a-a45e-459e-b4cd-b3ca4013b847.png",  
  "mask_image": null,  
  "width": "512",  
  "height": "512",  
  "samples": "1",  
  "scheduler": "UniPCMultistepScheduler",  
  "num_inference_steps": "30",  
  "safety_checker": "no",  
  "enhance_prompt": "yes",  
  "guidance_scale": 7.5,  
  "controlnet_conditioning_scale": 0.7,  
  "strength": 0.55,  
  "lora_model": "yae-miko-genshin,more_details",  
  "clip_skip": "2",  
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
  
fetch("https://stablediffusionapi.com/api/v5/controlnet", requestOptions)  
  .then(response => response.text())  
  .then(result => console.log(result))  
  .catch(error => console.log('error', error));  

```

```
<?php  
  
$payload = [  
  "key" => "",   
  "controlnet_model" => "openpose,canny,face_detector",   
  "controlnet_type" => "openpose",   
  "model_id" => "midjourney",   
  "auto_hint" => "yes",   
  "guess_mode" => "yes",   
  "prompt" => "human model doing photoshoot, ultra realistic face, ultra high resolution, 4K image",   
  "negative_prompt" => null,   
  "control_image" => "https://huggingface.co/takuma104/controlnet_dev/resolve/main/gen_compare/control_images/converted/control_human_openpose.png",   
  "init_image" => "https://cdn.stablediffusionapi.com/generations/0-4957a91a-a45e-459e-b4cd-b3ca4013b847.png",   
  "mask_image" => null,   
  "width" => "512",   
  "height" => "512",   
  "samples" => "1",   
  "scheduler" => "UniPCMultistepScheduler",   
  "num_inference_steps" => "30",   
  "safety_checker" => "no",   
  "enhance_prompt" => "yes",   
  "guidance_scale" => 7.5,   
  "controlnet_conditioning_scale" => 0.7,  
  "strength" => 0.55,   
  "lora_model" => "yae-miko-genshin,more_details",   
  "clip_skip" => "2",   
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
  CURLOPT_URL => 'https://stablediffusionapi.com/api/v5/controlnet',  
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
  'url': 'https://stablediffusionapi.com/api/v5/controlnet',  
  'headers': {  
    'Content-Type': 'application/json'  
  },  
  body: JSON.stringify({  
    "key": "",  
    "controlnet_model": "openpose,canny,face_detector",  
    "controlnet_type" :"openpose",  
    "model_id": "midjourney",  
    "auto_hint": "yes",  
    "guess_mode" : "yes",  
    "prompt": "human model doing photoshoot, ultra realistic face, ultra high resolution, 4K image",  
    "negative_prompt": null,  
    "control_image":"https://huggingface.co/takuma104/controlnet_dev/resolve/main/gen_compare/control_images/converted/control_human_openpose.png",  
    "init_image": "https://cdn.stablediffusionapi.com/generations/0-4957a91a-a45e-459e-b4cd-b3ca4013b847.png",  
    "mask_image": null,  
    "width": "512",  
    "height": "512",  
    "samples": "1",  
    "scheduler": "UniPCMultistepScheduler",  
    "num_inference_steps": "30",  
    "safety_checker": "no",  
    "enhance_prompt": "yes",  
    "guidance_scale": 7.5,  
    "controlnet_conditioning_scale": 0.7,  
    "strength": 0.55,  
    "lora_model": "yae-miko-genshin,more_details",  
    "clip_skip": "2",  
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
  
url = "https://stablediffusionapi.com/api/v5/controlnet"  
  
payload = json.dumps({  
  "key": "",  
  "controlnet_model": "openpose,canny,face_detector",  
  "controlnet_type" :"openpose",  
  "model_id": "midjourney",  
  "auto_hint": "yes",  
  "guess_mode" : "yes",  
  "prompt": "human model doing photoshoot, ultra realistic face, ultra high resolution, 4K image",  
  "negative_prompt": None,  
  "control_image":"https://huggingface.co/takuma104/controlnet_dev/resolve/main/gen_compare/control_images/converted/control_human_openpose.png",  
  "init_image": "https://cdn.stablediffusionapi.com/generations/0-4957a91a-a45e-459e-b4cd-b3ca4013b847.png",  
  "mask_image": None,  
  "width": "512",  
  "height": "512",  
  "samples": "1",  
  "scheduler": "UniPCMultistepScheduler",  
  "num_inference_steps": "30",  
  "safety_checker": "no",  
  "enhance_prompt": "yes",  
  "guidance_scale": 7.5,  
  "controlnet_conditioning_scale": 0.7,  
  "strength": 0.55,  
  "lora_model": "yae-miko-genshin,more_details",  
  "clip_skip": "2",  
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
RequestBody body = RequestBody.create(mediaType, "{\n     \"key\": \"\",\n  \"controlnet_model\": \"openpose,canny,face_detector\",\n  \"controlnet_type\" :\"openpose\",\n  \"model_id\": \"midjourney\",\n  \"auto_hint\": \"yes\",\n  \"guess_mode\" : \"yes\",\n  \"prompt\": \"human model doing photoshoot, ultra realistic face, ultra high resolution, 4K image\",\n  \"negative_prompt\": null,\n  \"control_image\": \"https://huggingface.co/takuma104/controlnet_dev/resolve/main/gen_compare/control_images/converted/control_human_openpose.png\",\n  \"init_image\": \"https://cdn.stablediffusionapi.com/generations/0-4957a91a-a45e-459e-b4cd-b3ca4013b847.png\",\n  \"mask_image\": null,\n  \"width\": \"512\",\n  \"height\": \"512\",\n  \"samples\": \"1\",\n  \"scheduler\": \"UniPCMultistepScheduler\",\n  \"num_inference_steps\": \"30\",\n  \"safety_checker\": \"no\",\n  \"enhance_prompt\": \"yes\",\n  \"guidance_scale\": 7.5,\n  \"controlnet_conditioning_scale\": 0.7,\n  \"strength\": 0.55,\n  \"lora_model\": \"yae-miko-genshin,more_details\",\n  \"clip_skip\": \"2\",\n  \"tomesd\": \"yes\",\n  \"use_karras_sigmas\": \"yes\",\n  \"vae\": null,\n  \"lora_strength\": null,\n  \"embeddings_model\": null,\n  \"seed\": null,\n  \"webhook\": null,\n  \"track_id\": null\n}");  
Request request = new Request.Builder()  
  .url("https://stablediffusionapi.com/api/v5/controlnet")  
  .method("POST", body)  
  .addHeader("Content-Type", "application/json")  
  .build();  
Response response = client.newCall(request).execute();  

```
### Response[â](#response "Direct link to Response")


```
{  
  "status": "success",  
  "generationTime": 14.463637351989746,  
  "id": 32303444,  
  "output": [  
    "https://cdn.stablediffusionapi.com/generations/0-0dcf98b7-c397-4536-bd56-f0bf69c6ec1a.png"  
  ],  
  "meta": {  
    "prompt": "mdjrny-v4 style human model doing photoshoot, ultra realistic face, ultra high resolution, 4K image",  
    "model_id": "midjourney",  
    "controlnet_model": "openpose,canny,face_detector",  
    "controlnet_type": "openpose",  
    "negative_prompt": "",  
    "scheduler": "UniPCMultistepScheduler",  
    "safety_checker": "no",  
    "auto_hint": "yes",  
    "guess_mode": "yes",  
    "strength": "1",  
    "W": 512,  
    "H": 512,  
    "guidance_scale": 7.5,  
    "controlnet_conditioning_scale": "0.7",  
    "seed": 465647573,  
    "multi_lingual": "no",  
    "use_karras_sigmas": "yes",  
    "tomesd": "yes",  
    "init_image": "https://cdn.stablediffusionapi.com/generations/0-4957a91a-a45e-459e-b4cd-b3ca4013b847.png",  
    "mask_image": null,  
    "control_image": "https://huggingface.co/takuma104/controlnet_dev/resolve/main/gen_compare/control_images/converted/control_human_openpose.png",  
    "vae": null,  
    "steps": 20,  
    "full_url": "no",  
    "upscale": "no",  
    "n_samples": 1,  
    "embeddings": null,  
    "lora": "yae-miko-genshin,more_details",  
    "lora_strength": 1,  
    "temp": "no",  
    "base64": "no",  
    "clip_skip": 2,  
    "file_prefix": "0dcf98b7-c397-4536-bd56-f0bf69c6ec1a.png"  
  }  
}  

```
[PreviousControlNet Main](/docs/controlnet/controlnet-main)[NextVoice Cloning](/docs/category/voice-cloning)* [Overview](#overview)
* [Request](#request)
* [Body Attributes](#body-attributes)
	+ [Models](#models)
	+ [Schedulers](#schedulers)
* [Example](#example)
	+ [Body](#body)
	+ [Request](#request-1)
	+ [Response](#response)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



