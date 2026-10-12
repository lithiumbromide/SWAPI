---
title: "ModelDoc::GetPathName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetPathName.htm"
---

# ModelDoc::GetPathName

This method is obsolete and has been superseded by [ModelDoc2::GetPathName](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetPathName.htm).

Description

This method retrieves the full path name for this document, including the file name. If the document has not been saved, then the returned string is empty.

Syntax (OLE Automation)

retval = ModelDoc.GetPathName ()

| Return: | (BSTR) retval | Full path name for this document, including the file name |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->GetPathName ( &retval )

| Output: | (BSTR) retval | Full path name for this document, including the file name |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
