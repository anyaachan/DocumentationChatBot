




Outpainting Endpoint \| Stable Diffusion API Documentation








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
* Outpainting
On this pageOutpainting Endpoint
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

This endpoint helps to outpaint by expanding the giving image

![Image to image endpoint result](/docs/assets/images/out-painting-1d03fe17ca436c59337aa5f6f071c779.png)Request[â](#request "Direct link to Request")
-----------------------------------------------


```
--request POST 'https://stablediffusionapi.com/api/v5/outpaint' \  

```
Make a `POST` request to <https://stablediffusionapi.com/api/v5/outpaint> endpoint and pass the required parameters as a request body to the endpoint. 

Body Attributes[â](#body-attributes "Direct link to Body Attributes")
-----------------------------------------------------------------------



| Parameter | Description |
| --- | --- |
| **key** | Your API Key used for request authorization |
| **prompt** | Text prompt with description of the things you want in the image to be generated |
| **negative\_prompt** | Items you don't want in the image |
| **image** | initial image url |
| **width** | Max Height: Width: 1024x1024 |
| **height** | Max Height: Width: 1024x1024 |
| **walk\_type** | List of values from `left`, `right`, `up`, `down` and `backward`. For example, if you want to pan to the right for a few steps and then zoom out, you must provide: `["right", "right", "backward"]` |
| **width\_translation\_per\_step** | The distance (in pixels) to translate the image in x\-axis while outpainting. Applies to walk types of `left`, `right` and `backward`. Default: 32px. |
| **height\_translation\_per\_step** | The distance (in pixels) to translate the image in y\-axis while outpainting. Applies to walk types of "up", "down" and "backward". Default: 32px. |
| **translation\_factor** | The factor by which to translate the image in x\-axis and y\-axis while outpainting. The calculated width translation per step is `translation_factor * width`, and similar for height. Provide either `translation_factor` or both `height_translation_per_step` and `width_translation_per_step`. If all three are provided, then `translation_factor` is ignored. Default: 0\.1\. |
| **num\_inference\_steps** | Number of denoising steps. Default: 20\. Min: 1, Max: 50 |
| **num\_interpolation\_steps** | Number of filler frames to generate between two outpaint walk directions. Default: 60\. Max: 120\. |
| **as\_video** | Whether to return the outpainting as a video or image. Should be `yes` or `no`. If `no`, the generated image will be the final result generated without any intermediate outpaint steps generated using `walk_type`. |
| **fps** | FPS of the generated video. This requires `as_video` to be set to `yes`. Default: 120\. |
| **seed** | Seed is used to reproduce results, same seed will give you same image in return again. Pass *null* for a random number. |
| **samples** | Number of images to be returned in response. The maximum value is 4\. |
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
    "width":512,  
    "height":512,  
    "prompt":"a majestic cat house, lush greenery, filled with plants, high quality, cartoonish, realistic, 4k",  
    "image":"https://i.ibb.co/wp0w7nt/1-d212fe65-f95c-4bbe-b275-99f0dedd901a.png",  
    "negative_prompt":"dull background, text, characters, symbols, unrealistic, repetitive background, boring background, bad, low quality, black background",  
    "height_translation_per_step": 64,  
    "width_translation_per_step":64,  
    "num_inference_steps": 15,  
    "as_video":"no",  
    "num_interpolation_steps": 32,  
    "walk_type":["back", "back", "left","left","up", "up"],  
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
    "width":512,  
    "height":512,  
    "prompt":"a majestic cat house, lush greenery, filled with plants, high quality, cartoonish, realistic, 4k",  
    "image":"https://i.ibb.co/wp0w7nt/1-d212fe65-f95c-4bbe-b275-99f0dedd901a.png",  
    "negative_prompt":"dull background, text, characters, symbols, unrealistic, repetitive background, boring background, bad, low quality, black background",  
    "height_translation_per_step": 64,  
    "width_translation_per_step":64,  
    "num_inference_steps": 15,  
    "as_video":"no",  
    "num_interpolation_steps": 32,  
    "walk_type":["back", "back", "left","left","up", "up"],  
    "webhook": null,  
    "track_id": null    
});  
  
var requestOptions = {  
  method: 'POST',  
  headers: myHeaders,  
  body: raw,  
  redirect: 'follow'  
};  
  
fetch("https://stablediffusionapi.com/api/v5/outpaint", requestOptions)  
  .then(response => response.text())  
  .then(result => console.log(result))  
  .catch(error => console.log('error', error));  

```

```
<?php  
  
$payload = [  
    "key" => "",  
    "seed" => 12345,  
    "width" => 512,  
    "height" => 512,  
    "prompt" => "a majestic cat house, lush greenery, filled with plants, high quality, cartoonish, realistic, 4k",  
    "image" => "https://i.ibb.co/wp0w7nt/1-d212fe65-f95c-4bbe-b275-99f0dedd901a.png",  
    "negative_prompt" => "dull background, text, characters, symbols, unrealistic, repetitive background, boring background, bad, low quality, black background",  
    "height_translation_per_step" => 64,  
    "width_translation_per_step" => 64,  
    "num_inference_steps" => 15,  
    "as_video" => "no",  
    "num_interpolation_steps" => 32,  
    "walk_type" => ["back", "back", "left","left","up", "up"],  
    "webhook" => null,  
    "track_id" => null   
];  
  
