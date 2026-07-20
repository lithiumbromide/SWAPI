---
title: "Getting Started"
project: "PDM Pro Web API Help"
interface: ""
member: ""
kind: "topic"
source: "pdmprowebapihelp/GettingStarted.html"
---

# Getting Started

- [Prerequisites](#Prerequisites)
- [Background](#research)
- [Javascript, Python, and C# Console Examples](#examples)
- [Install and Enable CORS](#CORS)
- [Event hooks](#hooks)

##### Prerequisites

In order to build applications that use the operations in the SOLIDWORKS PDM Professional Web API, you need:

- SOLIDWORKS PDM Professional

Read the**Installation Guide.pdf**in**c:\Program Files\SOLIDWORKS Corp\SOLIDWORKS PDM\Lang\ lang**. Follow the outline in**Chapter 2 Installation Overview**and all the instructions in ensuing chapters to install required and optional (SOLIDWORKS PDM Professional only) components.

- SOLIDWORKS PDM Web API Server (SOLIDWORKS PDM Professional only)

In the installation guide, follow the instructions under**Chapter 5 Installing SOLIDWORKS PDM - Installing SOLIDWORKS PDM Web API Server.**At**https://help.solidworks.com**select a version and a language and navigate to**SOLIDWORKS PDM >****SOLIDWORKS PDM Administration Tool > Administering Web API Servers (For SOLIDWORKS PDM Professional only)**). Using the PDM Administration Tool, you must add the web API server, add a vault to the web API server, and configure the vault.

- Configure IIS Application Pools

If you are using your computer as both the web API server and the web client, in order to have permission to stage files for check-in you may need to change the Application Pool entity of your web server to be your computer login**.**

1. In IIS under your local host in the Connections list, click

  Application Pools

  .
2. Right-click SOLIDWORKS PDM WebAPI and select

  Advanced Settings

  .
3. Change

  Process Model > Identity

  to your computer login.
4. Click

  OK

  .

Read more about IIS configuration at[https://learn.microsoft.com/en-us/iis](https://learn.microsoft.com/en-us/iis).

- Cross-origin resource sharing (CORS)

If you are not familiar with CORS, then please do an internet search for "Cross-origin resource sharing"**.**CORS is required if you use browser-based programming languages like Java, PHP, Javascript, Python, NodeJs etc. or access the PDM Pro Web API from a different domain. If Internet Information Services (IIS) is not already active, do an internet search of "how to open internet information services", and follow the instructions. Then[install CORS](#CORS)and configure the SWPDMWebAPI web site in IIS to enable CORS. See the Javascript and Python examples in[api/{vaultName}/authenticate](PDM%20Pro%20API_ws~r-api-{vaultName}-authenticate~o-HttpPost.html).

- Postman

Some examples in this help demonstrate usage of PDM Pro Web API endpoints using Postman collections. Each collection is a typical use case involving multiple endpoints. Postman provides an easy interface for you to verify HTTP requests using the PDM Pro Web API. Once you are satisfied that the API is working in Postman, you can confidently develop your own applications in any language. You can export the HTTP requests you set up in Postman to another language using the**Code****(</>)**button in the right sidebar of Postman.

Download and install Postman. Use an internet search engine to locate this free software. https://www.postman.com/downloads/

Click and save the following environment collection to your computer. Then drag/drop it into Postman:

**WebAPI.postman_environment.json**

Click**Environment Quick Look**next to the WebAPI enviroment in Postman to edit the following global variables (and possibly others) to work with your installation:

- host
- vaultName
- UserName
- Password
- basicURL
- token
- jsonTypeHeader

Look for links to other Postman collections in this help that you can drag/drop into Postman. The collections all contain an authenticate HTTP request that you must send to obtain a bearer token to send with all other HTTP requests.

- Microsoft Visual Studio (for C# and ASP.NET)

You can use a .NET project template to create a C# Console App (.NET Core) or an ASP.NET Web Application (.NET Framework) that accesses the PDM Pro Web API. See the C# console application example in[api/{vaultName}/authenticate](PDM%20Pro%20API_ws~r-api-{vaultName}-authenticate~o-HttpPost.html).

##### Background

The SOLIDWORKS PDM Professional Web API is an extension of Microsoft's[ASP.NET Web API](https://docs.microsoft.com/en-us/aspnet/web-api/)which is a framework that allows you to create Representational State Transfer (REST) applications on the .NET Framework.

If you are not familiar with REST, then please do an internet search of:

- Representational state transfer (REST)
- ASP.NET REST APIs with .NET and C#

Hypertext Transfer Protocol (HTTP) enables communication between clients and servers through a request-response protocol.

If you are not familiar with HTTP, then please do an internet search of:

- HTTP Methods

Your web service application can authenticate logged-in users and set up[JSON Web Tokens (JWT)](https://jwt.io/introduction)Bearer tokens to securely authorize and restrict API access. You must obtain a bearer token to send with most HTTP requests of the PDM Pro Web API.

Read about the importance of[API Security](https://www.freecodecamp.org/news/authenticate-and-authorize-apis-in-dotnet5/).

##### Javascript, Python, and C# Console Examples

You will find examples scattered throughout the help. To get started with authenticating users, authorizing access, and using the GET and POST HTTP methods, follow the examples in[api/{vaultName}/authenticate](PDM%20Pro%20API_ws~r-api-{vaultName}-authenticate~o-HttpPost.html).

##### Install and Enable CORS

If you use browser-based programming languages like Java, PHP, Javascript, Python, NodeJs etc., you need CORS. The CORS extension can be downloaded and installed from Microsoft and enabled in IIS by editing the WebAPI**web.config**file as follows:

1. Go to**https://www.iis.net/downloads/microsoft/iis-cors-module**. Download and install the CORS module.
2. Navigate to the PDM Pro Web API installation location (e.g.,**C:\inetpub\wwwroot\SOLIDWORKSPDM\WebApi**).
3. Open**web.config**in any text editor with Administrator privileges (Notepad or Notepad++, for example).
4. Add the following lines to the <configuration><system.webServer> section:
<cors enabled='true'>
<add origin='*'>
<allowHeaders allowAllRequestedHeaders='true' />
<allowMethods>
<add method='GET' />
<add method='POST' />
<add method='PUT' />
<add method='DELETE' />
</allowMethods>
</add>
</cors>

The <system.webServer> section should look like this:

<system.webServer>
<security>
<requestFiltering>
<requestLimits maxAllowedContentLength='4294967295' />
</requestFiltering>
</security>
<handlers>
<remove name='ExtensionlessUrlHandler-Integrated-4.0' />
<remove name='OPTIONSVerbHandler' />
<remove name='TRACEVerbHandler' />
<add name='Owin' verb=' path='*' type='Microsoft.Owin.Host.SystemWeb.OwinHttpHandler, Microsoft.Owin.Host.SystemWeb' />
<add name='ExtensionlessUrlHandler-Integrated-4.0' path='*.' verb='*' type='System.Web.Handlers.TransferRequestHandler' preCondition='integratedMode,runtimeVersionv4.0' />
</handlers>
<cors enabled='true'>
<add origin='*'>
<allowHeaders allowAllRequestedHeaders='true' />
<allowMethods>
<add method='GET' />
<add method='POST' />
<add method='PUT' />
<add method='DELETE' />
</allowMethods>
</add>
</cors>
</system.webServer>

5. Save**web.config**.

6. Open the IIS Manager.

7. Stop the SWPDMWebAPI site.

8. Stop the SOLIDWORKS PDM WebAPI application pool.

9. Restart the SOLIDWORKS PDM WebAPI application pool.

10. Restart the SWPDMWebAPI site.

##### Event hooks

As of 2025, PDM Pro Web API provides support for configuring and handling vault events and managing custom hook add-in DLLs.

Click and save the following JSON collections to your computer. Then drag/drop them into Postman:

**HooksManagement.postman_collection.json**

**GetPostFileServerRoot.postman_collection.json**

For details, see the[Web Event Hooks Programming Guide](PDMProWebAPI_Webhooks_Programming_Guide.html).
