




Dreambooth Finetunning API \| Stable Diffusion API Documentation








[Skip to main content](#docusaurus_skipToContent_fallback)[![Stable Diffusion Logo](/docs/img/SD-logo.png)![Stable Diffusion Logo](/docs/img/SD-logo.png)](https://stablediffusionapi.com)[Enterprise](https://stablediffusionapi.com/enterprise)[Pricing](https://stablediffusionapi.com/#pricing)[Blog](https://stablediffusionapi.com/blog)[Docs](https://stablediffusionapi.com/docs)[Playground](https://stablediffusionapi.com/playground)[Models](https://stablediffusionapi.com/models)[API Catalogue](https://stablediffusionapi.com/catalogue)* [Getting Started](/docs/)
* [Stable Diffusion API](/docs/category/stable-diffusion-api)
* [Train Model](/docs/category/train-model)
	+ [API Overview](/docs/train-model/overview)
	+ [Lora Training](/docs/train-model/lora-finetune)
	+ [Dreambooth Training (V2\)](/docs/train-model/finetune-v2)
	+ [Dreambooth Training](/docs/train-model/finetune)
	+ [Training Status](/docs/train-model/finetune-status)
	+ [Get Model List](/docs/train-model/finetune-list)
	+ [Delete Training](/docs/train-model/finetune-delete)
	+ [Cancel Training](/docs/train-model/cancel-training)
	+ [Crop Base64 Image](/docs/train-model/base64-crop)
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
* [Train Model](/docs/category/train-model)
* API Overview
On this pageDreambooth Finetunning API
==========================

Overview[â](#overview "Direct link to Overview")
--------------------------------------------------

The Dreambooth Finetunning API collection is dedicated to model training. 

The available endpoints handle requests for training models using custom images and a base model.

tipRead our handy **[blog article](https://stablediffusionapi.com/blog/stable-diffusion-api/how-to-finetune-dreambooth-model)** about model training, before you dive in.

Available Endpoints[â](#available-endpoints "Direct link to Available Endpoints")
-----------------------------------------------------------------------------------

* [fine\_tune](/docs/train-model/finetune)
* [fine\_tune\_v2](/docs/train-model/finetune-v2)
* [fine\_tune\_status](/docs/train-model/finetune-status)
* [cancle\_training](/docs/train-model/cancel-training)
* [finetune\_list](/docs/train-model/finetune-list)
* [finetune/delete](/docs/train-model/finetune-delete)
* [base64\_crop](/docs/train-model/base64-crop)
* [lora\_finetune](/docs/train-model/lora-finetune)
### Train a Dreambooth Model with Custom Images Endpoint[â](#train-a-dreambooth-model-with-custom-images-endpoint "Direct link to Train a Dreambooth Model with Custom Images Endpoint")

Using this endpoint you can train a Dreambooth model with your own images. You can train a model on any object or person.

### Train a Dreambooth Model with Custom Images (V2\) Endpoint[â](#train-a-dreambooth-model-with-custom-images-v2-endpoint "Direct link to Train a Dreambooth Model with Custom Images (V2) Endpoint")

Using this endpoint you can train a Dreambooth model with your own images. You can train a model on any object or person. 

The second version of the model training endpoint handles requests with more parameters.

### Get Training Status Endpoint[â](#get-training-status-endpoint "Direct link to Get Training Status Endpoint")

This endpoint allows to check the current status of the model training and the estimated time remaining for its completion if not completed yet.

### Cancel Training Request Endpoint[â](#cancel-training-request-endpoint "Direct link to Cancel Training Request Endpoint")

This endpoint is used to cancel a Dreambooth model training request.

### Delete Dreambooth Request Endpoint[â](#delete-dreambooth-request-endpoint "Direct link to Delete Dreambooth Request Endpoint")

This endpoint is used to delete a Dreambooth model training request.

### Get Model List Endpoint[â](#get-model-list-endpoint "Direct link to Get Model List Endpoint")

This endpoint returns an array with the IDs of the models that you have created.

### Upload Base64 Image and Crop Endpoint[â](#upload-base64-image-and-crop-endpoint "Direct link to Upload Base64 Image and Crop Endpoint")

This endpoint is used to upload an image in Base64 Format and crop it. 

### Train a Lora Model with Custom Images Endpoint[â](#train-a-lora-model-with-custom-images-endpoint "Direct link to Train a Lora Model with Custom Images Endpoint")

Using this endpoint you can train a lora model with your own images. You can train a model on any object or person.

Playground[â](#playground "Direct link to Playground")
--------------------------------------------------------

You can try the available endpoints in our [Playground](https://stablediffusionapi.com/playground?channel=dreambooth-training) section, just make sure to [sign up](https://stablediffusionapi.com/register) first.

[PreviousTrain Model](/docs/category/train-model)[NextLora Training](/docs/train-model/lora-finetune)* [Overview](#overview)
* [Available Endpoints](#available-endpoints)
	+ [Train a Dreambooth Model with Custom Images Endpoint](#train-a-dreambooth-model-with-custom-images-endpoint)
	+ [Train a Dreambooth Model with Custom Images (V2\) Endpoint](#train-a-dreambooth-model-with-custom-images-v2-endpoint)
	+ [Get Training Status Endpoint](#get-training-status-endpoint)
	+ [Cancel Training Request Endpoint](#cancel-training-request-endpoint)
	+ [Delete Dreambooth Request Endpoint](#delete-dreambooth-request-endpoint)
	+ [Get Model List Endpoint](#get-model-list-endpoint)
	+ [Upload Base64 Image and Crop Endpoint](#upload-base64-image-and-crop-endpoint)
	+ [Train a Lora Model with Custom Images Endpoint](#train-a-lora-model-with-custom-images-endpoint)
* [Playground](#playground)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



