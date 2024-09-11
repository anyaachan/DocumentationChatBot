




Enterprise: Upload Image Endpoint \| Stable Diffusion API Documentation








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
	+ [API Overview](/docs/enterprise-plan/overview)
	+ [System Details](/docs/enterprise-plan/system-details)
	+ [Restart Server](/docs/enterprise-plan/restart-server)
	+ [Update Server](/docs/enterprise-plan/update-server)
	+ [Update S3 Details](/docs/enterprise-plan/update-s3-details)
	+ [Clear Cache](/docs/enterprise-plan/clear-cache)
	+ [List Schedulers](/docs/enterprise-plan/list-schedulers)
	+ [Load Model](/docs/enterprise-plan/load-model)
	+ [Verify Model](/docs/enterprise-plan/verify-model)
	+ [Get All Models](/docs/enterprise-plan/get-all-models)
	+ [Delete Model](/docs/enterprise-plan/delete-model)
	+ [Controlnet](/docs/enterprise-plan/controlnet-ep)
	+ [Text to Image](/docs/enterprise-plan/text2img)
	+ [Text to Video](/docs/enterprise-plan/text2video)
	+ [Image to Image](/docs/enterprise-plan/img2img)
	+ [Inpainting](/docs/enterprise-plan/inpainting)
	+ [Super Resolution](/docs/enterprise-plan/super-resolution)
	+ [Upload Image](/docs/enterprise-plan/upload-image)
	+ [Sync Model](/docs/enterprise-plan/sync-model)
	+ [Load Vae](/docs/enterprise-plan/load-vae)
	+ [NSFW Image Check](/docs/enterprise-plan/nsfw-image-check)
	+ [Fetch Queued Images](/docs/enterprise-plan/fetch-queue-image)
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
* [Enterprise Plan](/docs/category/enterprise-plan)
* Upload Image
On this pageEnterprise: Upload Image Endpoint
=================================

