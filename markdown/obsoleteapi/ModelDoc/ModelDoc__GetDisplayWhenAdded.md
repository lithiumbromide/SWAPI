---
title: "ModelDoc::GetDisplayWhenAdded"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetDisplayWhenAdded.htm"
---

# ModelDoc::GetDisplayWhenAdded

This method is obsolete and has been superseded by [ModelDoc2::GetDisplayWhenAdded](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetDisplayWhenAdded.htm).

Description

This method determines whether entities are displayed when created.

Syntax (OLE Automation)

retval = ModelDoc.GetDisplayWhenAdded ()

| Return: | (BOOL) retval | TRUE if new entities are displayed when added, FALSE if not |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->GetDisplayWhenAdded ( &retval )

| Output: | (VARIANT_BOOL) retval | TRUE if new entities are displayed when added, FALSE if not |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
