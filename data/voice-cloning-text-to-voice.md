




Text to Voice Endpoint \| Stable Diffusion API Documentation








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
* Text to Voice
On this pageText to Voice Endpoint
======================

* [text\_to\_audio](/docs/voice-cloning/text-to-audio)
* [text\_to\_voice](/docs/voice-cloning/text-to-voice)
Overview[â](#overview "Direct link to Overview")
--------------------------------------------------

Text to voice endpoint allows you to create an audio by passing a pre\-existing voice\_id from the [list of voices](https://stablediffusionapi.com/voice-lists) and the text input description. The result produces an audio with the same voice\_id passed.

Request[â](#request "Direct link to Request")
-----------------------------------------------


```
--request POST 'https://stablediffusionapi.com/api/v5/text_to_voice' \  

```
Make a `POST` request to <https://stablediffusionapi.com/api/v5/text_to_voice> endpoint and pass the required parameters as a request body. 

Body Attributes[â](#body-attributes "Direct link to Body Attributes")
-----------------------------------------------------------------------



| Parameter | Description |
| --- | --- |
| **key** | Your API Key used for request authorization |
| **voice\_id** | The id of the voice. **[get voice\_id from here](https://stablediffusionapi.com/voice-lists)**. |
| **prompt** | Text prompt with description of the audio you want to generate |
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
 "voice_id":"jack_sparrow",  
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
  "voice_id":"jack_sparrow",  
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
  
fetch("https://stablediffusionapi.com/api/v5/text_to_voice", requestOptions)  
  .then(response => response.text())  
  .then(result => console.log(result))  
  .catch(error => console.log('error', error));  

```

```
<?php  
  
$payload = [  
  "key" => "",  
  "prompt" => "Narrative voices capable of pronouncing terminologies & acronyms in training and ai learning materials.",  
  "voice_id" => "jack_sparrow",  
  "decoder_iterations" => 30,  
  "webhook" => null,   
  "track_id" => null   
];  
  
$curl = curl_init();  
  
curl_setopt_array($curl, array(  
  CURLOPT_URL => 'https://stablediffusionapi.com/api/v5/text_to_voice',  
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
  'url': 'https://stablediffusionapi.com/api/v5/text_to_voice',  
  'headers': {  
    'Content-Type': 'application/json'  
  },  
  body: JSON.stringify({  
    "key": "",  
    "prompt":"Narrative voices capable of pronouncing terminologies & acronyms in training and ai learning materials.",  
    "voice_id":"jack_sparrow",  
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
  
url = "https://stablediffusionapi.com/api/v5/text_to_voice"  
  
payload = json.dumps({  
  "key": "",  
  "prompt":"Narrative voices capable of pronouncing terminologies & acronyms in training and ai learning materials.",  
  "voice_id":"jack_sparrow",  
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
RequestBody body = RequestBody.create(mediaType, "{\n    \"key\":\"\",\n    \"prompt\":\"Narrative voices capable of pronouncing terminologies & acronyms in training and ai learning materials.\",\n    \"voice_id\":\"jack_sparrow\",\n    \"decoder_iterations\": 30\n}");  
Request request = new Request.Builder()  
  .url("https://stablediffusionapi.com/api/v5/text_to_voice")  
  .method("POST", body)  
  .addHeader("Content-Type", "application/json")  
  .build();  
Response response = client.newCall(request).execute();  

```
### Response[â](#response "Direct link to Response")


```
{  
    "status": "success",  
    "generationTime": 5.966439723968506,  
    "id": 622,  
    "output": [  
        "https://pub-3626123a908346a7a8be8d9295f44e26.r2.dev/generations/812c194c-726e-44cb-b6da-4d4ccf5ee02f.wav"  
    ],  
    "meta": {  
        "decoder_iterations": 30,  
        "file_prefix": "812c194c-726e-44cb-b6da-4d4ccf5ee02f",  
        "input_sound_clip": "https://pub-f3505056e06f40d6990886c8e14102b2.r2.dev/audio/I-Captain-Jack-1.mp3",  
        "prompt": "Narrative voices capable of pronouncing terminologies & acronyms in training and ai learning materials.",  
        "language": "english",  
        "outdir": "out",  
        "seed": 1  
    }  
}  

```
[PreviousText to Audio](/docs/voice-cloning/text-to-audio)[NextEnterprise Plan](/docs/category/enterprise-plan)* [Overview](#overview)
* [Request](#request)
* [Body Attributes](#body-attributes)
* [Example](#example)
	+ [Body](#body)
	+ [Request](#request-1)
	+ [Response](#response)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



