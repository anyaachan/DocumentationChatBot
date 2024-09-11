




Dreambooth API \| Stable Diffusion API Documentation








[Skip to main content](#docusaurus_skipToContent_fallback)[![Stable Diffusion Logo](/docs/img/SD-logo.png)![Stable Diffusion Logo](/docs/img/SD-logo.png)](https://stablediffusionapi.com)[Enterprise](https://stablediffusionapi.com/enterprise)[Pricing](https://stablediffusionapi.com/#pricing)[Blog](https://stablediffusionapi.com/blog)[Docs](https://stablediffusionapi.com/docs)[Playground](https://stablediffusionapi.com/playground)[Models](https://stablediffusionapi.com/models)[API Catalogue](https://stablediffusionapi.com/catalogue)* [Getting Started](/docs/)
* [Stable Diffusion API](/docs/category/stable-diffusion-api)
* [Train Model](/docs/category/train-model)
* [Community Models API](/docs/category/community-models-api)
	+ [API Overview](/docs/community-models-api/overview)
	+ [Text to Image](/docs/community-models-api/dreamboothtext2img)
	+ [Image to Image](/docs/community-models-api/dreamboothimg2img)
	+ [Inpainting](/docs/community-models-api/dreamboothinpainting)
	+ [Fetch Queued Images](/docs/community-models-api/dreamboothfetchqueimg)
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
* [Community Models API](/docs/category/community-models-api)
* API Overview
On this pageDreambooth API
==============

Overview[â](#overview "Direct link to Overview")
--------------------------------------------------

The Dreambooth API brings some cool features for interaction with community models. You can send request using own models or publicly available ones, just specify the model's ID.

You can find a list of available community models as well as their IDs [here](https://stablediffusionapi.com/models).

The available endpoints handle requests for generating images based on specific description and/or image provided.

You can also specify the number of images to be generated and set their height and width. 

Currently the API supports the following image formats: **PNG** and **JPG**.

Available Endpoints[â](#available-endpoints "Direct link to Available Endpoints")
-----------------------------------------------------------------------------------

* [v3/dreambooth](/docs/community-models-api/dreamboothtext2img)
* [v3/dreambooth/img2img](/docs/community-models-api/dreamboothimg2img)
* [v3/dreambooth/inpaint](/docs/community-models-api/dreamboothinpainting)
* [v3/dreambooth/fetch](/docs/community-models-api/dreamboothfetchqueimg)
### Text to Image Endpoint[â](#text-to-image-endpoint "Direct link to Text to Image Endpoint")

This endpoint generates and returns an image from a text and model ID passed in the request.

You can write prompt and negative prompt. The prompt is for the things you would like to see in the image and the **negative prompt** is to refine you description by listing the things you do **not want** to have in the generated image.

##### Endpoint in Action[â](#endpoint-in-action "Direct link to Endpoint in Action")

![Text to image endpoint result](/docs/assets/images/dream-txt2img-action-sm-61e5486320235ad22195ddee64b62360.png)### Image to Image Endpoint[â](#image-to-image-endpoint "Direct link to Image to Image Endpoint")

This endpoint generates and returns an image from an image passed with its URL in the request as well as the desired model's ID.

Together with the image you can add your description of the expected result by passing prompt and negative prompt.

The generated image will be based on the original image with the modifications described in the prompts also affected by the model specified.

##### Endpoint in Action[â](#endpoint-in-action-1 "Direct link to Endpoint in Action")

![Image to image endpoint result](/docs/assets/images/dream-img2img-action-sm-7434c25b236aa6ed5af4b82e97a6ca31.png)### Inpainting Endpoint[â](#inpainting-endpoint "Direct link to Inpainting Endpoint")

This endpoint generates and returns an image from an image and a mask passed with their URLs in the request together with a model's ID.

You can also add your description of the desired result by passing prompt and negative prompt.

The generated image will be based on the original image with the applied mask in order to replace an element in the image according to the modifications described in the prompts and the selected model.

##### Endpoint in Action[â](#endpoint-in-action-2 "Direct link to Endpoint in Action")

![Inpainting endpoint result](/docs/assets/images/db-v4-inpaint-action-sm-98d162609bb06ddbedc37295c8f474a3.png)### Fetch Queued Images Endpoint[â](#fetch-queued-images-endpoint "Direct link to Fetch Queued Images Endpoint")

This endpoint returns an already generated image by passing its **ID** with the endpoint location. This ID is specified by the **id** parameter in the response returned upon the request execution.

noteSometimes the response to your request might be with a **processing** status. In this case, instead of an output image, you will get its **ID** and the **eta** (estimated time) needed for it to be generated. This is when the Fetch Queued Image endpoint comes in handy. Simply pass your API key as the request body to the endpoint location returned by the `fetch_result` parameter.

Alternatively, in your generation request, you can pass a webhook, on which a post API call will be made.

Playground[â](#playground "Direct link to Playground")
--------------------------------------------------------

You can try the available endpoints in our [Playground](https://stablediffusionapi.com/playground?channel=community-model) section, just make sure to [sign up](https://stablediffusionapi.com/register) first.

[PreviousCommunity Models API](/docs/category/community-models-api)[NextText to Image](/docs/community-models-api/dreamboothtext2img)* [Overview](#overview)
* [Available Endpoints](#available-endpoints)
	+ [Text to Image Endpoint](#text-to-image-endpoint)
	+ [Image to Image Endpoint](#image-to-image-endpoint)
	+ [Inpainting Endpoint](#inpainting-endpoint)
	+ [Fetch Queued Images Endpoint](#fetch-queued-images-endpoint)
* [Playground](#playground)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



