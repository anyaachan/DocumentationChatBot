




Image Editing API \| Stable Diffusion API Documentation








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
* API Overview
On this pageImage Editing API
=================

Overview[â](#overview "Direct link to Overview")
--------------------------------------------------

The image [editing suites](https://stablediffusionapi.com/image-editing) brings you some exclusive API endpoints with few default essential endpoints

Default endpoints :

1. [Text to image](/docs/category/stable-diffusion-api)\- Singleton model for faster speed \-
2. [Text to image](/docs/category/community-models-api-v4) \- Custom models from 10000\+ combinations
3. [Inpainting](/docs/community-models-api-v4/dreamboothinpainting)
4. [Custom Controlnets](/docs/category/controlnet)
5. [Custom LoRas](/docs/community-models-api-v4/dreamboothlora)

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
Available Endpoints[â](#available-endpoints "Direct link to Available Endpoints")
-----------------------------------------------------------------------------------

### Image Guided Edit[â](#image-guided-edit "Direct link to Image Guided Edit")

This endpoint is used to edit an image using a text prompt with the description of the desired changes.

##### Endpoint in Action[â](#endpoint-in-action "Direct link to Endpoint in Action")

![Picture to picture endpoint result](/docs/assets/images/v5-pix2pix-action-sm-3c8d81aab219063de5d407ca1d98b05e.png)### Depth to Image[â](#depth-to-image "Direct link to Depth to Image")

This endpoint allows for depth to generate a picture.

##### Endpoint in Action[â](#endpoint-in-action-1 "Direct link to Endpoint in Action")

![Depth to image endpoint result](/docs/assets/images/v5-depth2img-action-sm-813d79e2a873da9f14bd3ad4d736a9cb.png)##### Endpoint in Action[â](#endpoint-in-action-2 "Direct link to Endpoint in Action")

![Interior endpoint result](/docs/assets/images/v5-interior-action-sm-850ab622444040ba7471920e8d661705.png)### Super Resolution Endpoint[â](#super-resolution-endpoint "Direct link to Super Resolution Endpoint")

Use this endpoint to get a super resolution version of an image by passing its URL.

##### Endpoint in Action[â](#endpoint-in-action-3 "Direct link to Endpoint in Action")

![Super Resolution endpoint result](/docs/assets/images/super-res-action-sm-03f81fbaeda5b4d52cc825de8405df35.png)### Image Mixer[â](#image-mixer "Direct link to Image Mixer")

Image mixers merges two images togethers to produce an eye catching result.

### Remove Background and Create Mask[â](#remove-background-and-create-mask "Direct link to Remove Background and Create Mask")

Use this endpoint to remove background and(or) create mask.

### Magic Mix[â](#magic-mix "Direct link to Magic Mix")

Use this endpoint to generate an eye catching image blend with prompt

### Outpainting[â](#outpainting "Direct link to Outpainting")

Use this endpoint to outpaint

### Blip Diffusion[â](#blip-diffusion "Direct link to Blip Diffusion")

Use this endpoint to for blip diffusion

### Fashion[â](#fashion "Direct link to Fashion")

Use this endpoint to wear a cloth image on an existing model body.

Playground[â](#playground "Direct link to Playground")
--------------------------------------------------------

You can try the available endpoints in our [Playground](https://stablediffusionapi.com/playground?channel=apiv5) section, just make sure to [sign up](https://stablediffusionapi.com/register) first.

[PreviousImage Editing](/docs/category/image-editing)[NextOutpainting](/docs/image-editing/outpainting)* [Overview](#overview)
* [Available Endpoints](#available-endpoints)
	+ [Image Guided Edit](#image-guided-edit)
	+ [Depth to Image](#depth-to-image)
	+ [Super Resolution Endpoint](#super-resolution-endpoint)
	+ [Image Mixer](#image-mixer)
	+ [Remove Background and Create Mask](#remove-background-and-create-mask)
	+ [Magic Mix](#magic-mix)
	+ [Outpainting](#outpainting)
	+ [Blip Diffusion](#blip-diffusion)
	+ [Fashion](#fashion)
* [Playground](#playground)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



