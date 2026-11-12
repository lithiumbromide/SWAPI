---
title: "ModelDoc::SceneUserName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SceneUserName.htm"
---

# ModelDoc::SceneUserName

This property is obsolete and has been superseded by [ModelDoc2::SceneUserName](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SceneUserName.htm).

Description

The method gets and sets the scene user name.

Syntax (OLE Automation)

newName = ModelDoc.SceneUserName (VB Get property)

ModelDoc.SceneUserName = Name (VB Set property)

newName = ModelDoc.GetSceneUserName ( ) (C++ Get property)

ModelDoc.SetSceneUserName ( Name ) (C++ Set property)

| Property: | (BSTR) Name | User name of the scene |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->get_SceneUserName( &Name )

status = ModelDoc->put_SceneUserName( Name )

| Property: | (BSTR) Name | User name of the scene |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
