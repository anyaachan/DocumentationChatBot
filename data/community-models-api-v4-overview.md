




Dreambooth API V4 \| Stable Diffusion API Documentation








[Skip to main content](#docusaurus_skipToContent_fallback)[![Stable Diffusion Logo](/docs/img/SD-logo.png)![Stable Diffusion Logo](/docs/img/SD-logo.png)](https://stablediffusionapi.com)[Enterprise](https://stablediffusionapi.com/enterprise)[Pricing](https://stablediffusionapi.com/#pricing)[Blog](https://stablediffusionapi.com/blog)[Docs](https://stablediffusionapi.com/docs)[Playground](https://stablediffusionapi.com/playground)[Models](https://stablediffusionapi.com/models)[API Catalogue](https://stablediffusionapi.com/catalogue)* [Getting Started](/docs/)
* [Stable Diffusion API](/docs/category/stable-diffusion-api)
* [Train Model](/docs/category/train-model)
* [Community Models API](/docs/category/community-models-api)
* [Text To Video](/docs/category/text-to-video)
* [Community Models API V4](/docs/category/community-models-api-v4)
	+ [API Overview](/docs/community-models-api-v4/overview)
	+ [Text to Image](/docs/community-models-api-v4/dreamboothtext2img)
	+ [LoRA](/docs/community-models-api-v4/dreamboothlora)
	+ [LoRA Multi](/docs/community-models-api-v4/dreamboothloramulti)
	+ [Image to Image](/docs/community-models-api-v4/dreamboothimg2img)
	+ [Inpainting](/docs/community-models-api-v4/dreamboothinpainting)
	+ [Fetch Queued Images](/docs/community-models-api-v4/dreamboothfetchqueimg)
	+ [Reload Model](/docs/community-models-api-v4/dreamboothreloadmodel)
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
* [Community Models API V4](/docs/category/community-models-api-v4)
* API Overview
On this pageDreambooth API V4
=================

Overview[â](#overview "Direct link to Overview")
--------------------------------------------------

The Dreambooth API V4 brings some cool features for interaction with community models. You can send request using own models or publicly available ones, just specify the model's ID.

You can find a list of available community models as well as their IDs [here](https://stablediffusionapi.com/models).

The available endpoints handle requests for generating images based on specific description and/or image provided.

You can also specify the number of images to be generated and set their height and width. 

Currently the API supports the following image formats: **PNG** and **JPG**.

Available Endpoints[â](#available-endpoints "Direct link to Available Endpoints")
-----------------------------------------------------------------------------------

* [v4/dreambooth](/docs/community-models-api-v4/dreamboothtext2img)
* [v4/dreambooth/img2img](/docs/community-models-api-v4/dreamboothimg2img)
* [v4/dreambooth/inpaint](/docs/community-models-api-v4/dreamboothinpainting)
* [v4/dreambooth/fetch](/docs/community-models-api-v4/dreamboothfetchqueimg)
* [v4/dreambooth/model\_reload](/docs/community-models-api-v4/dreamboothreloadmodel)
### Text to Image Endpoint[â](#text-to-image-endpoint "Direct link to Text to Image Endpoint")

This endpoint generates and returns an image from a text and model ID passed in the request.

You can write prompt and negative prompt. The prompt is for the things you would like to see in the image and the **negative prompt** is to refine you description by listing the things you do **not want** to have in the generated image.

##### Endpoint in Action[â](#endpoint-in-action "Direct link to Endpoint in Action")

![Text to image endpoint result](/docs/assets/images/db-v4-txt2img-action-sm-2416bf81c855ac696913f6ca3b678920.png)### Image to Image Endpoint[â](#image-to-image-endpoint "Direct link to Image to Image Endpoint")

This endpoint generates and returns an image from an image passed with its URL in the request as well as the desired model's ID.

Together with the image you can add your description of the expected result by passing prompt and negative prompt.

The generated image will be based on the original image with the modifications described in the prompts also affected by the model specified.

##### Endpoint in Action[â](#endpoint-in-action-1 "Direct link to Endpoint in Action")

![Image to image endpoint result](/docs/assets/images/db-v4-img2img-action-sm-422bfe4e9d993856418842c5a58eb134.png)### Inpainting Endpoint[â](#inpainting-endpoint "Direct link to Inpainting Endpoint")

This endpoint generates and returns an image from an image and a mask passed with their URLs in the request together with a model's ID.

You can also add your description of the desired result by passing prompt and negative prompt.

The generated image will be based on the original image with the applied mask in order to replace an element in the image according to the modifications described in the prompts and the selected model.

##### Endpoint in Action[â](#endpoint-in-action-2 "Direct link to Endpoint in Action")

![Inpainting endpoint result](/docs/assets/images/db-v4-inpaint-action-sm-98d162609bb06ddbedc37295c8f474a3.png)### Text to Video Endpoint[â](#text-to-video-endpoint "Direct link to Text to Video Endpoint")

This endpoint is used to create video from a text prompt based on trained or on public models.

##### Endpoint in Action[â](#endpoint-in-action-3 "Direct link to Endpoint in Action")

![Text to video endpoint result](/docs/assets/images/db-v4-txt2vid-action-sm-0242dcadd7b6341c8f812468c42b0a62.png)### Fetch Queued Images Endpoint[â](#fetch-queued-images-endpoint "Direct link to Fetch Queued Images Endpoint")

This endpoint returns an already generated image by passing its **ID** in the request body to the Fetch endpoint. This ID is returned by the **id** parameter in the response upon the request execution.

noteSometimes the response to your request might be with a **processing** status. In this case, instead of an output image, you will get its **ID** and the **eta** (estimated time) needed for it to be generated. This is when the Fetch Queued Image endpoint comes in handy. Simply pass your API key and the **ID** as "request\_id" in the request body to the **fetch** endpoint.

Alternatively, in your generation request, you can pass a webhook, on which a post API call will be made.

### Reload Model Endpoint[â](#reload-model-endpoint "Direct link to Reload Model Endpoint")

The Dreambooth Reload Model API is used to reload an idle model that has not been used for more than 7 days.

[PreviousCommunity Models API V4](/docs/category/community-models-api-v4)[NextText to Image](/docs/community-models-api-v4/dreamboothtext2img)* [Overview](#overview)
* [Available Endpoints](#available-endpoints)
	+ [Text to Image Endpoint](#text-to-image-endpoint)
	+ [Image to Image Endpoint](#image-to-image-endpoint)
	+ [Inpainting Endpoint](#inpainting-endpoint)
	+ [Text to Video Endpoint](#text-to-video-endpoint)
	+ [Fetch Queued Images Endpoint](#fetch-queued-images-endpoint)
	+ [Reload Model Endpoint](#reload-model-endpoint)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



