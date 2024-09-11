




Multiview Endpoint \| Stable Diffusion API Documentation








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
* Multiview
On this pageMultiview Endpoint
==================

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

This endpoint takes one input image and generates multiple views of that same image. Note that images of objects and images without a background produces better result. 

![Image to image endpoint result](/docs/assets/images/multi-view-76089629be2af1c55007edd82e40dbfd.jpg)Request[â](#request "Direct link to Request")
-----------------------------------------------


```
--request POST 'https://stablediffusionapi.com/api/v5/multiview' \  

```
Make a `POST` request to <https://stablediffusionapi.com/api/v5/multiview> endpoint and pass the required parameters as a request body to the endpoint. 

Body Attributes[â](#body-attributes "Direct link to Body Attributes")
-----------------------------------------------------------------------



| Parameter | Description |
| --- | --- |
| **key** | Your API Key used for request authorization |
| **prompt** | Text prompt with description of the things you want in the image to be generated |
| **negative\_prompt** | Items you don't want in the image |
| **image** | initial image url |
| **width** | Width of generated images. Default: 640px. Max: 1024px |
| **height** | Height of generated images. Default: 960px. Max: 1024px |
| **temp** | "yes" if you want proxy links to access images apart from normal links. Useful in case your country blocks our storage provider. Default: "no" |
| **num\_inference\_steps** | Number of denoising steps (minimum: 1; maximum: 50\) |
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
    "image":"https://pub-3626123a908346a7a8be8d9295f44e26.r2.dev/generations/0558bcce-cba0-4157-963f-9374b53d68d9.png",  
    "prompt": "make multiple images",  
    "width": 640,  
    "height":960,  
    "num_inference_steps":50,  
    "guidance_scale":4,  
    "temp":"no",  
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
    "image":"https://pub-3626123a908346a7a8be8d9295f44e26.r2.dev/generations/0558bcce-cba0-4157-963f-9374b53d68d9.png",  
    "prompt": "make multiple images",  
    "width": 640,  
    "height":960,  
    "num_inference_steps":50,  
    "guidance_scale":4,  
    "temp":"no",  
    "webhook": null,  
    "track_id": null   
});  
  
var requestOptions = {  
  method: 'POST',  
  headers: myHeaders,  
  body: raw,  
  redirect: 'follow'  
};  
  
fetch("https://stablediffusionapi.com/api/v5/multiview", requestOptions)  
  .then(response => response.text())  
  .then(result => console.log(result))  
  .catch(error => console.log('error', error));  

```

```
<?php  
  
$payload = [  
    "key" => "",  
    "seed" => 12345,  
    "image" => "https://pub-3626123a908346a7a8be8d9295f44e26.r2.dev/generations/0558bcce-cba0-4157-963f-9374b53d68d9.png",  
    "prompt" =>  "make multiple images",  
    "width" => 640,  
    "height" => 960,  
    "num_inference_steps" => 50,  
    "guidance_scale" => 4,  
    "temp" => "no",  
    "webhook" =>  null,  
    "track_id" =>  null   
];  
  
$curl = curl_init();  
  
curl_setopt_array($curl, array(  
  CURLOPT_URL => 'https://stablediffusionapi.com/api/v5/multiview',  
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
  'url': 'https://stablediffusionapi.com/api/v5/multiview',  
  'headers': {  
    'Content-Type': 'application/json'  
  },  
  body: JSON.stringify({  
    "key":"",  
    "seed":12345,  
    "image":"https://pub-3626123a908346a7a8be8d9295f44e26.r2.dev/generations/0558bcce-cba0-4157-963f-9374b53d68d9.png",  
    "prompt": "make multiple images",  
    "width": 640,  
    "height":960,  
    "num_inference_steps":50,  
    "guidance_scale":4,  
    "temp":"no",  
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
  
url = "https://stablediffusionapi.com/api/v5/multiview"  
  
payload = json.dumps({  
    "key":"",  
    "seed":12345,  
    "image":"https://pub-3626123a908346a7a8be8d9295f44e26.r2.dev/generations/0558bcce-cba0-4157-963f-9374b53d68d9.png",  
    "prompt": "make multiple images",  
    "width": 640,  
    "height":960,  
    "num_inference_steps":50,  
    "guidance_scale":4,  
    "temp":"no",  
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
RequestBody body = RequestBody.create(mediaType, "{\n    \"key\":\"\",\n    \"seed\":12345,\n    \"image\":\"https://pub-3626123a908346a7a8be8d9295f44e26.r2.dev/generations/0558bcce-cba0-4157-963f-9374b53d68d9.png\",\n    \"prompt\": \"make multiple images\",\n    \"width\": 640,\n    \"height\":960,\n    \"num_inference_steps\":50,\n    \"guidance_scale\":4,\n    \"temp\":\"no\",\n    \"webhook\": null,\n    \"track_id\": null \n}");  
Request request = new Request.Builder()  
  .url("https://stablediffusionapi.com/api/v5/multiview")  
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
    "generationTime": 13.116175889968872,  
    "id": 657,  
    "output": [  
        "https://pub-3626123a908346a7a8be8d9295f44e26.r2.dev/generations/2ee9e794-7b5a-4e2d-80b1-7e6a943a8a36.png"  
    ],  
    "proxy_links": [  
        "https://cdn2.stablediffusionapi.com/generations/2ee9e794-7b5a-4e2d-80b1-7e6a943a8a36.png"  
    ],  
    "meta": {  
        "file_prefix": "2ee9e794-7b5a-4e2d-80b1-7e6a943a8a36",  
        "guidance_scale": 4,  
        "height": 960,  
        "image": "https://cdn2.stablediffusionapi.com/generations/2874812851699698333.png",  
        "num_inference_steps": 50,  
        "outdir": "out",  
        "prompt": "make multiple images",  
        "seed": 12345,  
        "temp": "no",  
        "width": 640  
    }  
}  
  

```
[PreviousMixture Canvas](/docs/image-editing/mixture-canvas)[NextFashion (Beta)](/docs/image-editing/fashion)* [Overview](#overview)
* [Request](#request)
* [Body Attributes](#body-attributes)
* [Example](#example)
	+ [Body](#body)
	+ [Request](#request-1)
	+ [Response](#response)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



