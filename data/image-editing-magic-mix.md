




Magic Mix Endpoint \| Stable Diffusion API Documentation








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
* Magic Mix
On this pageMagic Mix Endpoint
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

This endpoint allow you to magic mix image and prompt to produce an catching images

![Image to image endpoint result](/docs/assets/images/magic-mixer-1-75b41eff7345f2adf2035f93a5aa350c.png)Request[â](#request "Direct link to Request")
-----------------------------------------------


```
--request POST 'https://stablediffusionapi.com/api/v5/magic_mix' \  

```
Make a `POST` request to <https://stablediffusionapi.com/api/v5/magic_mix> endpoint and pass the required parameters as a request body to the endpoint. 

Body Attributes[â](#body-attributes "Direct link to Body Attributes")
-----------------------------------------------------------------------



| Parameter | Description |
| --- | --- |
| **key** | Your API Key used for request authorization |
| **prompt** | Text prompt with description of the things you want in the image to be generated |
| **negative\_prompt** | Items you don't want in the image |
| **image** | url of the image you want magic mix |
| **width** | Max Height: Default `768` |
| **height** | Max Height: Default `768` |
| **kmin** | Optional. Minimum k value. Default is `0.3` |
| **kmax** | Optional. Maximum k value. Default is `0.5` |
| **mix\_factor** | Optional. Mix factor for the task. Default is `0.5` |
| **steps** | Number of denoising steps (minimum: 1; maximum: 50\) Default is `20` |
| **samples** | Number of images to be returned in response. The maximum value is 4\. |
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
    "prompt":"Bed",  
    "height":768,  
    "width":768,  
    "image":"https://user-images.githubusercontent.com/59410571/209578593-141467c7-d831-4792-8b9a-b17dc5e47816.jpg",  
    "kmax":0.5,  
    "kmin":0.3,  
    "mix_factor":0.5,  
    "samples":1,  
    "negative_prompt":"low quality",  
    "seed":1829183163,  
    "steps":20,  
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
    "prompt":"Bed",  
    "height":768,  
    "width":768,  
    "image":"https://user-images.githubusercontent.com/59410571/209578593-141467c7-d831-4792-8b9a-b17dc5e47816.jpg",  
    "kmax":0.5,  
    "kmin":0.3,  
    "mix_factor":0.5,  
    "samples":1,  
    "negative_prompt":"low quality",  
    "seed":1829183163,  
    "steps":20,  
    "webhook": null,  
    "track_id": null   
});  
  
var requestOptions = {  
  method: 'POST',  
  headers: myHeaders,  
  body: raw,  
  redirect: 'follow'  
};  
  
fetch("https://stablediffusionapi.com/api/v5/magic_mix", requestOptions)  
  .then(response => response.text())  
  .then(result => console.log(result))  
  .catch(error => console.log('error', error));  

```

```
<?php  
  
$payload = [  
   "key" => "",  
    "prompt" => "Bed",  
    "height" => 768,  
    "width" => 768,  
    "image" => "https://user-images.githubusercontent.com/59410571/209578593-141467c7-d831-4792-8b9a-b17dc5e47816.jpg",  
    "kmax" => 0.5,  
    "kmin" => 0.3,  
    "mix_factor" => 0.5,  
    "samples" => 1,  
    "negative_prompt" => "low quality",  
    "seed" => 1829183163,  
    "steps" => 20,  
    "webhook" => null,  
    "track_id" => null   
];  
  
$curl = curl_init();  
  
curl_setopt_array($curl, array(  
  CURLOPT_URL => 'https://stablediffusionapi.com/api/v5/magic_mix',  
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
  'url': 'https://stablediffusionapi.com/api/v5/magic_mix',  
  'headers': {  
    'Content-Type': 'application/json'  
  },  
  body: JSON.stringify({  
    "key":"",  
    "prompt":"Bed",  
    "height":768,  
    "width":768,  
    "image":"https://user-images.githubusercontent.com/59410571/209578593-141467c7-d831-4792-8b9a-b17dc5e47816.jpg",  
    "kmax":0.5,  
    "kmin":0.3,  
    "mix_factor":0.5,  
    "samples":1,  
    "negative_prompt":"low quality",  
    "seed":1829183163,  
    "steps":20,  
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
  
url = "https://stablediffusionapi.com/api/v5/magic_mix"  
  
payload = json.dumps({  
    "key":"",  
    "prompt":"Bed",  
    "height":768,  
    "width":768,  
    "image":"https://user-images.githubusercontent.com/59410571/209578593-141467c7-d831-4792-8b9a-b17dc5e47816.jpg",  
    "kmax":0.5,  
    "kmin":0.3,  
    "mix_factor":0.5,  
    "samples":1,  
    "negative_prompt":"low quality",  
    "seed":1829183163,  
    "steps":20,  
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
    RequestBody body = RequestBody.create(mediaType, "{\n     \"key\":\"\",\n    \"prompt\":\"Bed\",\n    \"height\":768,\n    \"width\":768,\n    \"image\":\"https://user-images.githubusercontent.com/59410571/209578593-141467c7-d831-4792-8b9a-b17dc5e47816.jpg\",\n    \"kmax\":0.5,\n    \"kmin\":0.3,\n    \"mix_factor\":0.5,\n    \"samples\":1,\n    \"negative_prompt\":\"low quality\",\n    \"seed\":1829183163,\n    \"steps\":20,\n    \"webhook\": null,\n    \"track_id\": null \n}");  
    Request request = new Request.Builder()  
    .url("https://stablediffusionapi.com/api/v5/magic_mix")  
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
    "generationTime": 7.986585378646851,  
    "id": 511,  
    "output": [  
        "https://pub-3626123a908346a7a8be8d9295f44e26.r2.dev/generations/424151c6-00fd-4837-aaef-8b98a5c09f38.png"  
    ],  
    "meta": {  
        "H": 768,  
        "W": 768,  
        "file_prefix": "424151c6-00fd-4837-aaef-8b98a5c09f38",  
        "image": "https://user-images.githubusercontent.com/59410571/209578593-141467c7-d831-4792-8b9a-b17dc5e47816.jpg",  
        "kmax": 0.5,  
        "kmin": 0.3,  
        "mix_factor": 0.5,  
        "n_samples": 1,  
        "negative_prompt": "low quality",  
        "outdir": "out",  
        "prompt": "Bed",  
        "seed": 1829183163,  
        "steps": 20  
    }  
}  
  

```
[PreviousBlip Diffusion](/docs/image-editing/blip-diffusion)[NextDepth to Image](/docs/image-editing/depth2img)* [Overview](#overview)
* [Request](#request)
* [Body Attributes](#body-attributes)
* [Example](#example)
	+ [Body](#body)
	+ [Request](#request-1)
	+ [Response](#response)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



