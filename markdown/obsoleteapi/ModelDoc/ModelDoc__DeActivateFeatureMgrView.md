---
title: "ModelDoc::DeActivateFeatureMgrView"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__DeActivateFeatureMgrView.htm"
---

# ModelDoc::DeActivateFeatureMgrView

This method is obsolete and has been superseded by [ModelDoc2::DeActivateFeatureMgrView](sldworksAPI.chm::/ModelDoc2/ModelDoc2__DeActivateFeatureMgrView.htm).

Description

This method deactivates a tab in the FeatureManager design tree view.

Syntax (OLE Automation)

retval = ModelDoc.DeActivateFeatureMgrView ( appView )

| Input: | ( long* ) appView | Pointer to the FeatureManager design tree view |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if deactivated, FALSE otherwise |

Syntax (COM)

status = ModelDoc->DeActivateFeatureMgrView ( appView, &retval )

| Input: | ( long* ) appView | Pointer to the FeatureManager design tree view |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if deactivated, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
