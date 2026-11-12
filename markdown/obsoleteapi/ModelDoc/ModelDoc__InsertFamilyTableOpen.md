---
title: "ModelDoc::InsertFamilyTableOpen"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertFamilyTableOpen.htm"
---

# ModelDoc::InsertFamilyTableOpen

This method is obsolete and has been superseded by [ModelDoc2::InsertFamilyTableOpen](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertFamilyTableOpen.htm).

Description

This method opens a specified family table from Excel into the part

Syntax (OLE Automation)

retval = ModelDoc.InsertFamilyTableOpen ( FileName )

| Input: | (BSTR) FileName | Full path name of the family table file |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if the family table was inserted, FALSE if not |

Syntax (COM)

status = ModelDoc->InsertFamilyTableOpen ( )

| Input: | (BSTR) FileName | Full path name of the family table file |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the Family Table was inserted, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
