




Text to Audio Endpoint \| Stable Diffusion API Documentation








[Skip to main content](#docusaurus_skipToContent_fallback)[![Stable Diffusion Logo](/docs/img/SD-logo.png)![Stable Diffusion Logo](/docs/img/SD-logo.png)](https://stablediffusionapi.com)[Enterprise](https://stablediffusionapi.com/enterprise)[Pricing](https://stablediffusionapi.com/#pricing)[Blog](https://stablediffusionapi.com/blog)[Docs](https://stablediffusionapi.com/docs)[Playground](https://stablediffusionapi.com/playground)[Models](https://stablediffusionapi.com/models)[API Catalogue](https://stablediffusionapi.com/catalogue)* [Getting Started](/docs/)
* [Stable Diffusion API](/docs/category/stable-diffusion-api)
* [Train Model](/docs/category/train-model)
* [Community Models API](/docs/category/community-models-api)
* [Text To Video](/docs/category/text-to-video)
* [Community Models API V4](/docs/category/community-models-api-v4)
* [MISCS](/docs/category/miscs)
* [ControlNet](/docs/category/controlnet)
* [Voice Cloning](/docs/category/voice-cloning)
	+ [API Overview](/docs/voice-cloning/overview)
	+ [Text to Audio](/docs/voice-cloning/text-to-audio)
	+ [Text to Voice](/docs/voice-cloning/text-to-voice)
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
* [Voice Cloning](/docs/category/voice-cloning)
* Text to Audio
On this pageText to Audio Endpoint
======================

* [text\_to\_audio](/docs/voice-cloning/text-to-audio)
* [text\_to\_voice](/docs/voice-cloning/text-to-voice)
Overview[â](#overview "Direct link to Overview")
--------------------------------------------------

Text to audio endpoint allows you to create an audio by passing in the text and a valid audio url. The result produces an audio with the same sound as the audio url that was passed

Request[â](#request "Direct link to Request")
-----------------------------------------------


```
--request POST 'https://stablediffusionapi.com/api/v5/text_to_audio' \  

```
Make a `POST` request to <https://stablediffusionapi.com/api/v5/text_to_audio> endpoint and pass the required parameters as a request body. 

Body Attributes[â](#body-attributes "Direct link to Body Attributes")
-----------------------------------------------------------------------



| Parameter | Description |
| --- | --- |
| **key** | Your API Key used for request authorization |
| **prompt** | Text prompt with description of the audio you want to generate |
| **init\_audio** | A valid audio url you want it voice cloned |
| **language** | The language of the voice. As of now, only **english** is supported |
| **decoder\_iterations** | Decorator iteration number |
| **webhook** | Set an URL to get a POST API call once the image generation is complete. |
| **track\_id** | This ID is returned in the response to the webhook API call. This will be used to identify the webhook request. |

Example[â](#example "Direct link to Example")
-----------------------------------------------

### Body[â](#body "Direct link to Body")

Body
```
{     
 "key": "",  
 "prompt":"Narrative voices capable of pronouncing terminologies & acronyms in training and ai learning materials.",  
 "init_audio":"https://pub-f3505056e06f40d6990886c8e14102b2.r2.dev/audio/tom_hanks_1.wav",  
 "language":"english",  
 "decoder_iterations": 30,  
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
  "key": "",  
  "prompt":"Narrative voices capable of pronouncing terminologies & acronyms in training and ai learning materials.",  
  "init_audio":"https://pub-f3505056e06f40d6990886c8e14102b2.r2.dev/audio/tom_hanks_1.wav",  
  "language":"english",  
  "decoder_iterations": 30,  
  "webhook": null,  
  "track_id": null  
});  
  
var requestOptions = {  
  method: 'POST',  
  headers: myHeaders,  
  body: raw,  
  redirect: 'follow'  
};  
  
fetch("https://stablediffusionapi.com/api/v5/text_to_audio", requestOptions)  
  .then(response => response.text())  
  .then(result => console.log(result))  
  .catch(error => console.log('error', error));  

```

```
<?php  
  
$payload = [  
  "key" => "",  
  "prompt" => "Narrative voices capable of pronouncing terminologies & acronyms in training and ai learning materials.",  
  "init_audio" => "https://pub-f3505056e06f40d6990886c8e14102b2.r2.dev/audio/tom_hanks_1.wav",  
  "language" => "english",  
  "decoder_iterations" => 30,  
  "webhook" => null,   
  "track_id" => null   
];  
  
$curl = curl_init();  
  
curl_setopt_array($curl, array(  
  CURLOPT_URL => 'https://stablediffusionapi.com/api/v5/text_to_audio',  
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
  'url': 'https://stablediffusionapi.com/api/v5/text_to_audio',  
  'headers': {  
    'Content-Type': 'application/json'  
  },  
  body: JSON.stringify({  
    "key": "",  
    "prompt":"Narrative voices capable of pronouncing terminologies & acronyms in training and ai learning materials.",  
    "init_audio":"https://pub-f3505056e06f40d6990886c8e14102b2.r2.dev/audio/tom_hanks_1.wav",  
    "language":"english",  
    "decoder_iterations": 30,  
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
  
url = "https://stablediffusionapi.com/api/v5/text_to_audio"  
  
payload = json.dumps({  
  "key": "",  
  "prompt":"Narrative voices capable of pronouncing terminologies & acronyms in training and ai learning materials.",  
  "init_audio":"https://pub-f3505056e06f40d6990886c8e14102b2.r2.dev/audio/tom_hanks_1.wav",  
  "language":"english",  
  "decoder_iterations": 30,  
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
RequestBody body = RequestBody.create(mediaType, "{\n    \"key\":\"\",\n    \"prompt\":\"Narrative voices capable of pronouncing terminologies & acronyms in training and ai learning materials.\",\n    \"init_audio\":\"https://pub-f3505056e06f40d6990886c8e14102b2.r2.dev/audio/tom_hanks_1.wav\",\n    \"language\":\"arabic\",\n    \"decoder_iterations\": 30\n}");  
Request request = new Request.Builder()  
  .url("https://stablediffusionapi.com/api/v5/text_to_audio")  
  .method("POST", body)  
  .addHeader("Content-Type", "application/json")  
  .build();  
Response response = client.newCall(request).execute();  

```
### Response[â](#response "Direct link to Response")


```
{  
    "status": "success",  
    "generationTime": 6.007939100265503,  
    "id": 621,  
    "output": [  
        "https://pub-3626123a908346a7a8be8d9295f44e26.r2.dev/generations/3fdf4b44-7617-4175-b64f-0fd5eda947a5.wav"  
    ],  
    "meta": {  
        "decoder_iterations": 30,  
        "file_prefix": "3fdf4b44-7617-4175-b64f-0fd5eda947a5",  
        "init_audio": "https://pub-f3505056e06f40d6990886c8e14102b2.r2.dev/audio/tom_hanks_1.wav",  
        "prompt": "Narrative voices capable of pronouncing terminologies & acronyms in training and ai learning materials.",  
        "language": "arabic",  
        "outdir": "out",  
        "seed": 1  
    }  
}  

```
[PreviousAPI Overview](/docs/voice-cloning/overview)[NextText to Voice](/docs/voice-cloning/text-to-voice)* [Overview](#overview)
* [Request](#request)
* [Body Attributes](#body-attributes)
* [Example](#example)
	+ [Body](#body)
	+ [Request](#request-1)
	+ [Response](#response)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



