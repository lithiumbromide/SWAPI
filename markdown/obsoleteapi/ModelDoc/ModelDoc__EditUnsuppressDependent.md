---
title: "ModelDoc::EditUnsuppressDependent"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__EditUnsuppressDependent.htm"
---

# ModelDoc::EditUnsuppressDependent

This method is obsolete and has been superseded by [ModelDoc::EditUnsuppressDependent2](ModelDoc__EditUnsuppressDependent2.htm).

Description

This method unsuppresses the selected feature or the selected component and any dependents.

Syntax (OLE Automation)

retval = ModelDoc.EditUnsuppressDependent ( )

| Return: | (BOOL) retval | TRUE if unsuppress is successful, FALSE otherwise |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->EditUnsuppressDependent ( &retval )

| Output: | (VARIANT_BOOL) retval | TRUE if unsuppress is successful, FALSE otherwise |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks
