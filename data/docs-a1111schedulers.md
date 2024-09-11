




A1111 Schedulers \| Stable Diffusion API Documentation








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
* [Text To 3D](/docs/category/text-to-3d)
* [Uncensored Chat](/docs/uncensored-chat)
* [A1111 Schedulers](/docs/a1111schedulers)
* [FAQ](/docs/faq)
* [Postman Collection](https://documenter.getpostman.com/view/18679074/2s83zdwReZ)
* [Support](https://discord.gg/UxqnDu7j3r)
* 
* 
* A1111 Schedulers
On this pageA1111 Schedulers
================

A1111 Diffusers Scheduler Mapping[â](#a1111-diffusers-scheduler-mapping "Direct link to A1111 Diffusers Scheduler Mapping")
-----------------------------------------------------------------------------------------------------------------------------



| A1111 | Stable Diffusion API | Additional Parameters \& Notes |
| --- | --- | --- |
| DPM\+\+ 2M | DPMSolverMultistepScheduler |  |
| DPM\+\+ 2M Karras | DPMSolverMultistepScheduler | init with `use_karras_sigmas="yes"` |
| DPM\+\+ 2M SDE | DPMSolverMultistepScheduler | init with `algorithm_type="dpmsolver+++"` |
| DPM\+\+ 2M SDE Karras | DPMSolverMultistepScheduler | init with `algorithm_type="dpmsolver+++"` and `use_karras_sigmas="yes"` |
| DPM\+\+ 2S a | N/A | Very similar to DPMSolverMultistepScheduler |
| DPM\+\+ 2S a Karras | N/A | Very similar to DPMSolverMultistepScheduler with use\_karras\_sigmas\="yes" |
| DPM\+\+ SDE | DPMSolverSinglestepScheduler |  |
| DPM\+\+ SDE Karras | DPMSolverSinglestepScheduler | init with `use_karras_sigmas="yes"` |
| DPM2 | KDPM2DiscreteScheduler |  |
| DPM2 Karras | KDPM2DiscreteScheduler | init with `use_karras_sigmas="yes"` |
| DPM2 a | KDPM2AncestralDiscreteScheduler |  |
| DPM2 a Karras | KDPM2AncestralDiscreteScheduler | init with `use_karras_sigmas="yes"` |
| DPM adaptive | N/A |  |
| DPM fast | N/A |  |
| Euler | EulerDiscreteScheduler |  |
| Euler a | EulerAncestralDiscreteScheduler |  |
| Heun | HeunDiscreteScheduler |  |
| LMS | LMSDiscreteScheduler |  |
| LMS Karras | LMSDiscreteScheduler | Init with `use_karras_sigmas="yes"` |
| N/A | DEIS |  |
| N/A | UniPCMultistepScheduler |  |
| N/A | LCMScheduler |  |

[PreviousUncensored Chat](/docs/uncensored-chat)[NextFAQ](/docs/faq)* [A1111 Diffusers Scheduler Mapping](#a1111-diffusers-scheduler-mapping)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



