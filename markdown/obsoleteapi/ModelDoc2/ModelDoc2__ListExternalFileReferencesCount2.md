---
title: "ModelDoc2::ListExternalFileReferencesCount2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__ListExternalFileReferencesCount2.htm"
---

# ModelDoc2::ListExternalFileReferencesCount2

This method is obsolete and has been superseded by [ModelDocExtension::ListExternalFileReferences](sldworksAPI.chm::/ModelDocExtension/ModelDocExtension__ListExternalFileReferencesCount.htm).

Description

This method gets the number of external file references on this model.

Syntax (OLE Automation)

retval = ModelDoc2.ListExternalFileReferencesCount2 ( )

| Output: | (long) retval | Number of external references |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc2->ListExternalFileReferencesCount2 ( &retval )

| Output: | (long) retval | Number of external references |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Call this method before calling the COM version of [ModelDoc2::IListExternalFileReferences2](ModelDoc2__ListExternalFileReferences2.htm) to determine the size of the array .
