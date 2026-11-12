---
title: "ModelDoc::EditRollback"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__EditRollback.htm"
---

# ModelDoc::EditRollback

This method is obsolete and has been superseded by [ModelDoc::EditRollback2](ModelDoc__EditRollback2.htm).

Description

This method rolls back the model to just before the selected feature.

Syntax (OLE Automation)

retval = ModelDoc.EditRollback ( )

| Return: | (BOOL)retval | TRUE if rollback successful, FALSE otherwise |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->EditRollback ( &retval )

| Output: | (VARIANT_BOOL) retval | TRUE if rollback successful, FALSE otherwise |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful; S_FALSE otherwise |

Remarks

The selected feature and those below it in the FeatureManager design tree are suppressed and not accessible.
