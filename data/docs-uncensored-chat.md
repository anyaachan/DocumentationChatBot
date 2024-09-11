




Uncensored Chat \| Stable Diffusion API Documentation








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
* Uncensored Chat
On this pageUncensored Chat
===============

Overview[â](#overview "Direct link to Overview")
--------------------------------------------------

Uncensored chat endpoint allows you to create chat conversation and get responses based on the conversation. It is very flexible such that it could answer any question without restriction of answer.

Request[â](#request "Direct link to Request")
-----------------------------------------------


```
--request POST 'https://stablediffusionapi.com/api/v5/uncensored_chat' \  

```
Send a `POST` request to <https://stablediffusionapi.com/api/v5/uncensored_chat> endpoint and append the response of the api back to the request.

Attributes[â](#attributes "Direct link to Attributes")
--------------------------------------------------------



| Parameter | Type | Description |
| --- | --- | --- |
| **key** | String | Your API Key used for request authorization |
| **messages** | Array | It accepts the **role** and **content** key. The **role** accepts the value of `user` or `assistant` while the **content** accepts the chat description |
| **max\_tokens** | Int | The maximum number of token |

Example[â](#example "Direct link to Example")
-----------------------------------------------

### Body[â](#body "Direct link to Body")

Body Raw
```
{  
"key": "",  
"messages": [  
        {  
            "role": "user",  
            "content": "write php function to make api call"  
        },  
    ],  
"max_tokens": 1000  
}  

```
Once the endpoint is called, the sample response looks like so;

Body Raw
```
{  
    "status": "success",  
    "message": "Here is an example of a PHP function that makes an API call using the cURL extension:\n  
                \nfunction make_api_call($url, $data = []) {\n    $ch = curl_init();\n    curl_setopt($ch, CURLOPT_URL, $url);\n    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);\n    curl_setopt($ch, CURLOPT_POST, true);\n    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));\n    curl_setopt($ch, CURLOPT_HTTPHEADER, ['Content-Type: application/json']);\n    $response = curl_exec($ch);\n    curl_close($ch);\n    return $response;\n}\n",  
    "meta": {  
        "messages": [  
            {  
                "role": "user",  
                "content": "write php function to make api call"  
            }  
        ],  
        "max_tokens": 1000,  
        "temperature": 1,  
        "top_p": 1,  
        "presence_penalty": 0,  
        "frequency_penalty": 0,  
        "track_id": null,  
        "webhook": null  
    }  
}  

```
To continue the next API call, append the object of property `role` and `content` to the **messages** array where the `role` value is **assistant** and the `content` value is the response `message` from the previous call. After that, append another object of same property and pass `role` value as **user** and `content` value as your new description to continue the chat. The request will look like so;

Body Raw
```
  
{  
"key": "",  
"messages": [  
        {  
            "role": "user",  
            "content": "write php function to make api call"  
        },  
        {  
            "role":"assistant",  
            "content":"Here is an example of a PHP function that makes an API call using the cURL extension:\n  
                \nfunction make_api_call($url, $data = []) {\n    $ch = curl_init();\n    curl_setopt($ch, CURLOPT_URL, $url);\n    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);\n    curl_setopt($ch, CURLOPT_POST, true);\n    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));\n    curl_setopt($ch, CURLOPT_HTTPHEADER, ['Content-Type: application/json']);\n    $response = curl_exec($ch);\n    curl_close($ch);\n    return $response;\n}\n"  
        },  
        {  
            "role": "user",  
            "content": "write function to make api call to openai"  
        },  
  
    ],  
"max_tokens": 1000  
}  

```
The response of the above request looks like so

Body Raw
```
{  
    "status": "success",  
    "message": " Here is an example of a PHP function that makes an API call to OpenAI using the curl_ext extension:\n  
    \nfunction make_openai_api_call($endpoint, $params) {\n    $ch = curl_init();\n    curl_setopt($ch, CURLOPT_URL, $endpoint);\n    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);\n    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);\n    curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 2);\n    curl_setopt($ch, CURLOPT_HTTPHEADER, ['Content-Type: application/json']);\n    curl_setopt($ch, CURLOPT_POST, true);\n    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($params));\n    $response = curl_exec($ch);\n    curl_close($ch);\n    return $response;\n}\n",  
    "meta": {  
        "messages": [  
            {  
                "role": "user",  
                "content": "write php function to make api call"  
            },  
            {  
                "role": "assistant",  
                "content": "Here is an example of a PHP function that makes an API call using the cURL extension:\n  
                  \nfunction make_api_call($url, $data = []) {\n    $ch = curl_init();\n    curl_setopt($ch, CURLOPT_URL, $url);\n    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);\n    curl_setopt($ch, CURLOPT_POST, true);\n    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));\n    curl_setopt($ch, CURLOPT_HTTPHEADER, ['Content-Type: application/json']);\n    $response = curl_exec($ch);\n    curl_close($ch);\n    return $response;\n}\n  
                  "  
            },  
            {  
                "role": "user",  
                "content": "write function to make api call to openai"  
            }  
        ],  
        "max_tokens": 1000,  
        "temperature": 1,  
        "top_p": 1,  
        "presence_penalty": 0,  
        "frequency_penalty": 0,  
        "track_id": null,  
        "webhook": null  
    }  
}  
  

```
Repeat the process as many times as possible until you are satisfied with the results

Model being used is Mistral 7B Instruct\-v0\.1

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
  "messages": [  
          {  
              "role": "user",  
              "content": "write php function to make api call"  
          },  
      ],  
  "max_tokens": 1000  
});  
  
var requestOptions = {  
  method: 'POST',  
  headers: myHeaders,  
  body: raw,  
  redirect: 'follow'  
};  
  
fetch("https://stablediffusionapi.com/api/v5/uncensored_chat", requestOptions)  
  .then(response => response.text())  
  .then(result => console.log(result))  
  .catch(error => console.log('error', error));  

```

```
<?php  
  
$payload = [  
  "key" => "",  
  "messages" => [  
          [  
              "role": "user",  
              "content": "write php function to make api call"  
          ],  
      ],  
  "max_tokens" => 1000  
];  
  
$curl = curl_init();  
  
curl_setopt_array($curl, array(  
  CURLOPT_URL => 'https://stablediffusionapi.com/api/v5/uncensored_chat',  
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
  'url': 'https://stablediffusionapi.com/api/v5/uncensored_chat',  
  'headers': {  
    'Content-Type': 'application/json'  
  },  
  body: JSON.stringify({  
    "key": "",  
    "messages": [  
            {  
                "role": "user",  
                "content": "write php function to make api call"  
            },  
        ],  
    "max_tokens": 1000  
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
  
url = "https://stablediffusionapi.com/api/v5/uncensored_chat"  
  
payload = json.dumps({  
  "key": "",  
  "messages": [  
          {  
              "role": "user",  
              "content": "write php function to make api call"  
          },  
      ],  
  "max_tokens": 1000  
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
RequestBody body = RequestBody.create(mediaType, "{\n  \"key\": \"\",\n  \"messages\": [\n      {\n          \"role\":\"user\",\n          \"content\":\"write a php function to make an api call\"\n      }\n  ],\n  \"max_tokens\": 1000\n}");  
Request request = new Request.Builder()  
  .url("https://stablediffusionapi.com/api/v5/uncensored_chat")  
  .method("POST", body)  
  .addHeader("Content-Type", "application/json")  
  .build();  
Response response = client.newCall(request).execute();  

```
### Response[â](#response "Direct link to Response")


```
{  
    "status": "success",  
    "message": "Here is an example of a PHP function that makes an API call using the cURL extension:\n  
                \nfunction make_api_call($url, $data = []) {\n    $ch = curl_init();\n    curl_setopt($ch, CURLOPT_URL, $url);\n    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);\n    curl_setopt($ch, CURLOPT_POST, true);\n    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));\n    curl_setopt($ch, CURLOPT_HTTPHEADER, ['Content-Type: application/json']);\n    $response = curl_exec($ch);\n    curl_close($ch);\n    return $response;\n}\n",  
    "meta": {  
        "messages": [  
            {  
                "role": "user",  
                "content": "write php function to make api call"  
            }  
        ],  
        "max_tokens": 1000,  
        "temperature": 1,  
        "top_p": 1,  
        "presence_penalty": 0,  
        "frequency_penalty": 0,  
        "track_id": null,  
        "webhook": null  
    }  
}  

```
[PreviousImage to 3D](/docs/text-to-3d/imageto3d)[NextA1111 Schedulers](/docs/a1111schedulers)* [Overview](#overview)
* [Request](#request)
* [Attributes](#attributes)
* [Example](#example)
	+ [Body](#body)
	+ [Request](#request-1)
	+ [Response](#response)
Â·Â·Â© 2023 Stable Diffusion API. All rights reserved.



