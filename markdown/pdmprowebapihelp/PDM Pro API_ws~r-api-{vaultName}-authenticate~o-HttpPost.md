---
title: "api/{vaultName}/authenticate (Post)"
project: ""
interface: "r-api-{vaultName}-authenticate"
member: "o-HttpPost"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-authenticate~o-HttpPost.html"
---

# api/{vaultName}/authenticate (Post)

PDM Pro API Web Service

| Post | api/{vaultName}/authenticate |
| --- | --- |

Spacing

Collapse All

Expand All

| PDM Pro API Web Service > Authentication Resource Group : api/{vaultName}/authenticate (Post) |
| --- |

Description

POST: api/{VaultName}/authenticate Use for the authenticate to get authentication token

Authenticates the specified login for the specified vault and returns the authentication token and status.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Name of the vault (required) | string |
| Username | (Body) Login name | string |
| Password | (Body) Password | string |
| Version | (Response) Software version information: Major Minor Build Revision MajorRevision MinorRevision Member of HttpResponseMessage model | Version |
| Content | (Response) Authentication token Member of HttpResponseMessage model | HttpContent |
| StatusCode | (Response) Status code; see https://en.wikipedia.org/wiki/List_of_HTTP_status_codes Member of HttpResponseMessage model | HttpStatusCode |
| ReasonPhrase | (Response) Reason Member of HttpResponseMessage model | string |
| Headers | (Response) Collection of headers Member of HttpResponseMessage model | Collection of Object |
| RequestMessage | (Response) An HttpRequestMessage object that consists of: Version (Version model) Content (HttpContent object consisting of Headers array) Method (HttpMethod object consisting of Method string) RequestUri (URI) Headers (Array of objects) Properties (Dictionary of string [key] and Object [value] Member of HttpResponseMessage model | HttpRequestMessage |
| IsSuccessStatusCode | (Response) True if successful, false if not Member of HttpResponseMessage model | boolean |

Request (application/json, text/json)

Body parameter is an array of Username and Password.

#### Sample Data

```
{
  "Username": "sample string 1",
  "Password": "sample string 2"
}
```

Request (application/xml, text/xml)

Body parameter is an array of Username and Password.

#### Sample Data

```
<UserCredentials xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/SWPDM.Models">
  <Password>sample string 2</Password>
  <Username>sample string 1</Username>
</UserCredentials>
```

Request (application/x-www-form-urlencoded)

Body parameter is an array of Username and Password.

Example

**Python application (*.py):**

#Change the basicUrl, vaultname, and payload variable assignments below for your system

import requests
import json

**basicUrl**= "http://`machine_name:port`/api/"
**vaultname**= "`vault_name`"

# Post api/{vaultName}/authenticate
PostAuthenticateurl = basicUrl+vaultname+"/"+"authenticate"

**payload**= "{\"Password\":\"\",\"Username\":\"Admin\"}"
headers = {
'Content-Type': 'application/json;charset=UTF-8',
'version': '30.0'
}
response = requests.request(
"POST", PostAuthenticateurl, headers=headers, data=payload)
jwtToken = json.loads(response.text)

# This token will be used in all the downsteam APIs
token = jwtToken["JwtString"]

# GET api/{vaultName}/folders/{folderId}/browse
Getbrowsefolderurl = basicUrl+vaultname+"/"+"folders/1/browse"

payload = {}
headers = {
'Authorization': 'Bearer ' + token
}

response = requests.request(
"GET", Getbrowsefolderurl, headers=headers, data=payload)

data = json.loads(response.text)

print("All the File Names inside the folder Id = 1 are : ")
for item in data:
if item["Type"] == 1:
print(" " + item["Name"])

**C# console application:**

//============================================================

// Preconditions:

// 1. A SOLIDWORKS PDM Professional Web Server is running on a host machine web site.

// 2. SOLIDWORKS PDM Professional is installed and configured with a vault, vault view, and Admin user.

// 3. Create a C# console project in Visual Studio.

// 4. Copy the code below into**Program.cs**.

// 5. Change the namespace as needed. Change "localhost" and the port in this application's Url string to your host machine's name and available port.

// 6. Change the vaultName and loginuser.password assignments to your vault name and Admin password.

// Postconditions:

// 1. Authenticates the logged-in user. Deserializes the authentication result to create a JSON Web Tokens (JWT) Bearer token.

// 2. Sends GET requests with the Bearer token to obtain all folders and all users in the vault.

// 3. Inspect the console.

//================================================================

usingNewtonsoft.Json;

usingSystem;

usingSystem.Collections.Generic;

usingSystem.IO;

usingSystem.Linq;

usingSystem.Net;

usingSystem.Text;

usingSystem.Threading.Tasks;

usingSystem.Web.Script.Serialization;

namespaceConsoleWebAPIClientHTTPWebReq

{

classProgram

{

conststringUrl ="http://localhost:8082/api/";

staticstringJwtString =string.Empty;

staticboolAuthorized =false;

conststringvaultName ="2_24_2021";

staticvoidMain(string[] args)

{

try

{

stringurlLogin = Url + vaultName +"/authenticate";

UserCredentials loginUser =newUserCredentials();

loginUser.username ="Admin";

loginUser.password = String.Empty;

stringloginResult = AuthenticateRequest(urlLogin, loginUser);

Authorized = AuthorizationCode(loginResult);

if(Authorized)

{

// Get all the folders in the root folder of the vault

Console.WriteLine(" All folders : \n");

stringurlBrowseAllFolder = Url + vaultName +"/folders/1/browse";

List<ObjectInfo> vaultFolderItems = GetVaultItems(urlBrowseAllFolder);

foreach(var iteminvaultFolderItems)

{

Console.WriteLine(" Folder Name :"+ item.Name);

}

// Get all the users in the vault

Console.WriteLine("\n Vault Users : \n");

stringurlAllUsers = Url + vaultName +"/users";

vaultFolderItems = GetVaultItems(urlAllUsers);

foreach(var iteminvaultFolderItems)

{

Console.WriteLine(" User Name :"+ item.FullName);

Console.WriteLine(" User ID :"+ item.UserInfo.UserId.ToString());

}

}

}

catch(Exception ex)

{

Console.WriteLine(ex.ToString());

}

}

privatestaticList<ObjectInfo> GetVaultItems(stringUrl)

{

varresult = GetResultOfAPI<List<ObjectInfo>>(Url);

returnresult ??newList<ObjectInfo>();

}

publicstaticT GetResultOfAPI<T>(stringdata)

{

T model =default(T);

stringresult = GetRequest(data, JwtString);

try

{

// Convert the GET returned string to a list

// of objects of type specified in GetVaultItems

model = ConvertToType<T>(result);

}

catch(Exception ex)

{

Console.WriteLine(ex.ToString());

}

returnmodel;

}

publicstaticT ConvertToType<T>(stringresponse)

{

// Deserialize the response and convert it to the specified type

returnJsonConvert.DeserializeObject<T>(response);

}

publicstaticboolAuthorizationCode(stringresult)

{

try

{

varjsonConvert =newJavaScriptSerializer();

// Deserialize the authentication result

// and convert it to a JSON Web Token

vartemp = (Dictionary<string,object>)jsonConvert.DeserializeObject(result);

JwtString = temp["JwtString"].ToString();

}

catch(Exception ex)

{

Console.WriteLine(ex.ToString());

}

// Authorize, if the Bearer token is not empty of null

Authorized = !String.IsNullOrEmpty(JwtString);

returnAuthorized;

}

public static string AuthenticateRequest( string url, UserCredentials user)

{

stringresult = String.Empty;

varjsonConvert =newJavaScriptSerializer();

stringjson = jsonConvert.Serialize(user);

varbody = Encoding.UTF8.GetBytes(json);

HttpWebRequestrequest = (HttpWebRequest)WebRequest.Create(url);

request.Method ="POST";

request.ContentType ="application/json";

request.ContentLength = body.Length;

// Get a Stream object to send request data

// using the Stream.Write method

using(Stream stream = request.GetRequestStream())

{

stream.Write(body, 0, body.Length);

stream.Close();

}

try

{

// Sends the HttpWebRequest and waits for the response

using(HttpWebResponse response = (HttpWebResponse)request.GetResponse())

{

// Gets the stream associated with the response

// and pipes it to a higher-level stream reader // with the required encoding format

using(varsr =newStreamReader(response.GetResponseStream()))

{

result = sr.ReadToEnd();

}

response.Close();

}

}

catch(WebException ex)

{

if(ex.Response ==null)

throw;

using(WebResponse response = ex.Response)

{

using(varsr =newStreamReader(response.GetResponseStream()))

{

result = sr.ReadToEnd();

}

}

}

returnresult;

}

publicstaticstringGetRequest(stringurl,stringjwt)

{

// Initialize an HttpWebRequest

HttpWebRequest req = (HttpWebRe quest)WebRequest.Create(url);

req.Accept ="application/json";

req.Headers.Add("Authorization","Bearer "+ jwt);

stringresult = String.Empty;

try

{

// Sends the HttpWebRequest and waits for the response

HttpWebResponse resp = (HttpWebResponse)req.GetRespons e();

// Gets the stream used to read the body of the response

using(varsr =newStreamReader(resp.GetResponseStream()))

{

result = sr.ReadToEnd();

}

}

catch(WebException ex)

{

if(ex.Response ==null)

returnresult;

using(WebResponse response = ex.Response)

{

using(varsr =newStreamReader(response.GetResponseStream()))

{

result = sr.ReadToEnd();

}

}

}

returnresult;

}

}

publicstructUserCredentials

{

publicstringpassword;

publicstringusername;

}

publicclassObjectInfo

{

publicintId {get;set; }

publicstringName {get;set; }

publiclongSize {get;set; }

publicDateTime ModifiedDate {get;set; }

publicintVersion {get;set; }

publicstringState {get;set; }

publicintStateId {get;set; }

publicintParentFolderId {get;set; }

publicstringPath {get;set; }

publicObjectType Type {get;set; }

publicintIsLocked {get;set; }

publicintLockedBy {get;set; }

publicintIsShared {get;set; }

publicintIsToolbox {get;set; }

publicintIsDeleted {get;set; }

publicUserInfo UserInfo {get;set; }

publicstringFullName {get;set; }

publicstringInitials {get;set; }

}

publicenumObjectType

{

Folder = 0,

File = 1,

Bom = 3

}

publicclassUserInfo

{

publicstringUserName {get;set; }

publicintUserId {get;set; }

}

}

Example

[Authentication (JS)](index.html)

|

[Use Search Variables.postman_collection.json](Use%20Search%20Variables.postman_collection.json)

|

[Upload SOLIDWORKS Files to PDM Vault.postman_collection.json](Upload%20SOLIDWORKS%20Files%20to%20PDM%20Vault.postman_collection.json)

|

[Check in SOLIDWORKS Files in PDM Vault.postman_collection.json](Check%20in%20SOLIDWORKS%20Files%20%20in%20PDM%20Vault.postman_collection.json)

|

[Check Out Files in PDM Vault.postman_collection.json](Check%20Out%20Files%20in%20PDM%20Vault.postman_collection.json)

|

[Modify File Datacards.postman_collection.json](Modify%20File%20Datacards.postman_collection.json)

Remarks

Read[Getting Started](GettingStarted.html).

For more information about the data types used in authentication:

- [HttpContent](https://docs.microsoft.com/en-us/dotnet/api/system.net.http.httpcontent?view=net-5.0)
- [HttpRequestMessage](https://docs.microsoft.com/en-us/dotnet/api/system.net.http.httprequestmessage?view=net-5.0)
- [HttpResponseMessage](https://docs.microsoft.com/en-us/dotnet/api/system.net.http.httpresponsemessage?view=net-5.0)
- [HttpStatusCode enumerator](https://docs.microsoft.com/en-us/dotnet/api/system.net.httpstatuscode?view=net-5.0)
- [HttpWebRequest](https://docs.microsoft.com/en-us/dotnet/api/system.net.httpwebrequest?view=net-5.0)
- [HttpWebResponse](https://docs.microsoft.com/en-us/dotnet/api/system.net.httpwebresponse?view=net-5.0)

See Also

[Authentication Resource Group](PDM%20Pro%20API_ws~g-bbaa3f80-71d7-4075-9f18-96b58d1b66e0.html)

|

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
