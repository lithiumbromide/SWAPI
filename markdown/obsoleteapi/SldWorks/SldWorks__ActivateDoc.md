---
title: "SldWorks::ActivateDoc"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__ActivateDoc.htm"
---

# SldWorks::ActivateDoc

This method is obsolete and has been superseded by [SldWorks::ActivateDoc2](sldworksAPI.chm::/SldWorks/SldWorks__ActivateDoc2.htm).

Description

This method activates a document that has already been loaded. This file becomes the active document, and this method returns a pointer to that document object.

Syntax (OLE Automation)

retval = SldWorks.ActivateDoc ( Name)

| Input: | (BSTR) Name | Name of document |
| --- | --- | --- |
| Return: | (LPDISPATCH) retval | Pointer to Dispatch object, the document or NULL if the operation fails |

Syntax (COM)

status = SldWorks->IActivateDoc ( Name, &retval )

| Input: | (BSTR) Name | Name of document |
| --- | --- | --- |
| Output: | (LPMODELDOC) retval | Pointer to the document or NULL if the operation fails |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If you do not specify a file extension in the Name parameter, then SolidWorks activates the document based strictly on its name and ignores the file extension. This may cause problems if you have two different document types with the same name loaded , for example, 12345.sldprt and 12345.sldasm. If you do not specify the file extension in your call to this method, then you cannot be sure which document will be activated. To avoid this problem, you can specify the file extension in the Name parameter or you can check the document type after it is activated using ModelDoc2::GetType.
