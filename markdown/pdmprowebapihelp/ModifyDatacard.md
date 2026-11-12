---
title: "Modify a Vault File's Datacard Variable Values Example (Javascript)"
project: ""
interface: ""
member: ""
kind: "example"
source: "pdmprowebapihelp/ModifyDatacard.html"
---

# Modify a Vault File's Datacard Variable Values Example (Javascript)

| This example uses JSON objects. Do not try to run this example from the compiled help (chm). The browser that underpins compiled help is Microsoft Internet Explorer, which does not recognize JSON objects. To recreate this example in a supported web browser: Right-click in this page and select View source . Save the file as an HTML file. Open the HTML file in a supported web browser (Microsoft Edge, Google Chrome, or Mozilla Firefox). This example authenticates credentials that you enter in a form, checks out a SOLIDWORKS file, modifies the file's datacard, creates a changeset, adds the modified file to the changeset, and checks in the changeset. Follow the Getting Started instructions. Ensure that a Quick Start data card exists. (A Quick Start data card for SOLIDWORKS files is optionally created during vault setup.) Ensure that at least one SOLIDWORKS file is checked into the root folder (folder Id = 1) of your vault. In the form below, enter the machine name where your web server is hosted, your web server's application port, a PDM Pro vault name, and your PDM Pro Admin credentials. Click Authenticate . Examine the Response text area for the JSON web token. Click Find IDs to get the IDs of all files in the root folder of your vault. Examine the Response text area and locate one SOLIDWORKS part's ID, version, and folder ID. Enter the file's version in the Version field, file ID in the FileID field, and the root folder ID in the FolderID field. Click Check out SOLIDWORKS file . Click Display the file's data card . Examine the Response text area for file's data card values. Inspect the first variable (Project Name). Note the VarId (48). Enter the 48 in the ID of Project Name variable field. Click Change variable value to change the Project Name value to PDM Pro Web API. Examine the Response text area. Click Create change set . Examine the Response text area for the changeset ID. Enter the changeset ID in the Changeset ID field. Click Add files to changeset . Click Check in file . NOTES: Errors are also printed to the Response text area. |
| --- |
|  |
