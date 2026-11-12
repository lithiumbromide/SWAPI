---
title: "ModelDoc::GetExternalReferenceName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetExternalReferenceName.htm"
---

# ModelDoc::GetExternalReferenceName

This method is obsolete and has been superseded by [ModelDoc2::GetExternalReferenceName](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetExternalReferenceName.htm).

Description

This method returns the name of the externally referenced document if a joined or mirrored part. The full path of the externally referenced document is returned.

Syntax (OLE Automation)

retval = ModelDoc.GetExternalReferenceName ( )

| Return: | (BSTR) retval | Full path of referenced document or NULL |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->GetExternalReferenceName ( &retval )

| Output: | (BSTR) retval | Full path of referenced document or NULL |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If ModelDoc does not have an externally referenced document, a null string is returned.
