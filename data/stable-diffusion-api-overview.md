




Stable Diffusion API \| Stable Diffusion API Documentation








[Skip to main content](#docusaurus_skipToContent_fallback)[![Stable Diffusion Logo](/docs/img/SD-logo.png)![Stable Diffusion Logo](/docs/img/SD-logo.png)](https://stablediffusionapi.com)[Enterprise](https://stablediffusionapi.com/enterprise)[Pricing](https://stablediffusionapi.com/#pricing)[Blog](https://stablediffusionapi.com/blog)[Docs](https://stablediffusionapi.com/docs)[Playground](https://stablediffusionapi.com/playground)[Models](https://stablediffusionapi.com/models)[API Catalogue](https://stablediffusionapi.com/catalogue)* [Getting Started](/docs/)
* [Stable Diffusion API](/docs/category/stable-diffusion-api)
	+ [API Overview](/docs/stable-diffusion-api/overview)
	+ [Text to Image](/docs/stable-diffusion-api/text2img)
	+ [Image to Image](/docs/stable-diffusion-api/img2img)
	+ [Inpainting](/docs/stable-diffusion-api/inpainting)
	+ [Fetch Queued Images](/docs/stable-diffusion-api/fetchqueimg)
	+ [System Load](/docs/stable-diffusion-api/system-load)
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
* [Text To 3D](/docs/category/text-to-3d)
* [Uncensored Chat](/docs/uncensored-chat)
* [A1111 Schedulers](/docs/a1111schedulers)
* [FAQ](/docs/faq)
* [Postman Collection](https://documenter.getpostman.com/view/18679074/2s83zdwReZ)
* [Support](https://discord.gg/UxqnDu7j3r)
* 
* 
* [Stable Diffusion API](/docs/category/stable-diffusion-api)
* API Overview
On this pageStable Diffusion API
====================

Overview[â](#overview "Direct link to Overview")
--------------------------------------------------

The Stable Diffusion API is using SDXL as single model API. So you can't change model on this endpoint. This API is faster and creates images in seconds.

The available endpoints handle requests for generating images based on specific description and/or image provided.

You can also specify the number of images to be generated and set their height and width. 

Currently the API supports the following image formats: **PNG** and **JPG**.

Available Endpoints[â](#available-endpoints "Direct link to Available Endpoints")
-----------------------------------------------------------------------------------

* [text2img](/docs/stable-diffusion-api/text2img)
* [img2img](/docs/stable-diffusion-api/img2img)
* [inpaint](/docs/stable-diffusion-api/inpainting)
* [fetch](/docs/stable-diffusion-api/fetchqueimg)
* [system\_load](/docs/stable-diffusion-api/system-load)
### Text to Image Endpoint[â](#text-to-image-endpoint "Direct link to Text to Image Endpoint")

This endpoint generates and returns an image from a text passed in the request.

You can write prompt and negative prompt. The prompt is for the things you would like to see in the image and the **negative prompt** is to refine you description by listing the things you do **not want** to have in the generated image.

##### Endpoint in Action[â](#endpoint-in-action "Direct link to Endpoint in Action")

![Text to image endpoint result](/docs/assets/images/txt2img-action-sm-76f78ddd2eac261716ae30ad397f8475.png)### Image to Image Endpoint[â](#image-to-image-endpoint "Direct link to Image to Image Endpoint")

This endpoint generates and returns an image from an image passed with its URL in the request.

Together with the image you can add your description of the desired result by passing prompt and negative prompt.

The generated image will be based on the original image with the modifications described in the prompts.

##### Endpoint in Action[â](#endpoint-in-action-1 "Direct link to Endpoint in Action")

![Image to image endpoint result](/docs/assets/images/img2img-action-sm-69595247104544ee95fe301c4d43b642.png)### Inpainting Endpoint[â](#inpainting-endpoint "Direct link to Inpainting Endpoint")

This endpoint generates and returns an image from an image and a mask passed with their URLs in the request.

Together with the image and the mask you can add your description of the desired result by passing prompt and negative prompt.

The generated image will be based on the original image with the applied mask in order to replace an element in the image according to the modifications described in the prompts.

##### Endpoint in Action[â](#endpoint-in-action-2 "Direct link to Endpoint in Action")

![Inpainting endpoint result](/docs/assets/images/inpaint-action-sm-9019741d6f6b106deaf22e58f3b39af1.png)### Fetch Queued Images Endpoint[â](#fetch-queued-images-endpoint "Direct link to Fetch Queued Images Endpoint")

This endpoint returns an already generated image by passing its **ID** with the endpoint location. This ID is specified by the **id** parameter in the response returned upon the request execution.

noteSometimes the response to your request might be with a **processing** status. In this case, instead of an output image, you will get its **ID** and the **eta** (estimated time) needed for it to be generated. This is when the Fetch Queued Image endpoint comes in handy. Simply pass your API key as the request body to the endpoint location returned by the `fetch_result` parameter.

Alternatively, in your generation request, you can pass a webhook, on which a post API call will be made.

### System Load Endpoint[â](#system-load-endpoint "Direct link to System Load Endpoint")

This endpoint returns information about any queued images, their processing time and the system status.

### Super Resolution Endpoint[â](#super-resolution-endpoint "Direct link to Super Resolution Endpoint")

This endpoint generates and returns a scaled up high resolution image from an image passed with its URL in the request.

##### Endpoint in Action[â](#endpoint-in-action-3 "Direct link to Endpoint in Action")

![Super Resolution endpoint result](/docs/assets/images/super-res-action-sm-03f81fbaeda5b4d52cc825de8405df35.png)Playground[â](#playground "Direct link to Playground")
--------------------------------------------------------

You can try the available endpoints in our [Playground](https://stablediffusionapi.com/playground?channel=stable-diffusion) section, just make sure to [sign up](https://stablediffusionapi.com/register) first.

[PreviousStable Diffusion API](/docs/category/stable-diffusion-api)[NextText to Image](/docs/stable-diffusion-api/text2img)* [Overview](#overview)
* [Available Endpoints](#available-endpoints)
	+ [Text to Image Endpoint](#text-to-image-endpoint)
	+ [Image to Image Endpoint](#image-to-image-endpoint)
	+ [Inpainting Endpoint](#inpainting-endpoint)
	+ [Fetch Queued Images Endpoint](#fetch-queued-images-endpoint)
	+ [System Load Endpoint](#system-load-endpoint)
	+ [Super Resolution Endpoint](#super-resolution-endpoint)
* [Playground](#playground)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



