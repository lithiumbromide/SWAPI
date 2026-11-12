---
title: "ModelDoc::GetType"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetType.htm"
---

# ModelDoc::GetType

This method is obsolete and has been superseded by [ModelDoc2::GetType](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetType.htm).

Description

This method returns the type of the document.

Syntax (OLE Automation)

retval = ModelDoc.GetType ()

| Return: | (long) retval | Type of document |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->GetType ( &retval )

| Output: | (long) retval | Type of document |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The document type can be one of the following values:

swDocNONE - no document

swDocPART - part document

swDocASSEMBLY- assembly document

swDocDRAWING - drawing document

These definitions replace these now obsolete types:

TYPE_PART = 1

TYPE_ASSEMBLY = 2

TYPE_DRAWING = 3
