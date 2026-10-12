---
title: "ModelDoc::EditRollback2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__EditRollback2.htm"
---

# ModelDoc::EditRollback2

This method is obsolete and has been superseded by [ModelDoc2::EditRollback2](../ModelDoc2/ModelDoc2__EditRollback2.htm).

Description

This function rolls back the model to just before the selected feature.

Syntax (OLE Automation)

retval = ModelDoc.EditRollback2 ( )

| Return: | (BOOL) retval | TRUE if rollback successful, FALSE otherwise |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->EditRollback2 ( &retval )

| Output: | (VARIANT_BOOL) retval | TRUE if rollback successful, FALSE otherwise |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The selected feature,and those below it in the FeatureManager design tree are suppressed and not accessible.

This routine is identical to ModelDoc::EditRollback. The version number was incremented to allow VB applications to take advantage of information not available in PartDoc::EditRollback.
