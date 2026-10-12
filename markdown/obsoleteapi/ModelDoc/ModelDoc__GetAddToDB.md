---
title: "ModelDoc::GetAddToDB"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetAddToDB.htm"
---

# ModelDoc::GetAddToDB

This method is obsolete and has been superseded by [ModelDoc2::GetAddToDB](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetAddToDB.htm).

Description

This method determines whether or not entities are added directly to the SolidWorks database.

Syntax (OLE Automation)

retval = ModelDoc.GetAddToDB ()

| Return: | (BOOL) retval | TRUE if adding items directly to the database, FALSE otherwise |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->GetAddToDB ( &retval )

| Output: | (VARIANT_BOOL) retval | TRUE if adding items directly to the database, FALSE otherwise |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
