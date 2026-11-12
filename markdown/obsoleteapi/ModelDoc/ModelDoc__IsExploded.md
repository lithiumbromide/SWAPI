---
title: "ModelDoc::IsExploded"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__IsExploded.htm"
---

# ModelDoc::IsExploded

This method is obsolete and has been superseded by [ModelDoc2::IsExploded](sldworksAPI.chm::/ModelDoc2/ModelDoc2__IsExploded.htm).

Description

This method determines if the model is currently exploded.

Syntax (OLE Automation)

retval = ModelDoc.IsExploded ()

| Return: | (BOOL) retval | TRUE if the model is currently displayed in exploded state, FALSE if the model is being displayed in collapsed state |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->IsExploded ( &retval )

| Output: | (VARIANT_BOOL) retval | TRUE if the model is currently displayed in exploded state, FALSE if the model is being displayed in collapsed state |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
