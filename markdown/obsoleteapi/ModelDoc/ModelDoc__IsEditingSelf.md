---
title: "ModelDoc::IsEditingSelf"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__IsEditingSelf.htm"
---

# ModelDoc::IsEditingSelf

This method is obsolete and has been superseded by [ModelDoc2::IsEditingSelf](sldworksAPI.chm::/ModelDoc2/ModelDoc2__IsEditingSelf.htm).

Description

This method determines if this model is being edited in the context of another document.

Syntax (OLE Automation)

retval = ModelDoc.IsEditingSelf ()

| Return: | (BOOL) retval | TRUE if this ModelDoc object is the active edit target, FALSE if this ModelDoc object is not the active edit target of the SolidWorks session |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->IsEditingSelf ( &retval )

| Output: | (VARIANT_BOOL) retval | TRUE if this ModelDoc object is the active edit target, FALSE if this ModelDoc object is not the active edit target of the SolidWorks session |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