* [enterprise/system\_details](/docs/enterprise-plan/system-details)
* [enterprise/restart\_server](/docs/enterprise-plan/restart-server)
* [enterprise/update\_server](/docs/enterprise-plan/update-server)
* [enterprise/update\_s3](/docs/enterprise-plan/update-s3-details)
* [enterprise/clear\_cache](/docs/enterprise-plan/clear-cache)
* [enterprise/schedulers\_list](/docs/enterprise-plan/list-schedulers)
* [enterprise/load\_model](/docs/enterprise-plan/load-model)
* [enterprise/verify\_model](/docs/enterprise-plan/verify-model)
* [enterprise/get\_all\_models](/docs/enterprise-plan/get-all-models)
* [enterprise/delete\_model](/docs/enterprise-plan/delete-model)
* [enterprise/controlnet](/docs/enterprise-plan/controlnet-ep)
* [enterprise/text2img](/docs/enterprise-plan/text2img)
* [enterprise/text2video](/docs/enterprise-plan/img2img)
* [enterprise/text2video](/docs/enterprise-plan/text2video)
* [enterprise/inpaint](/docs/enterprise-plan/inpainting)
* [enterprise/super\_resolution](/docs/enterprise-plan/super-resolution)
* [enterprise/upload\_image](/docs/enterprise-plan/upload-image)
* [enterprise/sync\_image](/docs/enterprise-plan/sync-model)
* [enterprise/load\_vae](/docs/enterprise-plan/load-vae)
* [enterprise/nsfw\_image\_check](/docs/enterprise-plan/nsfw-image-check)
* [enterprise/fetch\_queue\_image](/docs/enterprise-plan/fetch-queue-image)
Overview[â](#overview "Direct link to Overview")
--------------------------------------------------

The Enterprise Upload Image endpoint uploads an image to your S3 bucket.

infoYou should have your own S3 bucket to use this endpoint.

Update your S3 bucket details using **[this endpoint](/docs/enterprise-plan/update-s3-details)**.

Request[â](#request "Direct link to Request")
-----------------------------------------------


```
--request POST 'https://stablediffusionapi.com/api/v1/enterprise/upload_image' \  

```
Send a `POST` request to <https://stablediffusionapi.com/api/v1/enterprise/upload_image> endpoint. 

noteMake sure you are passing the image in **base64** format.

Body Attributes[â](#body-attributes "Direct link to Body Attributes")
-----------------------------------------------------------------------



| Parameter | Description |
| --- | --- |
| **key** | Your enterprise API Key used for request authorization. |
| **base64\_image** | The base64 string of the image to be uploaded. |
| **image\_type** | Extension or type of the image; **options**: png, jpeg, jpg |

Example[â](#example "Direct link to Example")
-----------------------------------------------

### Body[â](#body "Direct link to Body")

Body Raw
```
{  
  "key": "enterprise_api_key",  
  "base64_image": "iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAACXBIWXMAAA7DAAAOwwHHb6hkAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAABe1JREFUaIHdms9PVFcUxz/zA2YhFRAUQVjVH1EXVBFIEBxNq2n/BKMB2RgDahCCCxOX/gG17YYfUVmYxh9VlCC1QcFGg4mKdmGi/ZGgLkQYQKogkJnbxZkH782bx7w3zDBtT3Iyc+fec+75zrv33HPOfS4SQx5gO7An/LkJWA9kRIz7APwBvAAeA33AEyCYIDvipjLge2AUUHHyaFhH6TLbDsA3wK92DM3OFrYzFrgH7FsOABuBX6IZUVSEqqlBtbejBgZQ4+MopYw8NiZ9bW2o6mrUunWWgHqADckA4AKagE/6CX0+VG0t6t49VChkNjwWh0Kovj7UoUOo9HQTmE9AQ3juhFAmcEM/ideLOnoU9eaNc+Ot+PVrVH296I4AdB1YuVQQa4FBveLyctSzZ4kDEMlPn6JKS01gHgN5SwHxu6bM5UI1N6NmZ5MHQuPZWVRjo8ypA/MyHjArEf+uAOXxyCZONoBI7uhApaUZwPwGZNkF4QJuasJpaajOzuUHofG1a6Z9cx2bDqAJ3XLq6EgdCI3PnTMtsxOxQGxA52JPnkw9CI0bG02uedNiQOYPu/Ly5dnYdnl21uTNfrYC8bU2yOtNrouNlwcHxfHowEQNZ+Zjp2PHUm+0FdfVGYD0R4Io0zp9Pmcn9rt3Anz3btSJE6hAILZMICBj/X7U8eOiw+58r16ZwpkdeiA/aB21tfaVTk2hNm82nsLbti2+t2ZmUMXFRpktW1DT0/bnrakxyJ/VQHjQ5RP9/fYVdnWJTE6OhOqZmdLu7bWW6e2VMVlZIrNqlbS7uuzPe+eOAcgw4HYjGV0OQGEhVFVZ+QIzffwon+npMD4OPp+0p6acy2i/2yG/H/Lz55trgC8AThJGV1PjbOONjKByc43LJD8fNTFhLTMxIWP0MqtXo0ZHnc198KBBR5P2RADYtcv+vwKQmwu3bkFFBaxYIfI9PZCZaS2TmSkyVVUis3MndHdDTo6zuf1+Q7ME4ClhZAMDiXeXyeL7941hvgv4m3C1Y2wMsrOd/TOpokBAVkSYJl1ACHB5PDA3B66EJZbJJaXA64VQSJpuwiFxRsZ/BwSIrRkLVTOXO4W2JJT+V0vrA0AwCBMTqTTNGQUC8yAAJt3AX1rr5Uv7ivr6oLISTp1amkGhEOzfDwUFcPmyfbkIW/8E+JGwP3ZSYPD7F/x4d3f858HFiwt6Kivty7W0GM6Ri26kZgRAvym6t6aSkoXvDQ0wOWlfVqOREWhuXmjv3WtfNsLWxyDxvAJUYaH90ufw8EK0C6iqquj1Xit++xa1ffuCfF4e6v17e7LBoCle2wYSxo9oPzoJ469cMVY3iopQly7JRFYyc3Oo8+fFcE3O7Ubdvm1/Xi0VCPNbYP4Y+U7rcJJYKYU6e9ZUqlFFRVLHbW9H3byJunFD1vThw+bI1+NxXnKqrjbo+Fa/xkq1Dp9PCspOFHd2otassbwisOTCwsWTsGg8NGRKdUuIoH6ts77eufcJBFCnT0tuEQtAQQHqzBnU5KTzeY4cMei6qxmvP8f3Ea4Veb3w6BEUF0dijU3BoHiUhw/h+XPJAt1uiaq3bpXcpaIinJs6pMFBKC2VOcL0FdAbbWwPYbSlpf+uAt3MDGrHDsPT6F4M9HpgWhvc1JR6ABo3NJhKphtjPcEGTcDlkgJyqkG0tZk84/FYIED2zXVNyOuV0n6qQFy9arpWuIqDe8XPkGN/3te3ti4/iAsXTCAeYX4JISblIddd88usqWl5HMDMjOyJiOX0AqlhxUV5+icDqLIyqYonC8STJybvpD2JuEFotBLdniG8b+rqnEcAi/HQkBx2EdcGCviJOJaTFbmQ6y7DCwPp6VKdvHt38UDRioNBCVGqq6O+MDCNeKekJN8b0B2aes7PlzJmayvqwYPoJdDRUelraUEdOIBau9YyjOlGzrSk017kFaWYcVVWlrCdsUjs9OVyAIikEiSMHrZpaDQeDuswRbFOKFHrz42U9vcgGedG4HPkPRY9vUcKBdqLZ3eAZ0hJakn0DwRcaPWWv+9kAAAAAElFTkSuQmCC",  
  "image_type": "png"  
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
  "base64_image": "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",  
  "image_type": "png"  
});  
  
var requestOptions = {  
  method: 'POST',  
  headers: myHeaders,  
  body: raw,  
  redirect: 'follow'  
};  
  
fetch("https://stablediffusionapi.com/api/v1/enterprise/upload_image", requestOptions)  
  .then(response => response.text())  
  .then(result => console.log(result))  
  .catch(error => console.log('error', error));  

```

```
<?php  
  
$payload = [  
  "key" => "",  
  "base64_image" => "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",  
  "image_type" => "png"  
];  
  
$curl = curl_init();  
  
curl_setopt_array($curl, array(  
  CURLOPT_URL => 'https://stablediffusionapi.com/api/v1/enterprise/upload_image',  
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
  'url': 'https://stablediffusionapi.com/api/v1/enterprise/upload_image',  
  'headers': {  
    'Content-Type': 'application/json'  
  },  
  body: JSON.stringify({  
    "key": "",  
    "base64_image": "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",  
    "image_type": "png"  
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
  
url = "https://stablediffusionapi.com/api/v1/enterprise/upload_image"  
  
payload = json.dumps({  
  "key": "",  
  "base64_image": "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",  
  "image_type": "png"  
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
RequestBody body = RequestBody.create(mediaType, "{\n  \"key\": \"\",\n  \"base64_image\": \"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\",\n  \"image_type\": \"png\"\n}");  
Request request = new Request.Builder()  
  .url("https://stablediffusionapi.com/api/v1/enterprise/upload_image")  
  .method("POST", body)  
  .addHeader("Content-Type", "application/json")  
  .build();  
Response response = client.newCall(request).execute();  

```
### Response[â](#response "Direct link to Response")


```
{  
  "status": "success",  
  "message": "image uploaded",  
  "image_url": "https://pub-8b49af329fae499aa563997f5d4068a4.r2.dev/generations/2789658481681896990.png"  
}  

```
[PreviousSuper Resolution](/docs/enterprise-plan/super-resolution)[NextSync Model](/docs/enterprise-plan/sync-model)* [Overview](#overview)
* [Request](#request)
* [Body Attributes](#body-attributes)
* [Example](#example)
	+ [Body](#body)
	+ [Request](#request-1)
	+ [Response](#response)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



