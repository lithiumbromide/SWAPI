---
title: "SldWorks::OpenDoc2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__OpenDoc2.htm"
---

# SldWorks::OpenDoc2

This method is obsolete and has been superseded by [SldWorks::OpenDoc3](SldWorks__OpenDoc3.htm).

Description

This method opens an existing document of Name and Type and returns a pointer to the document object. It also allows control over whether or not to suppress display of dialog boxes, opening the document read-only and opening the document view-only.

Syntax (OLE Automation)

retval = SldWorks.OpenDoc2 ( name, type, readOnly, viewOnly, silent, &errors )

| Input: | (BSTR) name | Name of document or full path, if not current directory |
| --- | --- | --- |
| Input: | (long) t ype | Type of document as defined in swDocumentTypes_e |
| Input: | (BOOL) readOnly | TRUE if document should be opened read-only, FALSE if document should not be opened read-only |
| Input: | (BOOL) viewOnly | TRUE if document should be opened view-only, FALSE if document should not be opened view-only |
| Input: | (BOOL) silent | TRUE if dialogs and warning messages should be avoided, FALSE if dialogs and warning messages should be displayed to the end-user |
| Output: | (long) errors | Error code as defined in swFileLoadError_e |
| Return: | (LPDISPATCH) retval | Pointer to dispatch object, the document , or NULL if the operation fails |

Syntax (COM)

status = SldWorks->IOpenDoc2 ( name, type, readOnly, viewOnly, silent, &errors, &retval )

| Input: | (BSTR) name | Name of document or full path, if not current directory |
| --- | --- | --- |
| Input: | (long) t ype | Type of document as defined in swDocumentTypes_e |
| Input: | (VARIANT_BOOL) readOnly | TRUE if document should be opened read-only, FALSE if document should not be opened read-only |
| Input: | ( VARIANT_BOOL ) viewOnly | TRUE if document should be opened view-only, FALSE if document should not be opened view-only |
| Input: | ( VARIANT_BOOL ) silent | TRUE if dialogs and warning messages should be avoided, FALSE if dialogs and warning messages should be displayed to the end-user |
| Output: | (long) errors | Error code as defined in swFileLoadError_e |
| Output: | (LPMODELDOC) retval | Pointer to dispatch object, the document , or NULL if the operation fails |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method fires SldWorksEvents::FileOpenNotify event.
