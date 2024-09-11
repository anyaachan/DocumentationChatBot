




Mixture Canvas Endpoint \| Stable Diffusion API Documentation








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
* [Dreambooth Sandbox](/docs/category/dreambooth-sandbox)
* [Image Editing](/docs/category/image-editing)
	+ [API Overview](/docs/image-editing/overview)
	+ [Outpainting](/docs/image-editing/outpainting)
	+ [Blip Diffusion](/docs/image-editing/blip-diffusion)
	+ [Magic Mix](/docs/image-editing/magic-mix)
	+ [Depth to Image](/docs/image-editing/depth2img)
	+ [Image Mixer](/docs/image-editing/imagemixer)
	+ [Image Guided Editing](/docs/image-editing/pix2pix)
	+ [Remove Background](/docs/image-editing/removebg-createmask)
	+ [Super Resolution](/docs/image-editing/super-resolution)
	+ [Mixture Canvas](/docs/image-editing/mixture-canvas)
	+ [Multiview](/docs/image-editing/multiview)
	+ [Fashion (Beta)](/docs/image-editing/fashion)
* [Text To 3D](/docs/category/text-to-3d)
* [Uncensored Chat](/docs/uncensored-chat)
* [A1111 Schedulers](/docs/a1111schedulers)
* [FAQ](/docs/faq)
* [Postman Collection](https://documenter.getpostman.com/view/18679074/2s83zdwReZ)
* [Support](https://discord.gg/UxqnDu7j3r)
* 
* 
* [Image Editing](/docs/category/image-editing)
* Mixture Canvas
On this pageMixture Canvas Endpoint
=======================

* [v5/outpainting](/docs/image-editing/outpainting)
* [v5/blip\_diffusion](/docs/image-editing/blip-diffusion)
* [v5/magic\_mix](/docs/image-editing/magic-mix)
* [v5/depth2img](/docs/image-editing/depth2img)
* [v5/image\_guided\_editing](/docs/image-editing/pix2pix)
* [v5/removebg\_createmask](/docs/image-editing/removebg-createmask)
* [v5/super\_resolution](/docs/image-editing/super-resolution)
* [v5/image\_mixer](/docs/image-editing/imagemixer)
* [v5/mixture\-canvas](/docs/image-editing/mixture-canvas)
* [v5/multiview](/docs/image-editing/multiview)
* [v5/fashion](/docs/image-editing/fashion)
Overview[â](#overview "Direct link to Overview")
--------------------------------------------------

This endpoint allow you to add canva to an image and fill the canva with prompt description

Request[â](#request "Direct link to Request")
-----------------------------------------------


```
--request POST 'https://stablediffusionapi.com/api/v5/mixture_canvas' \  

```
Make a `POST` request to <https://stablediffusionapi.com/api/v5/mixture_canvas> endpoint and pass the required parameters as a request body to the endpoint. 

Body Attributes[â](#body-attributes "Direct link to Body Attributes")
-----------------------------------------------------------------------



| Parameter | Description |
| --- | --- |
| **key** | Your API Key used for request authorization |
| **prompt** | Text prompt with description of the things you want in the image to be generated |
| **negative\_prompt** | Items you don't want in the image |
| **image** | url of the image to outpaint |
| **width** | This is the canvas width: Default `800` |
| **height** | This is the canvas height: Default `360` |
| **guidance\_scale** | Optional. Scale for classifier\-free guidance (minimum: 1; maximum: 20\). Default is `8` |
| **strength** | Optional. Prompt strength when using image. 1\.0 corresponds to full destruction of information in the image. |
| **num\_inference\_steps** | Optional. Number of denoising steps. Default `20` |
| **mix\_factor** | Optional. Mix factor for the task. Default is `0.5` |
| **pos\_y1** | Optional. Y1 position for the outpainting. Default is `448` |
| **pos\_y2** | Optional. Y2 position for the outpainting. Default is `800` |
| **pos\_x1** | Optional. X1 position for the outpainting. Default is `0` |
| **pos\_x2** | Optional. X2 position for the outpainting. Default is `352` |
| **seed** | Seed is used to reproduce results, same seed will give you same image in return again. Pass *null* for a |
| **webhook** | Set an URL to get a POST API call once the image generation is complete. |
| **track\_id** | This ID is returned in the response to the webhook API call. This will be used to identify the webhook request. |

Example[â](#example "Direct link to Example")
-----------------------------------------------

### Body[â](#body "Direct link to Body")

Body
```
{  
    "key":"",  
    "image":"https://camo.githubusercontent.com/5591434c42714807553e83644a191816cdf39100648f8d94b28a149dc0bc5cc7/68747470733a2f2f68756767696e67666163652e636f2f64617461736574732f6b616469726e61722f6469666675736572735f726561646d655f696d616765732f7265736f6c76652f6d61696e2f696e7075745f696d6167652e706e67",  
    "prompt":"best quality, masterpiece, WLOP, sakimichan, art contest winner on pixiv, 8K, intricate details, wet effects, rain drops, ethereal, mysterious, futuristic, UHD, HDR, cinematic lighting, in a beautiful forest, rainy day, award winning, trending on artstation, beautiful confident cheerful young woman, wearing a futuristic sleeveless dress, ultra beautiful detailed  eyes, hyper-detailed face, complex,  perfect, model,  textured,  chiaroscuro, professional make-up, realistic, figure in frame,",  
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
    "key":"",  
    "image":"https://camo.githubusercontent.com/5591434c42714807553e83644a191816cdf39100648f8d94b28a149dc0bc5cc7/68747470733a2f2f68756767696e67666163652e636f2f64617461736574732f6b616469726e61722f6469666675736572735f726561646d655f696d616765732f7265736f6c76652f6d61696e2f696e7075745f696d6167652e706e67",  
    "prompt":"best quality, masterpiece, WLOP, sakimichan, art contest winner on pixiv, 8K, intricate details, wet effects, rain drops, ethereal, mysterious, futuristic, UHD, HDR, cinematic lighting, in a beautiful forest, rainy day, award winning, trending on artstation, beautiful confident cheerful young woman, wearing a futuristic sleeveless dress, ultra beautiful detailed  eyes, hyper-detailed face, complex,  perfect, model,  textured,  chiaroscuro, professional make-up, realistic, figure in frame,",  
    "webhook": null,  
    "track_id": null   
});  
  
var requestOptions = {  
  method: 'POST',  
  headers: myHeaders,  
  body: raw,  
  redirect: 'follow'  
};  
  
fetch("https://stablediffusionapi.com/api/v5/mixture_canvas", requestOptions)  
  .then(response => response.text())  
  .then(result => console.log(result))  
  .catch(error => console.log('error', error));  

```

```
<?php  
  
$payload = [  
    "key" => "",  
    "image" => "https://camo.githubusercontent.com/5591434c42714807553e83644a191816cdf39100648f8d94b28a149dc0bc5cc7/68747470733a2f2f68756767696e67666163652e636f2f64617461736574732f6b616469726e61722f6469666675736572735f726561646d655f696d616765732f7265736f6c76652f6d61696e2f696e7075745f696d6167652e706e67",  
    "prompt" => "best quality, masterpiece, WLOP, sakimichan, art contest winner on pixiv, 8K, intricate details, wet effects, rain drops, ethereal, mysterious, futuristic, UHD, HDR, cinematic lighting, in a beautiful forest, rainy day, award winning, trending on artstation, beautiful confident cheerful young woman, wearing a futuristic sleeveless dress, ultra beautiful detailed  eyes, hyper-detailed face, complex,  perfect, model,  textured,  chiaroscuro, professional make-up, realistic, figure in frame,",  
    "webhook" => null,  
    "track_id" => null   
];  
  
$curl = curl_init();  
  
curl_setopt_array($curl, array(  
  CURLOPT_URL => 'https://stablediffusionapi.com/api/v5/mixture_canvas',  
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
  'url': 'https://stablediffusionapi.com/api/v5/mixture_canvas',  
  'headers': {  
    'Content-Type': 'application/json'  
  },  
  body: JSON.stringify({  
    "key":"",  
    "image":"https://camo.githubusercontent.com/5591434c42714807553e83644a191816cdf39100648f8d94b28a149dc0bc5cc7/68747470733a2f2f68756767696e67666163652e636f2f64617461736574732f6b616469726e61722f6469666675736572735f726561646d655f696d616765732f7265736f6c76652f6d61696e2f696e7075745f696d6167652e706e67",  
    "prompt":"best quality, masterpiece, WLOP, sakimichan, art contest winner on pixiv, 8K, intricate details, wet effects, rain drops, ethereal, mysterious, futuristic, UHD, HDR, cinematic lighting, in a beautiful forest, rainy day, award winning, trending on artstation, beautiful confident cheerful young woman, wearing a futuristic sleeveless dress, ultra beautiful detailed  eyes, hyper-detailed face, complex,  perfect, model,  textured,  chiaroscuro, professional make-up, realistic, figure in frame,",  
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
  
url = "https://stablediffusionapi.com/api/v5/mixture_canvas"  
  
payload = json.dumps({  
    "key":"",  
    "image":"https://camo.githubusercontent.com/5591434c42714807553e83644a191816cdf39100648f8d94b28a149dc0bc5cc7/68747470733a2f2f68756767696e67666163652e636f2f64617461736574732f6b616469726e61722f6469666675736572735f726561646d655f696d616765732f7265736f6c76652f6d61696e2f696e7075745f696d6167652e706e67",  
    "prompt":"best quality, masterpiece, WLOP, sakimichan, art contest winner on pixiv, 8K, intricate details, wet effects, rain drops, ethereal, mysterious, futuristic, UHD, HDR, cinematic lighting, in a beautiful forest, rainy day, award winning, trending on artstation, beautiful confident cheerful young woman, wearing a futuristic sleeveless dress, ultra beautiful detailed  eyes, hyper-detailed face, complex,  perfect, model,  textured,  chiaroscuro, professional make-up, realistic, figure in frame,",  
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
  RequestBody body = RequestBody.create(mediaType, "{\n    \"key\":\"bXagUMkX2VTOTc1Z2TAoU0Yh39N1TftQ8BmQCQzKM4Ng5G5qmufiCzX6Arnn\",\n    \"prompt\": \"best quality, masterpiece, WLOP, sakimichan, art contest winner on pixiv, 8K, intricate details, wet effects, rain drops, ethereal, mysterious, futuristic, UHD, HDR, cinematic lighting, in a beautiful forest, rainy day, award winning, trending on artstation, beautiful confident cheerful young woman, wearing a futuristic sleeveless dress, ultra beautiful detailed  eyes, hyper-detailed face, complex,  perfect, model,  textured,  chiaroscuro, professional make-up, realistic, figure in frame,\",\n    \"image\":\"https://camo.githubusercontent.com/5591434c42714807553e83644a191816cdf39100648f8d94b28a149dc0bc5cc7/68747470733a2f2f68756767696e67666163652e636f2f64617461736574732f6b616469726e61722f6469666675736572735f726561646d655f696d616765732f7265736f6c76652f6d61696e2f696e7075745f696d6167652e706e67\",\n     \"num_inference_steps\":20,\n    \"strength\":1.0\n}");  
  Request request = new Request.Builder()  
    .url("https://stablediffusionapi.com/api/v5/mixture_canvas")  
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
    "generationTime": 12.331510066986084,  
    "id": 514,  
    "output": [  
        "https://pub-3626123a908346a7a8be8d9295f44e26.r2.dev/generations/07eb4e9b-3248-4789-b87f-44a7f64d77fd.png"  
    ],  
    "meta": {  
        "canvas_height": 800,  
        "canvas_width": 360,  
        "file_prefix": "07eb4e9b-3248-4789-b87f-44a7f64d77fd",  
        "guidance_scale": 8,  
        "image": "https://camo.githubusercontent.com/5591434c42714807553e83644a191816cdf39100648f8d94b28a149dc0bc5cc7/68747470733a2f2f68756767696e67666163652e636f2f64617461736574732f6b616469726e61722f6469666675736572735f726561646d655f696d616765732f7265736f6c76652f6d61696e2f696e7075745f696d6167652e706e67",  
        "negative_prompt": "low quality",  
        "outdir": "out",  
        "pos_x1": 0,  
        "pos_x2": 352,  
        "pos_y1": 448,  
        "pos_y2": 800,  
        "prompt": "best quality, masterpiece, WLOP, sakimichan, art contest winner on pixiv, 8K, intricate details, wet effects, rain drops, ethereal, mysterious, futuristic, UHD, HDR, cinematic lighting, in a beautiful forest, rainy day, award winning, trending on artstation, beautiful confident cheerful young woman, wearing a futuristic sleeveless dress, ultra beautiful detailed  eyes, hyper-detailed face, complex,  perfect, model,  textured,  chiaroscuro, professional make-up, realistic, figure in frame,",  
        "seed": 3843097097,  
        "steps": 100,  
        "strength": 1  
    }  
}  

```
[PreviousSuper Resolution](/docs/image-editing/super-resolution)[NextMultiview](/docs/image-editing/multiview)* [Overview](#overview)
* [Request](#request)
* [Body Attributes](#body-attributes)
* [Example](#example)
	+ [Body](#body)
	+ [Request](#request-1)
	+ [Response](#response)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



