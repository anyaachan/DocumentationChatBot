




Text to Image Endpoint \| Stable Diffusion API Documentation








[Skip to main content](#docusaurus_skipToContent_fallback)[![Stable Diffusion Logo](/docs/img/SD-logo.png)![Stable Diffusion Logo](/docs/img/SD-logo.png)](https://stablediffusionapi.com)[Enterprise](https://stablediffusionapi.com/enterprise)[Pricing](https://stablediffusionapi.com/#pricing)[Blog](https://stablediffusionapi.com/blog)[Docs](https://stablediffusionapi.com/docs)[Playground](https://stablediffusionapi.com/playground)[Models](https://stablediffusionapi.com/models)[API Catalogue](https://stablediffusionapi.com/catalogue)* [Getting Started](/docs/)
* [Stable Diffusion API](/docs/category/stable-diffusion-api)
	+ [API Overview](/docs/stable-diffusion-api/overview)
	+ [Text to Image](/docs/stable-diffusion-api/text2img)
	+ [Image to Image](/docs/stable-diffusion-api/img2img)
	+ [Inpainting](/docs/stable-diffusion-api/inpainting)
	+ [Fetch Queued Images](/docs/stable-diffusion-api/fetchqueimg)
	+ [System Load](/docs/stable-diffusion-api/system-load)
* [Train Model](/docs/category/train-model)
* [Community Models API](/docs/category/community-models-api)
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
* [Stable Diffusion API](/docs/category/stable-diffusion-api)
* Text to Image
On this pageText to Image Endpoint
======================

* [text2img](/docs/stable-diffusion-api/text2img)
* [img2img](/docs/stable-diffusion-api/img2img)
* [inpaint](/docs/stable-diffusion-api/inpainting)
* [fetch](/docs/stable-diffusion-api/fetchqueimg)
* [system\_load](/docs/stable-diffusion-api/system-load)
Overview[â](#overview "Direct link to Overview")
--------------------------------------------------

Stable Diffusion V3 APIs Text2Image API generates an image from a text prompt.

This endpoint generates and returns an image from a text passed in the request body.

![Text to image endpoint result](/docs/assets/images/txt2img-action-sm-76f78ddd2eac261716ae30ad397f8475.png)Request[â](#request "Direct link to Request")
-----------------------------------------------


```
--request POST 'https://stablediffusionapi.com/api/v3/text2img' \  

```
Make a `POST` request to <https://stablediffusionapi.com/api/v3/text2img> endpoint and pass the required parameters as a request body. 

Watch the how\-to video to see it in action.

Body Attributes[â](#body-attributes "Direct link to Body Attributes")
-----------------------------------------------------------------------



| Parameter | Description |
| --- | --- |
| **key** | Your API Key used for request authorization. |
| **prompt** | Text prompt with description of the things you want in the image to be generated. |
| **negative\_prompt** | Items you don't want in the image. |
| **width** | Max Height: Width: 1024x1024\. |
| **height** | Max Height: Width: 1024x1024\. |
| **samples** | Number of images to be returned in response. The maximum value is 4\. |
| **num\_inference\_steps** | Number of denoising steps. Available values: 21, 31, 41, 51\. |
| **safety\_checker** | A checker for NSFW images. If such an image is detected, it will be replaced by a blank image. |
| **enhance\_prompt** | Enhance prompts for better results; **default**: yes, **options**: yes/no. |
| **seed** | Seed is used to reproduce results, same seed will give you same image in return again. Pass *null* for a random number. |
| **guidance\_scale** | Scale for classifier\-free guidance (minimum: 1; maximum: 20\). |
| **multi\_lingual** | Allow multi lingual prompt to generate images. Use "no" for the default English. |
| **panorama** | Set this parameter to "yes" to generate a panorama image. |
| **self\_attention** | If you want a high quality image, set this parameter to "yes". In this case the image generation will take more time. |
| **upscale** | Set this parameter to "yes" if you want to upscale the given image resolution two times (2x). If the requested resolution is 512 x 512 px, the generated image will be 1024 x 1024 px. |
| **embeddings\_model** | This is used to pass an embeddings model (embeddings\_model\_id). |
| **webhook** | Set an URL to get a POST API call once the image generation is complete. |
| **track\_id** | This ID is returned in the response to the webhook API call. This will be used to identify the webhook request. |

### Multi\_lingual Supported Languages[â](#multi_lingual-supported-languages "Direct link to Multi_lingual Supported Languages")

If you use a language different from English in you text prompts, pass the "multi\_lingual" parameter with "yes" value in the request body. This will trigger an automatic language detection and translation during the processing of your request.

The following languages are supported:

Arabic (ar\_AR), Czech (cs\_CZ), German (de\_DE), English (en\_XX), Spanish (es\_XX), Estonian (et\_EE), Finnish (fi\_FI), French (fr\_XX), Gujarati (gu\_IN), Hindi (hi\_IN), Italian (it\_IT), Japanese (ja\_XX), Kazakh (kk\_KZ), Korean (ko\_KR), Lithuanian (lt\_LT), Latvian (lv\_LV), Burmese (my\_MM), Nepali (ne\_NP), Dutch (nl\_XX), Romanian (ro\_RO), Russian (ru\_RU), Sinhala (si\_LK), Turkish (tr\_TR), Vietnamese (vi\_VN), Chinese (zh\_CN), Afrikaans (af\_ZA), Azerbaijani (az\_AZ), Bengali (bn\_IN), Persian (fa\_IR), Hebrew (he\_IL), Croatian (hr\_HR), Indonesian (id\_ID), Georgian (ka\_GE), Khmer (km\_KH), Macedonian (mk\_MK), Malayalam (ml\_IN), Mongolian (mn\_MN), Marathi (mr\_IN), Polish (pl\_PL), Pashto (ps\_AF), Portuguese (pt\_XX), Swedish (sv\_SE), Swahili (sw\_KE), Tamil (ta\_IN), Telugu (te\_IN), Thai (th\_TH), Tagalog (tl\_XX), Ukrainian (uk\_UA), Urdu (ur\_PK), Xhosa (xh\_ZA), Galician (gl\_ES), Slovene (sl\_SI)

Example[â](#example "Direct link to Example")
-----------------------------------------------

### Body[â](#body "Direct link to Body")

Body
```
{  
  "key": "",  
  "prompt": "ultra realistic close up portrait ((beautiful pale cyberpunk female with heavy black eyeliner))",  
  "negative_prompt": null,  
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
  "prompt": "ultra realistic close up portrait ((beautiful pale cyberpunk female with heavy black eyeliner))",  
  "negative_prompt": null,  
  "width": "512",  
  "height": "512",  
  "samples": "1",  
  "num_inference_steps": "20",  
  "seed": null,  
  "guidance_scale": 7.5,  
  "safety_checker": "yes",  
  "multi_lingual": "no",  
  "panorama": "no",  
  "self_attention": "no",  
  "upscale": "no",  
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
  
fetch("https://stablediffusionapi.com/api/v3/text2img", requestOptions)  
  .then(response => response.text())  
  .then(result => console.log(result))  
  .catch(error => console.log('error', error));  

```

```
<?php  
  
$payload = [  
  "key" => "",   
  "prompt" => "ultra realistic close up portrait ((beautiful pale cyberpunk female with heavy black eyeliner))",   
  "negative_prompt" => null,   
  "width" => "512",   
  "height" => "512",   
  "samples" => "1",   
  "num_inference_steps" => "20",   
  "seed" => null,   
  "guidance_scale" => 7.5,   
  "safety_checker" => "yes",   
  "multi_lingual" => "no",   
  "panorama" => "no",   
  "self_attention" => "no",   
  "upscale" => "no",   
  "embeddings_model" => null,   
  "webhook" => null,   
  "track_id" => null   
];  
  
$curl = curl_init();  
  
curl_setopt_array($curl, array(  
  CURLOPT_URL => 'https://stablediffusionapi.com/api/v3/text2img',  
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
  'url': 'https://stablediffusionapi.com/api/v3/text2img',  
  'headers': {  
    'Content-Type': 'application/json'  
  },  
  body: JSON.stringify({  
    "key": "",  
    "prompt": "ultra realistic close up portrait ((beautiful pale cyberpunk female with heavy black eyeliner))",  
    "negative_prompt": null,  
    "width": "512",  
    "height": "512",  
    "samples": "1",  
    "num_inference_steps": "20",  
    "seed": null,  
    "guidance_scale": 7.5,  
    "safety_checker": "yes",  
    "multi_lingual": "no",  
    "panorama": "no",  
    "self_attention": "no",  
    "upscale": "no",  
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
  
url = "https://stablediffusionapi.com/api/v3/text2img"  
  
payload = json.dumps({  
  "key": "",  
  "prompt": "ultra realistic close up portrait ((beautiful pale cyberpunk female with heavy black eyeliner))",  
  "negative_prompt": None,  
  "width": "512",  
  "height": "512",  
  "samples": "1",  
  "num_inference_steps": "20",  
  "seed": None,  
  "guidance_scale": 7.5,  
  "safety_checker": "yes",  
  "multi_lingual": "no",  
  "panorama": "no",  
  "self_attention": "no",  
  "upscale": "no",  
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
RequestBody body = RequestBody.create(mediaType, "{\n    \"key\": \"\",\n  \"prompt\": \"ultra realistic close up portrait ((beautiful pale cyberpunk female with heavy black eyeliner))\",\n   \"negative_prompt\": null,\n  \"width\": \"512\",\n \"height\": \"512\",\n \"samples\": \"1\",\n \"num_inference_steps\": \"20\",\n \"seed\": null,\n \"guidance_scale\": 7.5,\n\"safety_checker\":\"yes\",\n  \"multi_lingual\":\"no\",\n  \"panorama\":\"no\",\n  \"self_attention\":\"no\",\n  \"upscale\":\"no\",\n \"embeddings_model\":\"no\",\n   \"webhook\": null,\n  \"track_id\": null\n}");  
Request request = new Request.Builder()  
  .url("https://stablediffusionapi.com/api/v3/text2img")  
  .method("POST", body)  
  .addHeader("Content-Type", "application/json")  
  .build();  
Response response = client.newCall(request).execute();  

```
### Response[â](#response "Direct link to Response")


```
{  
  "status": "success",  
  "generationTime": 1.3200268745422363,  
  "id": 12202888,  
  "output": [  
    "https://pub-8b49af329fae499aa563997f5d4068a4.r2.dev/generations/e5cd86d3-7305-47fc-82c1-7d1a3b130fa4-0.png"  
  ],  
  "meta": {  
    "H": 512,  
    "W": 512,  
    "enable_attention_slicing": "true",  
    "file_prefix": "e5cd86d3-7305-47fc-82c1-7d1a3b130fa4",  
    "guidance_scale": 7.5,  
    "model": "runwayml/stable-diffusion-v1-5",  
    "n_samples": 1,  
    "negative_prompt": " ((out of frame)), ((extra fingers)), mutated hands, ((poorly drawn hands)), ((poorly drawn face)), (((mutation))), (((deformed))), (((tiling))), ((naked)), ((tile)), ((fleshpile)), ((ugly)), (((abstract))), blurry, ((bad anatomy)), ((bad proportions)), ((extra limbs)), cloned face, glitchy, ((extra breasts)), ((double torso)), ((extra arms)), ((extra hands)), ((mangled fingers)), ((missing breasts)), (missing lips), ((ugly face)), ((fat)), ((extra legs))",  
    "outdir": "out",  
    "prompt": "ultra realistic close up portrait ((beautiful pale cyberpunk female with heavy black eyeliner)) DSLR photography, sharp focus, Unreal Engine 5, Octane Render, Redshift, ((cinematic lighting)), f/1.4, ISO 200, 1/160s, 8K, RAW, unedited, symmetrical balance, in-frame",  
    "revision": "fp16",  
    "safetychecker": "no",  
    "seed": 3499575229,  
    "steps": 20,  
    "vae": "stabilityai/sd-vae-ft-mse"  
  }  
}  

```
[PreviousAPI Overview](/docs/stable-diffusion-api/overview)[NextImage to Image](/docs/stable-diffusion-api/img2img)* [Overview](#overview)
* [Request](#request)
* [Body Attributes](#body-attributes)
	+ [Multi\_lingual Supported Languages](#multi_lingual-supported-languages)
* [Example](#example)
	+ [Body](#body)
	+ [Request](#request-1)
	+ [Response](#response)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



