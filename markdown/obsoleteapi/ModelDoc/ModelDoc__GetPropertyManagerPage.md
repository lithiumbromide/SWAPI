---
title: "ModelDoc::GetPropertyManagerPage"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetPropertyManagerPage.htm"
---

# ModelDoc::GetPropertyManagerPage

This method is obsolete and has been superseded by [ModelDoc2::GetPropertyManagerPage](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetPropertyManagerPage.htm).

Description

This method creates a page for display in the PropertyManager.

Syntax (OLE Automation)

Not Availiable.

Syntax (COM)

status = ModelDoc->GetPropertyManagerPage ( dialogId, title, &handler, &retval )

| Input: | (long) dialogId | Resource ID of the dialog resource |
| --- | --- | --- |
| Input: | (BSTR) title | Title of the PropertyManager page dialog |
| Input: | (IUnknown) handler | Pointer to the event handler to use with this PropertyManager page |
| Output: | (LPPROPERTYMANAGERPAGE) retval | Pointer to the newly created PropertyManager page |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