$curl = curl_init();  
  
curl_setopt_array($curl, array(  
  CURLOPT_URL => 'https://stablediffusionapi.com/api/v5/outpaint',  
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
  'url': 'https://stablediffusionapi.com/api/v5/outpaint',  
  'headers': {  
    'Content-Type': 'application/json'  
  },  
  body: JSON.stringify({  
    "key":"",  
    "seed":12345,  
    "width":512,  
    "height":512,  
    "prompt":"a majestic cat house, lush greenery, filled with plants, high quality, cartoonish, realistic, 4k",  
    "image":"https://i.ibb.co/wp0w7nt/1-d212fe65-f95c-4bbe-b275-99f0dedd901a.png",  
    "negative_prompt":"dull background, text, characters, symbols, unrealistic, repetitive background, boring background, bad, low quality, black background",  
    "height_translation_per_step": 64,  
    "width_translation_per_step":64,  
    "num_inference_steps": 15,  
    "as_video":"no",  
    "num_interpolation_steps": 32,  
    "walk_type":["back", "back", "left","left","up", "up"],  
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
  
url = "https://stablediffusionapi.com/api/v5/outpaint"  
  
payload = json.dumps({  
    "key":"",  
    "seed":12345,  
    "width":512,  
    "height":512,  
    "prompt":"a majestic cat house, lush greenery, filled with plants, high quality, cartoonish, realistic, 4k",  
     "image":"https://i.ibb.co/wp0w7nt/1-d212fe65-f95c-4bbe-b275-99f0dedd901a.png",  
    "negative_prompt":"dull background, text, characters, symbols, unrealistic, repetitive background, boring background, bad, low quality, black background",  
    "height_translation_per_step": 64,  
    "width_translation_per_step":64,  
    "num_inference_steps": 15,  
    "as_video":"no",  
    "num_interpolation_steps": 32,  
    "walk_type":["back", "back", "left","left","up", "up"],  
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
    RequestBody body = RequestBody.create(mediaType, "{\n    \"key\":\"\",\n    \"seed\":12345,\n    \"width\":512,\n    \"height\":512,\n    \"prompt\":\"a majestic cat house, lush greenery, filled with plants, high quality, cartoonish, realistic, 4k\",\n     \"image\":\"https://i.ibb.co/wp0w7nt/1-d212fe65-f95c-4bbe-b275-99f0dedd901a.png\",\n    \"negative_prompt\":\"dull background, text, characters, symbols, unrealistic, repetitive background, boring background, bad, low quality, black background\",\n   \n    \"height_translation_per_step\": 64,\n    \"width_translation_per_step\":64,\n    \"num_inference_steps\": 15,\n    \"as_video\":\"no\",\n    \"num_interpolation_steps\": 32,\n    \"walk_type\":[\"back\", \"back\", \"left\",\"left\",\"up\", \"up\"],\n    \"webhook\": null,\n    \"track_id\": null \n}");  
    Request request = new Request.Builder()  
      .url("https://stablediffusionapi.com/api/v5/outpaint")  
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
    "generationTime": 6.230603456497192,  
    "id": 663,  
    "output": [  
        "https://pub-3626123a908346a7a8be8d9295f44e26.r2.dev/generations/47b84646-fd81-4aaf-83fd-a25506b3d8d6.png"  
    ],  
    "proxy_links": [  
        "https://cdn2.stablediffusionapi.com/generations/47b84646-fd81-4aaf-83fd-a25506b3d8d6.png"  
    ],  
    "meta": {  
        "as_video": "no",  
        "file_prefix": "47b84646-fd81-4aaf-83fd-a25506b3d8d6",  
        "fps": 120,  
        "guidance_scale": 8,  
        "height": 512,  
        "height_translation_per_step": 64,  
        "image": "https://i.ibb.co/wp0w7nt/1-d212fe65-f95c-4bbe-b275-99f0dedd901a.png",  
        "n_samples": 1,  
        "negative_prompt": "dull background, text, characters, symbols, unrealistic, repetitive background, boring background, bad, low quality, black background",  
        "num_inference_steps": 15,  
        "num_interpolation_steps": 60,  
        "outdir": "out",  
        "prompt": "a majestic cat house, lush greenery, filled with plants, high quality, cartoonish, realistic, 4k",  
        "seed": 12345,  
        "temp": "no",  
        "translation_factor": null,  
        "walk_type": [],  
        "width": 512,  
        "width_translation_per_step": 64  
    }  
}  
  

```
[PreviousAPI Overview](/docs/image-editing/overview)[NextBlip Diffusion](/docs/image-editing/blip-diffusion)* [Overview](#overview)
* [Request](#request)
* [Body Attributes](#body-attributes)
* [Example](#example)
	+ [Body](#body)
	+ [Request](#request-1)
	+ [Response](#response)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



