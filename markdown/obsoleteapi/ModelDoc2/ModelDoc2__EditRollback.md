---
title: "ModelDoc2::EditRollback"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__EditRollback.htm"
---

# ModelDoc2::EditRollback

This method is obsolete and has been superseded by [ModelDoc2::EditRollback2](ModelDoc2__EditRollback2.htm).

Description

This method rolls back the FeatureManager design tree's rollback bar to just before the selected feature.

Syntax (OLE Automation)

retval = ModelDoc2.EditRollback ( )

| Return: | (BOOL)retval | TRUE if rollback successful, FALSE otherwise |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc2->EditRollback ( &retval )

| Output: | (VARIANT_BOOL) retval | TRUE if rollback successful, FALSE otherwise |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The selected feature, and those below it in the FeatureManager design tree, are suppressed and not accessible.
