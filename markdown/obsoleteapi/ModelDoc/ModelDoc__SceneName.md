---
title: "ModelDoc::SceneName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SceneName.htm"
---

# ModelDoc::SceneName

This property is obsolete and has been superseded by [ModelDoc2::SceneName](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SceneName.htm).

Description

This property gets and sets the scene name.

Syntax (OLE Automation)

newName = ModelDoc.SceneName (VB Get property)

ModelDoc.SceneName = Name (VB Set property)

newName = ModelDoc.GetSceneName ( ) (C++ Get property)

ModelDoc.SetSceneName ( Name ) (C++ Set property)

| Property: | (BSTR) Name | Name of the scene |
| --- | --- | --- |

Syntax (Com)

status = ModelDoc->get_SceneName ( &Name)

status = ModelDoc->put_SceneName ( Name )

| Property: | (BSTR) Name | Name of the scene |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
