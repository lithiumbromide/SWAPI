---
title: "SldWorks::EnumDocuments"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__EnumDocuments.htm"
---

# SldWorks::EnumDocuments

This method is obsolete and has been superseded by [SldWorks::EnumDocuments2](sldworksAPI.chm::/SldWorks/SldWorks__EnumDocuments2.htm).

Description

This method gets the enumerated list of documents that are currently open in the application.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = SldWorks->EnumDocuments( &retval )

| Output: | (LPENUMDOCUMENTS) retval | Pointer to the enumerated list of documents |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

#### Remarks

The list of ModelDoc2 objects contained in the EnumDocuments2 object contain any open ModelDoc2 pointer. This includes ModelDoc2 objects that may have been opened as file references; for example, from an assembly or drawing.

You may want to use the ModelDoc2::Visible property to determine if a particular document has its own window and is visible to the user.
