---
title: "ModelDoc::GetSceneExtProperty"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetSceneExtProperty.htm"
---

# ModelDoc::GetSceneExtProperty

This method is obsolete and has been superseded by [ModelDoc2::GetSceneExtProperty](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetSceneExtProperty.htm).

Description

This method retrieves a float, string, or integer value stored for the scene. The VARIANT type returned is based on the how the data was placed. See ModelDoc::AddSceneExtProperty for details.

Syntax (OLE Automation)

retval = ModelDoc.GetSceneExtProperty ( PropertyId)

| Input: | (long) PropertyId | ID of the property extension |
| --- | --- | --- |
| Return: | (VARIANT) retval | Value stored for the scene extension property |

Syntax (COM)

status = ModelDoc->GetSceneExtProperty ( PropertyId, &retval )

| Input: | (long) PropertyId | ID of the property extension |
| --- | --- | --- |
| Output: | (VARIANT) retval | Value stored for the scene extension property |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
