---
title: "ModelDoc::AddSceneExtProperty"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__AddSceneExtProperty.htm"
---

# ModelDoc::AddSceneExtProperty

This property is obsolete and has been superseded by [ModelDoc2::AddSceneExtProperty](sldworksAPI.chm::/ModelDoc2/ModelDoc2__AddSceneExtProperty.htm).

Description

This method stores a float, string, or integer value for a scene. This scene extension property is stored on the model document, but is unique to the model's scene. To add the extension property, you must first define the VARIANT type (float, string, or integer), give your variable a value, and then call this method to place the value on the light source for future reference.

Syntax (OLE Automation)

retval = ModelDoc.AddSceneExtProperty ( PropertyExtension)

| Input: | (VARIANT) PropertyExtension | Value you wish to store for the scene |
| --- | --- | --- |
| Return: | (long) retval | Unique identifier returned to allow you to access the Property Extension in the future |

Syntax (COM)

status = ModelDoc->AddSceneExtProperty ( PropertyExtension, &retval )

| Input: | (VARIANT) PropertyExtension | Value you wish to store for the scene |
| --- | --- | --- |
| Output: | (long) retval | Unique identifier returned to allow you to access the Property Extension in the future |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
