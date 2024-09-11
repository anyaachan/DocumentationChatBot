




Enterprise API \| Stable Diffusion API Documentation








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
* API Overview
On this pageEnterprise API
==============

Overview[â](#overview "Direct link to Overview")
--------------------------------------------------

The Enterprise API is packed with a nice collection of endpoints. Some of them cover the interaction with your server which is the main advantage of the Enterprise plan. Others cover common model, image and video related processes.

infoThe Enterprise API is accessible only with a special **enterprise API key**, which you will receive upon **[purchasing](https://stablediffusionapi.com/enterprise#plan)** an enterprise plan.

You can view our Enterprise plans **[here](https://stablediffusionapi.com/enterprise#plan)**.

Available Endpoints[â](#available-endpoints "Direct link to Available Endpoints")
-----------------------------------------------------------------------------------

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
### System Details[â](#system-details "Direct link to System Details")

This endpoint returns information about your server.

### Restart Server[â](#restart-server "Direct link to Restart Server")

This endpoint is used to restart your dedicated server. As a response you will receive information about the result of the restart command.

### Update Server[â](#update-server "Direct link to Update Server")

This endpoint is used to update your dedicated server. As a response you will receive information about the result of the update command.

### Update S3 Details[â](#update-s3-details "Direct link to Update S3 Details")

This endpoint is used to update the S3 details on your dedicated server.

### Clear Cache[â](#clear-cache "Direct link to Clear Cache")

This endpoint is used to clear the API's cache.

### List Schedulers[â](#list-schedulers "Direct link to List Schedulers")

This endpoint is used to get a list of all the available schedulers.

### Load Model[â](#load-model "Direct link to Load Model")

This endpoint is used to load a model to your dedicated server.

### Verify Model[â](#verify-model "Direct link to Verify Model")

This endpoint is used to check if a particular model exists.

### Get All Models[â](#get-all-models "Direct link to Get All Models")

This endpoint returns a list of all the models available on your dedicated server.

### Delete Model[â](#delete-model "Direct link to Delete Model")

This endpoint is used to delete a model from your dedicated server.

### Controlnet Endpoint[â](#controlnet-endpoint "Direct link to Controlnet Endpoint")

This endpoint is used to generate ControlNet images.

### Text to Image[â](#text-to-image "Direct link to Text to Image")

This endpoint is used to create an image from a text prompt based on trained or on public models.

### Text to Video[â](#text-to-video "Direct link to Text to Video")

This endpoint is used to create video from a text prompt based on trained or on public models.

### Inpainting[â](#inpainting "Direct link to Inpainting")

This endpoint is used to change (inpaint) some part of an image according to specific requirements, based on trained or on public models.

### Super Resolution[â](#super-resolution "Direct link to Super Resolution")

This endpoint returns a super resolution version of an image.

### Upload Image[â](#upload-image "Direct link to Upload Image")

This endpoint id used to upload an image to your S3 bucket.

### Sync Models[â](#sync-models "Direct link to Sync Models")

This endpoint is important for users with multiple servers and want to sync models between two servers

### Load Vae[â](#load-vae "Direct link to Load Vae")

This endpoint is helps to load vae

### NSFW Image Check[â](#nsfw-image-check "Direct link to NSFW Image Check")

This endpoint allows you to check if an image is nsfw image

Playground[â](#playground "Direct link to Playground")
--------------------------------------------------------

You can test the available endpoints in our dedicated **[Playground Section](https://stablediffusionapi.com/playground?channel=enterprise)**.

[PreviousEnterprise Plan](/docs/category/enterprise-plan)[NextSystem Details](/docs/enterprise-plan/system-details)* [Overview](#overview)
* [Available Endpoints](#available-endpoints)
	+ [System Details](#system-details)
	+ [Restart Server](#restart-server)
	+ [Update Server](#update-server)
	+ [Update S3 Details](#update-s3-details)
	+ [Clear Cache](#clear-cache)
	+ [List Schedulers](#list-schedulers)
	+ [Load Model](#load-model)
	+ [Verify Model](#verify-model)
	+ [Get All Models](#get-all-models)
	+ [Delete Model](#delete-model)
	+ [Controlnet Endpoint](#controlnet-endpoint)
	+ [Text to Image](#text-to-image)
	+ [Text to Video](#text-to-video)
	+ [Inpainting](#inpainting)
	+ [Super Resolution](#super-resolution)
	+ [Upload Image](#upload-image)
	+ [Sync Models](#sync-models)
	+ [Load Vae](#load-vae)
	+ [NSFW Image Check](#nsfw-image-check)
* [Playground](#playground)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



