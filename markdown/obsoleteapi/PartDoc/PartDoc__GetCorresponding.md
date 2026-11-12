---
title: "PartDoc::GetCorresponding"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PartDoc/PartDoc__GetCorresponding.htm"
---

# PartDoc::GetCorresponding

This method is obsolete and has been superseded by [ModelDocExtension::GetCorresponding](sldworksAPI.chm::/ModelDocExtension/ModelDocExtension__GetCorresponding.htm).

Description

This method gets the object that corresponds to the Dispatch object in the context of the part document.

Syntax (OLE Automation)

*OutputObject = PartDoc.GetCorresponding ( InputObject)

| Input: | (LPDISPATCH) InputObject | Pointer to the Dispatch object |
| --- | --- | --- |
| Output: | (LPDISPATCH ) *OutputObject | Pointer to the corresponding object in the context of the part document |

Syntax (COM)

status = PartDoc->GetCorresponding ( InputObject, &OutputObject)

| Input: | (LPDISPATCH) InputObject | Pointer to the Dispatch object |
| --- | --- | --- |
| Output: | (LPDISPATCH ) *OutputObject | Pointer to the corresponding object in the context of the part document |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You can use this method with any object assigned a persistent reference ID; for example, a Feature, Annotation or Sketch object.
