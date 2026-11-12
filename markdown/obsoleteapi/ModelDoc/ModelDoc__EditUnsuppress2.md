---
title: "ModelDoc::EditUnsuppress2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__EditUnsuppress2.htm"
---

# ModelDoc::EditUnsuppress2

This method is obsolete and has been superseded by [ModelDoc2::EditUnsuppress2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__EditSuppress2.htm).

Description

This method unsuppresses the selected feature or the selected component.

Syntax (OLE Automation)

retval = ModelDoc.EditUnsuppress2 ( )

| Return: | (BOOL) retval | TRUE if unsuppress is successful, FALSE otherwise |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->EditUnsuppress2 ( &retval )

| Output: | (VARIANT_BOOL) retval | TRUE if unsuppress is successful, FALSE otherwise |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This routine is identical to ModelDoc::EditUnsuppress. The version number was incremented to allow VB applications to take advantage of information not available in PartDoc::EditUnsuppress.
