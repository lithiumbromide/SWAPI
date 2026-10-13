---
title: "ModelDoc::InsertDatumTag2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertDatumTag2.htm"
---

# ModelDoc::InsertDatumTag2

This method is obsolete and has been superseded by [ModelDoc2::InsertDatumTag2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertDatumTag2.htm).

Description

This method inserts a datum tag symbol at the selected location.

Syntax (OLE Automation)

retval = ModelDoc.InsertDatumTag2 ( )

| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the newly created DATUMTAG object |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->IInsertDatumTag2 ( &retval )

| Output: | (LPDATUMTAG) retval | Pointer to a newly created LPDATUMTAG object |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
