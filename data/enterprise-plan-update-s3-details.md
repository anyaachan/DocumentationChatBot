




Enterprise: Update S3 Details Endpoint \| Stable Diffusion API Documentation








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
* Update S3 Details
On this pageEnterprise: Update S3 Details Endpoint
======================================

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

This endpoint is used to update the S3 details on your dedicated server.

Request[â](#request "Direct link to Request")
-----------------------------------------------


```
--request POST 'https://stablediffusionapi.com/api/v1/enterprise/update_s3' \  

```
Send a `POST` request to <https://stablediffusionapi.com/api/v1/enterprise/update_s3> endpoint. You have to pass the below listed request body parameters to update the S3 details.

info**You can use any S3 compatible service like Cloudflare R2, Digital Ocean Spaces, AWS S3, Google Cloud Storage, Alibaba OSS, Backblaze, etc.**

dangerYou need to give PutObjectAcl on S3 bucket. Else you won't be able to upload images to S3 bucket.
Here is link to stackoverflow on how to do it: `<https://stackoverflow.com/questions/36272286/getting-access-denied-when-calling-the-putobject-operation-with-bucket-level-per>`

Attributes[â](#attributes "Direct link to Attributes")
--------------------------------------------------------



| Parameter | Description |
| --- | --- |
| **key** | Your enterprise API Key used for request authorization. |
| **public\_url** | A public URL on which images can be accessible. Make sure to make your bucket publicly accessible, so you can access the links. |
| **region\_name** | S3 region name. |
| **endpoint\_url** | S3 endpoint URL. |
| **aws\_access\_key\_id** | Bucket's access key. |
| **aws\_secret\_access\_key** | Bucket's secret key. |
| **image\_directory** | The image directory inside the S3 bucket, where images will be stored. Create a directory named "generations" inside the bucket and make sure it is public, so you can access the images using their links. |

Example[â](#example "Direct link to Example")
-----------------------------------------------

### Body[â](#body "Direct link to Body")

Body Raw
```
{  
  "key": "enterprise_api_key",  
  "public_url": "https://d1okzptojspljx.cloudfront.net/generations/",  
  "region_name": "us-east-1",  
  "endpoint_url": "https://stable-diffusion-api.s3.amazonaws.com",  
  "aws_access_key_id": "access-key",  
  "aws_secret_access_key": "secret-key",  
  "image_directory": "generations"  
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
  "public_url": "https://d1okzptojspljx.cloudfront.net/generations/",  
  "region_name": "us-east-1",  
  "endpoint_url": "https://stable-diffusion-api.s3.amazonaws.com",  
  "aws_access_key_id": "access-key",  
  "aws_secret_access_key": "secret-key",  
  "image_directory": "generations"  
});  
  
var requestOptions = {  
  method: 'POST',  
  headers: myHeaders,  
  body: raw,  
  redirect: 'follow'  
};  
  
fetch("https://stablediffusionapi.com/api/v1/enterprise/update_s3", requestOptions)  
  .then(response => response.text())  
  .then(result => console.log(result))  
  .catch(error => console.log('error', error));  

```

```
<?php  
  
$payload = [  
  "key" => "",   
  "public_url" => "https://d1okzptojspljx.cloudfront.net/generations/",   
  "region_name" => "us-east-1",   
  "endpoint_url" => "https://stable-diffusion-api.s3.amazonaws.com",   
  "aws_access_key_id" => "access-key",   
  "aws_secret_access_key" => "secret-key",   
  "image_directory" => "generations"  
];  
  
$curl = curl_init();  
  
curl_setopt_array($curl, array(  
  CURLOPT_URL => 'https://stablediffusionapi.com/api/v1/enterprise/update_s3',  
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
  'url': 'https://stablediffusionapi.com/api/v1/enterprise/update_s3',  
  'headers': {  
    'Content-Type': 'application/json'  
  },  
  body: JSON.stringify({  
    "key": "",  
    "public_url": "https://d1okzptojspljx.cloudfront.net/generations/",  
    "region_name": "us-east-1",  
    "endpoint_url": "https://stable-diffusion-api.s3.amazonaws.com",  
    "aws_access_key_id": "access-key",  
    "aws_secret_access_key": "secret-key",  
    "image_directory": "generations"  
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
  
url = "https://stablediffusionapi.com/api/v1/enterprise/update_s3"  
  
payload = json.dumps({  
  "key": "",  
  "public_url": "https://d1okzptojspljx.cloudfront.net/generations/",  
  "region_name": "us-east-1",  
  "endpoint_url": "https://stable-diffusion-api.s3.amazonaws.com",  
  "aws_access_key_id": "access-key",  
  "aws_secret_access_key": "secret-key",  
  "image_directory": "generations"  
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
RequestBody body = RequestBody.create(mediaType, "{\n    \"key\": \"\",\n    \"public_url\": \"https://d1okzptojspljx.cloudfront.net/generations/\",\n    \"region_name\": \"us-east-1\",\n    \"endpoint_url\": \"https://stable-diffusion-api.s3.amazonaws.com\",\n    \"aws_access_key_id\": \"access-key\",\n    \"aws_secret_access_key\": \"secret-key\",\n    \"image_directory\": \"generations\"\n}");  
Request request = new Request.Builder()  
  .url("https://stablediffusionapi.com/api/v1/enterprise/update_s3")  
  .method("POST", body)  
  .addHeader("Content-Type", "application/json")  
  .build();  
Response response = client.newCall(request).execute();  

```
### Response[â](#response "Direct link to Response")

Make sure to give below permissions to your IAM user to upload images on S3 bucket.


```
{  
  "Version": "2012-10-17",  
  "Statement": [  
    {  
      "Sid": "VisualEditor0",  
      "Effect": "Allow",  
      "Action": [  
        "s3:ListBucket",  
        "s3:PutObject",  
        "s3:GetObject",  
        "s3:PutObjectAcl"  
      ],  
      "Resource": [  
        "arn:aws:s3:::stable-diffusion-api",  
        "arn:aws:s3:::stable-diffusion-api/*"  
      ]  
    }  
  ]  
}  

```
[PreviousUpdate Server](/docs/enterprise-plan/update-server)[NextClear Cache](/docs/enterprise-plan/clear-cache)* [Overview](#overview)
* [Request](#request)
* [Attributes](#attributes)
* [Example](#example)
	+ [Body](#body)
	+ [Request](#request-1)
	+ [Response](#response)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



