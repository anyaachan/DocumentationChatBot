




Background Removal and Create mask Endpoint \| Stable Diffusion API Documentation








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
* Remove Background
On this pageBackground Removal and Create mask Endpoint
===========================================

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

This endpoint removes background from image and create mask.

![Image to image endpoint result](/docs/assets/images/remove-background-51f31d4f7ebf7b7349274e3e548bf3bd.png)Request[â](#request "Direct link to Request")
-----------------------------------------------


```
--request POST 'https://stablediffusionapi.com/api/v5/removebg_mask' \  

```
Make a `POST` request to <https://stablediffusionapi.com/api/v5/removebg_mask> endpoint and pass the required parameters as a request body to the endpoint. 

Body Attributes[â](#body-attributes "Direct link to Body Attributes")
-----------------------------------------------------------------------



| Parameter | Description |
| --- | --- |
| **key** | Your API Key used for request authorization |
| **image** | url of the image you want to remove and create its mask |
| **alpha\_matting** | Whether to perform alpha matting. It accepts `true` or `false`. Default is `false` |
| **post\_process\_mask** | To post process the mask image. It accepts `true` or `false`. Default is `false` |
| **only\_mask** | Whether to return only mask image or not. It accept `true` or `false`. Default is `false` |
| **seed** | Seed is used to reproduce results, same seed will give you same image in return again. Pass *null* for a random number. |
| **alpha\_matting\_foreground\_threshold** | Optional. Threshold for alpha matting foreground. Default is 240 |
| **alpha\_matting\_background\_threshold** | Optional. Threshold for alpha matting foreground. Default is 20 |
| **alpha\_matting\_erode\_size** | Optional. Erode size for alpha matting. Default is 5\. |
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
    "image":"https://huggingface.co/datasets/diffusers/test-arrays/resolve/main/stable_diffusion_inpaint/boy.png",  
    "post_process_mask": false,  
    "only_mask": false,  
    "alpha_matting":false,  
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
    "seed":12345,  
    "image":"https://huggingface.co/datasets/diffusers/test-arrays/resolve/main/stable_diffusion_inpaint/boy.png",  
    "post_process_mask": false,  
    "only_mask": false,  
    "alpha_matting":false,  
    "webhook": null,  
    "track_id": null     
});  
  
var requestOptions = {  
  method: 'POST',  
  headers: myHeaders,  
  body: raw,  
  redirect: 'follow'  
};  
  
fetch("https://stablediffusionapi.com/api/v5/removebg_mask", requestOptions)  
  .then(response => response.text())  
  .then(result => console.log(result))  
  .catch(error => console.log('error', error));  

```

```
<?php  
  
$payload = [  
    "key" =>"",  
    "seed" =>12345,  
    "image" => "https://huggingface.co/datasets/diffusers/test-arrays/resolve/main/stable_diffusion_inpaint/boy.png",  
    "post_process_mask" => false,  
    "only_mask" => false,  
    "alpha_matting" =>false,  
    "webhook" => null,  
    "track_id" => null    
];  
  
$curl = curl_init();  
  
curl_setopt_array($curl, array(  
  CURLOPT_URL => 'https://stablediffusionapi.com/api/v5/removebg_mask',  
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
  'url': 'https://stablediffusionapi.com/api/v5/removebg_mask',  
  'headers': {  
    'Content-Type': 'application/json'  
  },  
  body: JSON.stringify({  
    "key":"",  
    "seed":12345,  
    "image":"https://huggingface.co/datasets/diffusers/test-arrays/resolve/main/stable_diffusion_inpaint/boy.png",  
    "post_process_mask": false,  
    "only_mask": false,  
    "alpha_matting":false,  
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
  
url = "https://stablediffusionapi.com/api/v5/removebg_mask"  
  
payload = json.dumps({  
    "key":"",  
    "seed":12345,  
    "image":"https://img.freepik.com/premium-photo/red-roses-rose-petals-white-backgroundvalentines-day-concept_167862-5720.jpg,https://huggingface.co/datasets/diffusers/test-arrays/resolve/main/stable_diffusion_inpaint/boy.png",  
    "post_process_mask": false,  
    "only_mask": false,  
    "alpha_matting":false,  
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
    RequestBody body = RequestBody.create(mediaType, "{\n     \"key\":\"\",\n    \"seed\":12345,\n    \"image\":\"https://huggingface.co/datasets/diffusers/test-arrays/resolve/main/stable_diffusion_inpaint/boy.png\",\n    \"post_process_mask\": false,\n    \"only_mask\": false,\n    \"alpha_matting\":false,\n    \"webhook\": null,\n    \"track_id\": null\n}");  
    Request request = new Request.Builder()  
      .url("https://stablediffusionapi.com/api/v5/removebg_mask")  
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
    "generationTime": 4.726040601730347,  
    "id": 558,  
    "output": [  
        "https://pub-3626123a908346a7a8be8d9295f44e26.r2.dev/generations/2a231897-80f8-4cdd-82bf-e0d43e82462d.png.png"  
    ],  
    "meta": {  
        "alpha_matting": "0",  
        "alpha_matting_background_threshold": 20,  
        "alpha_matting_erode_size": 5,  
        "alpha_matting_foreground_threshold": 240,  
        "base64": "no",  
        "file_prefix": "2a231897-80f8-4cdd-82bf-e0d43e82462d.png",  
        "image_url": "https://huggingface.co/datasets/diffusers/test-arrays/resolve/main/stable_diffusion_inpaint/boy.png",  
        "instant_response": "no",  
        "only_mask": false,  
        "outdir": "out",  
        "post_process_mask": "0",  
        "seed": 1,  
        "temp": "no"  
    }  
}  
  

```
[PreviousImage Guided Editing](/docs/image-editing/pix2pix)[NextSuper Resolution](/docs/image-editing/super-resolution)* [Overview](#overview)
* [Request](#request)
* [Body Attributes](#body-attributes)
* [Example](#example)
	+ [Body](#body)
	+ [Request](#request-1)
	+ [Response](#response)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



