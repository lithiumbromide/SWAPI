---
title: "ModelDoc::EditSuppress2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__EditSuppress2.htm"
---

# ModelDoc::EditSuppress2

This method is obsolete and has been superseded by [ModelDoc2::EditSuppress2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__EditSuppress2.htm).

Description

This method suppresses the selected feature, the selected component, or the owning feature of the selected face.

Syntax (OLE Automation)

retval = ModelDoc.EditSuppress2 ( )

| Return: | (BOOL) retval | TRUE if suppress successful, FALSE otherwise |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->EditSuppress2 ( &retval )

| Output: | (VARIANT_BOOL) retval | TRUE if suppress successful, FALSE otherwise |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is identical to ModelDoc::EditSuppress. The version number was incremented to allow VB applications to take advantage of information not available in PartDoc::EditSuppress.
