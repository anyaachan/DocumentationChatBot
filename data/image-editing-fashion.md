




Fashion Endpoint \| Stable Diffusion API Documentation








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
* Fashion (Beta)
On this pageFashion Endpoint
================

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

This endpoint allows you to wear a cloth image sample on an existing model body. The ideal input images should have white background, fully visible model body, and the cloth should be an individual piece. 

![Image to image endpoint result](/docs/assets/images/fashion-api-e5962d0202077a68b8f56bdebb36fd5b.jpg)Request[â](#request "Direct link to Request")
-----------------------------------------------


```
--request POST 'https://stablediffusionapi.com/api/v5/fashion' \  

```
Make a `POST` request to <https://stablediffusionapi.com/api/v5/fashion> endpoint and pass the required parameters as a request body to the endpoint. 

Body Attributes[â](#body-attributes "Direct link to Body Attributes")
-----------------------------------------------------------------------



| Parameter | Description |
| --- | --- |
| **key** | Your API Key used for request authorization |
| **init\_image** | Image URL of the model to try the dress on |
| **cloth\_image** | Cloth/Dress URL for the garment to try\-on |
| **cloth\_type** | One of `upper_body`, `lower_body` or `dress`, based on where the garment is to be worn. |
| **prompt** | Text prompt with description of the things you want in the image to be generated |
| **negative\_prompt** | Items you don't want in the image |
| **width** | Width of generated images. Default: 384px. Max: 1024px |
| **height** | Height of generated images. Default: 512px. Max: 1024px |
| **num\_inference\_steps** | Number of denoising steps (minimum: 1; maximum: 50\) |
| **temp** | "yes" if you want proxy links to access images apart from normal links. Useful in case your country blocks our storage provider. Default: "no" |
| **guidance\_scale** | Scale for classifier\-free guidance (minimum: 1; maximum: 20\) |
| **webhook** | Set an URL to get a POST API call once the image generation is complete. |
| **track\_id** | This ID is returned in the response to the webhook API call. This will be used to identify the webhook request. |

Example[â](#example "Direct link to Example")
-----------------------------------------------

### Body[â](#body "Direct link to Body")

Body
```
{  
   "key": "",  
   "prompt": "A realistic photo of a model wearing a beautiful white top.",  
   "negative_prompt": "Low quality, unrealistic, bad cloth, warped cloth",  
   "init_image": "https://www.vstar.in/media/cache/350x0/catalog/product/f/0/f09632_parent_1_1653003388.jpg",  
   "cloth_image": "https://thumbs.dreamstime.com/b/plain-hollow-female-tank-top-shirt-isolated-white-background-30020169.jpg",  
   "cloth_type": "upper_body",  
   "height": 512,  
   "width": 384,  
   "guidance_scale": 8.0,  
   "num_inference_steps": 20,  
   "seed": 128915590,  
   "temp": "no",  
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
   "prompt": "A realistic photo of a model wearing a beautiful white top.",  
   "negative_prompt": "Low quality, unrealistic, bad cloth, warped cloth",  
   "init_image": "https://www.vstar.in/media/cache/350x0/catalog/product/f/0/f09632_parent_1_1653003388.jpg",  
   "cloth_image": "https://thumbs.dreamstime.com/b/plain-hollow-female-tank-top-shirt-isolated-white-background-30020169.jpg",  
   "cloth_type": "upper_body",  
   "height": 512,  
   "width": 384,  
   "guidance_scale": 8.0,  
   "num_inference_steps": 20,  
   "seed": 128915590,  
   "temp": "no",  
   "webhook": null,  
   "track_id": null   
});  
  
var requestOptions = {  
  method: 'POST',  
  headers: myHeaders,  
  body: raw,  
  redirect: 'follow'  
};  
  
fetch("https://stablediffusionapi.com/api/v5/fashion", requestOptions)  
  .then(response => response.text())  
  .then(result => console.log(result))  
  .catch(error => console.log('error', error));  

```

```
<?php  
  
$payload = [  
    "key" =>  "",  
   "prompt" => "A realistic photo of a model wearing a beautiful white top.",  
   "negative_prompt" =>  "Low quality, unrealistic, bad cloth, warped cloth",  
   "init_image" => "https://www.vstar.in/media/cache/350x0/catalog/product/f/0/f09632_parent_1_1653003388.jpg",  
   "cloth_image": "https://thumbs.dreamstime.com/b/plain-hollow-female-tank-top-shirt-isolated-white-background-30020169.jpg",  
   "cloth_type" => "upper_body",  
   "height" => 512,  
   "width" => 384,  
   "guidance_scale" => 8.0,  
   "num_inference_steps" => 20,  
   "seed" => 128915590,  
   "temp" => "no",  
   "webhook" => null,  
   "track_id" =>  null   
];  
  
$curl = curl_init();  
  
curl_setopt_array($curl, array(  
  CURLOPT_URL => 'https://stablediffusionapi.com/api/v5/fashion',  
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
  'url': 'https://stablediffusionapi.com/api/v5/fashion',  
  'headers': {  
    'Content-Type': 'application/json'  
  },  
  body: JSON.stringify({  
   "key": "",  
   "prompt": "A realistic photo of a model wearing a beautiful white top.",  
   "negative_prompt": "Low quality, unrealistic, bad cloth, warped cloth",  
   "init_image": "https://www.vstar.in/media/cache/350x0/catalog/product/f/0/f09632_parent_1_1653003388.jpg",  
   "cloth_image": "https://thumbs.dreamstime.com/b/plain-hollow-female-tank-top-shirt-isolated-white-background-30020169.jpg",  
   "cloth_type": "upper_body",  
   "height": 512,  
   "width": 384,  
   "guidance_scale": 8.0,  
   "num_inference_steps": 20,  
   "seed": 128915590,  
   "temp": "no",  
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
  
url = "https://stablediffusionapi.com/api/v5/fashion"  
  
payload = json.dumps({  
   "key": "",  
   "prompt": "A realistic photo of a model wearing a beautiful white top.",  
   "negative_prompt": "Low quality, unrealistic, bad cloth, warped cloth",  
   "init_image": "https://www.vstar.in/media/cache/350x0/catalog/product/f/0/f09632_parent_1_1653003388.jpg",  
   "cloth_image": "https://thumbs.dreamstime.com/b/plain-hollow-female-tank-top-shirt-isolated-white-background-30020169.jpg",  
   "cloth_type": "upper_body",  
   "height": 512,  
   "width": 384,  
   "guidance_scale": 8.0,  
   "num_inference_steps": 20,  
   "seed": 128915590,  
   "temp": "no",  
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
RequestBody body = RequestBody.create(mediaType, "{\n    \"key\": \"\",\n   \"prompt\": \"A realistic photo of a model wearing a beautiful white top.\",\n   \"negative_prompt\": \"Low quality, unrealistic, bad cloth, warped cloth\",\n   \"init_image\": \"https://www.vstar.in/media/cache/350x0/catalog/product/f/0/f09632_parent_1_1653003388.jpg\",\n   \"cloth_image\": \"https://thumbs.dreamstime.com/b/plain-hollow-female-tank-top-shirt-isolated-white-background-30020169.jpg\",\n   \"cloth_type\": \"upper_body\",\n   \"height\": 512,\n   \"width\": 384,\n   \"guidance_scale\": 8.0,\n   \"num_inference_steps\": 20,\n   \"seed\": 128915590,\n   \"temp\": \"no\",\n   \"webhook\": null,\n   \"track_id\": null \n}");  
Request request = new Request.Builder()  
  .url("https://stablediffusionapi.com/api/v5/fashion")  
  .method("POST", body)  
  .addHeader("Content-Type", "application/json")  
  .build();  
Response response = client.newCall(request).execute();  

```
### Response[â](#response "Direct link to Response")

Example Response
```
  
{  
    {  
    "status": "success",  
    "generationTime": 9.295560359954834,  
    "id": 658,  
    "output": [  
        "https://pub-3626123a908346a7a8be8d9295f44e26.r2.dev/generations/f32fbb02-59ba-427d-96ec-e5ce35475c8e.png"  
    ],  
    "proxy_links": [  
        "https://cdn2.stablediffusionapi.com/generations/f32fbb02-59ba-427d-96ec-e5ce35475c8e.png"  
    ],  
    "meta": {  
        "cloth": "https://thumbs.dreamstime.com/b/plain-hollow-female-tank-top-shirt-isolated-white-background-30020169.jpg",  
        "cloth_type": "upper_body",  
        "file_prefix": "f32fbb02-59ba-427d-96ec-e5ce35475c8e",  
        "guidance_scale": 8,  
        "height": 512,  
        "init_image": "https://www.vstar.in/media/cache/350x0/catalog/product/f/0/f09632_parent_1_1653003388.jpg",  
        "negative_prompt": "low quality",  
        "num_inference_steps": 20,  
        "outdir": "out",  
        "prompt": "A realistic photo of a model wearing a beautiful white top.",  
        "seed": 128915590,  
        "temp": "no",  
        "width": 384  
    }  
}  
}  
  

```
[PreviousMultiview](/docs/image-editing/multiview)[NextText To 3D](/docs/category/text-to-3d)* [Overview](#overview)
* [Request](#request)
* [Body Attributes](#body-attributes)
* [Example](#example)
	+ [Body](#body)
	+ [Request](#request-1)
	+ [Response](#response)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



