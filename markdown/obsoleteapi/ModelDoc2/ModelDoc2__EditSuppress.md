---
title: "ModelDoc2::EditSuppress"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__EditSuppress.htm"
---

# ModelDoc2::EditSuppress

This method is obsolete and has been superseded by [ModelDoc2::EditSuppress2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__EditSuppress2.htm).

Description

This method suppresses the selected feature, the selected component, or the owning feature of the selected face.

Syntax (OLE Automation)

retval = ModelDoc2.EditSuppress ( )

| Return: | (BOOL) retval | TRUE if suppressed, FALSE otherwise |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc2->EditSuppress ( &retval )

| Output: | (VARIANT_BOOL) retval | TRUE if suppressed, FALSE otherwise |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
