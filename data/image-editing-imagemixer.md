




Image Mixer Endpoint \| Stable Diffusion API Documentation








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
* Image Mixer
On this pageImage Mixer Endpoint
====================

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

This endpoint generates image by mixing multiple images.

Together with the image you can add your description of the desired result by passing prompt and negative prompt.

Request[â](#request "Direct link to Request")
-----------------------------------------------


```
--request POST 'https://stablediffusionapi.com/api/v5/img_mixer' \  

```
Make a `POST` request to <https://stablediffusionapi.com/api/v5/img_mixer> endpoint and pass the required parameters as a request body to the endpoint. 

Body Attributes[â](#body-attributes "Direct link to Body Attributes")
-----------------------------------------------------------------------



| Parameter | Description |
| --- | --- |
| **key** | Your API Key used for request authorization |
| **prompt** | Text prompt with description of the things you want in the image to be generated |
| **negative\_prompt** | Items you don't want in the image |
| **init\_image** | comma separated image urls of images to mix |
| **width** | Max Height: Width: 1024x1024 |
| **height** | Max Height: Width: 1024x1024 |
| **steps** | Number of denoising steps (minimum: 1; maximum: 50\) |
| **guidance\_scale** | Scale for classifier\-free guidance (minimum: 1; maximum: 20\) |
| **init\_image\_weights** | weigth of the images being passed separated by comma |
| **seed** | Seed is used to reproduce results, same seed will give you same image in return again. Pass *null* for a random number. |
| **samples** | Number of images to be returned in response. The maximum value is 4\. |
| **guidance\_scale** | Scale for classifier\-free guidance (minimum: 1; maximum: 20\) |
| **webhook** | Set an URL to get a POST API call once the image generation is complete. |
| **track\_id** | This ID is returned in the response to the webhook API call. This will be used to identify the webhook request. |

Example[â](#example "Direct link to Example")
-----------------------------------------------

### Body[â](#body "Direct link to Body")

Body
```
{  
    "key":"",  
    "seed":12345,  
    "init_image":"https://img.freepik.com/premium-photo/red-roses-rose-petals-white-backgroundvalentines-day-concept_167862-5720.jpg,https://huggingface.co/datasets/diffusers/test-arrays/resolve/main/stable_diffusion_inpaint/boy.png",  
    "prompt":"rose man",  
    "negative_prompt":"A polluted city",  
    "init_image_weights":"0.5,0.7",  
    "width":800,  
    "height":600,  
    "guidance_scale":10,  
    "steps":100,  
    "samples":1  
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
    "init_image":"https://img.freepik.com/premium-photo/red-roses-rose-petals-white-backgroundvalentines-day-concept_167862-5720.jpg,https://huggingface.co/datasets/diffusers/test-arrays/resolve/main/stable_diffusion_inpaint/boy.png",  
    "seed":"12345",  
    "prompt":"rose man",  
    "negative_prompt":"A polluted city",  
    "init_image_weights":"0.5,0.7",  
    "width":800,  
    "height":600,  
    "guidance_scale":10,  
    "steps":100,  
    "samples":1,  
    "webhook": null,  
    "track_id": null    
});  
  
var requestOptions = {  
  method: 'POST',  
  headers: myHeaders,  
  body: raw,  
  redirect: 'follow'  
};  
  
fetch("https://stablediffusionapi.com/api/v5/img_mixer", requestOptions)  
  .then(response => response.text())  
  .then(result => console.log(result))  
  .catch(error => console.log('error', error));  

```

```
<?php  
  
$payload = [  
    "key" => "",   
    "init_image" => "https://img.freepik.com/premium-photo/red-roses-rose-petals-white-backgroundvalentines-day-concept_167862-5720.jpg,https://huggingface.co/datasets/diffusers/test-arrays/resolve/main/stable_diffusion_inpaint/boy.png",  
    "seed" => "12345",  
    "prompt" => "rose man",  
    "negative_prompt" => "A polluted city",  
    "init_image_weights" => "0.5,0.7",  
    "width" => 800,  
    "height" => 600,  
    "guidance_scale" => 10,  
    "steps" => 100,  
    "samples" => 1,  
    "webhook" => null,  
    "track_id" => null    
];  
  
$curl = curl_init();  
  
curl_setopt_array($curl, array(  
  CURLOPT_URL => 'https://stablediffusionapi.com/api/v5/img_mixer',  
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
  'url': 'https://stablediffusionapi.com/api/v5/img_mixer',  
  'headers': {  
    'Content-Type': 'application/json'  
  },  
  body: JSON.stringify({  
    "key": "",  
    "init_image":"https://img.freepik.com/premium-photo/red-roses-rose-petals-white-backgroundvalentines-day-concept_167862-5720.jpg,https://huggingface.co/datasets/diffusers/test-arrays/resolve/main/stable_diffusion_inpaint/boy.png",  
    "seed":"12345",  
    "prompt":"rose man",  
    "negative_prompt":"A polluted city",  
    "init_image_weights":"0.5,0.7",  
    "width":800,  
    "height":600,  
    "guidance_scale":10,  
    "steps":100,  
    "samples":1,  
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
  
url = "https://stablediffusionapi.com/api/v5/img_mixer"  
  
payload = json.dumps({  
  "key": "",  
  "init_image":"https://img.freepik.com/premium-photo/red-roses-rose-petals-white-backgroundvalentines-day-concept_167862-5720.jpg,https://huggingface.co/datasets/diffusers/test-arrays/resolve/main/stable_diffusion_inpaint/boy.png",  
 "seed":"12345",  
 "prompt":"rose man",  
 "negative_prompt":"A polluted city",  
 "init_image_weights":"0.5,0.7",  
 "width":800,  
 "height":600,  
 "guidance_scale":10,  
 "steps":100,  
 "samples":1    
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
RequestBody body = RequestBody.create(mediaType, "{\n    \"key\":\"",\n    \"seed\":12345,\n    \"init_image\":\"https://img.freepik.com/premium-photo/red-roses-rose-petals-white-backgroundvalentines-day-concept_167862-5720.jpg,https://huggingface.co/datasets/diffusers/test-arrays/resolve/main/stable_diffusion_inpaint/boy.png\",\n    \"prompt\":\"rose man\",\n    \"negative_prompt\":\"A polluted city\",\n    \"init_image_weights\":\"0.5,0.7\",\n    \"width\":800,\n    \"height\":600,\n    \"guidance_scale\":10,\n    \"steps\":100,\n    \"samples\":1\n    \n}");  
Request request = new Request.Builder()  
  .url("https://stablediffusionapi.com/api/v5/img_mixer")  
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
    "generationTime": 19.260561227798462,  
    "id": 349,  
    "output": [  
        "https://cdn2.stablediffusionapi.com/generations/8aa6cb76-0c62-4ebc-a29a-3a3e3727bc88-0.png"  
    ],  
    "meta": {  
        "H": 600,  
        "W": 800,  
        "file_prefix": "8aa6cb76-0c62-4ebc-a29a-3a3e3727bc88",  
        "guidance_scale": 10,  
        "init_image": "https://img.freepik.com/premium-photo/red-roses-rose-petals-white-backgroundvalentines-day-concept_167862-5720.jpg,https://huggingface.co/datasets/diffusers/test-arrays/resolve/main/stable_diffusion_inpaint/boy.png",  
        "init_image_weights": "0.5,0.7",  
        "n_samples": 1,  
        "negative_prompt": "A polluted city",  
        "outdir": "out",  
        "prompt": "rose man",  
        "seed": 12345,  
        "steps": 100  
    }  
}  
  

```
[PreviousDepth to Image](/docs/image-editing/depth2img)[NextImage Guided Editing](/docs/image-editing/pix2pix)* [Overview](#overview)
* [Request](#request)
* [Body Attributes](#body-attributes)
* [Example](#example)
	+ [Body](#body)
	+ [Request](#request-1)
	+ [Response](#response)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



