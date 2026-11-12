---
title: "ModelDoc2::GetPropertyManagerPage"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__GetPropertyManagerPage.htm"
---

# ModelDoc2::GetPropertyManagerPage

This method is obsolete and has been superseded by [SldWorks::CreatePropertyManagerPage](sldworksAPI.chm::/SldWorks/SldWorks__CreatePropertyManagerPage.htm).

Description

This method creates a page for display in the PropertyManager.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = ModelDoc2->GetPropertyManagerPage ( dialogId, title, &handler, &retval )

| Input: | (long) dialogId | Resource ID of the dialog resource |
| --- | --- | --- |
| Input: | (BSTR) title | Title of the PropertyManager page dialog |
| Input: | (IUnknown) handler | Pointer to the event handler to use with this PropertyManager page |
| Output: | (LPPROPERTYMANAGERPAGE) retval | Pointer to the newly created PropertyManager page |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
