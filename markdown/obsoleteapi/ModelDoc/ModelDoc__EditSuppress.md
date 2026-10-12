---
title: "ModelDoc::EditSuppress"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__EditSuppress.htm"
---

# ModelDoc::EditSuppress

This method is obsolete and has been superseded by [ModelDoc::EditSuppress2](ModelDoc__EditSuppress2.htm).

Description

This method suppresses the selected feature, the selected component, or the owning feature of the selected face.

Syntax (OLE Automation)

retval = ModelDoc.EditSuppress ( )

| Return: | (BOOL) retval | TRUE if suppress successful, FALSE otherwise |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->EditSuppress ( &retval )

| Output: | (VARIANT_BOOL) retval | TRUE if suppress successful, FALSE otherwise |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
