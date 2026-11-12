---
title: "ModelDoc::ActivateFeatureMgrView"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__ActivateFeatureMgrView.htm"
---

# ModelDoc::ActivateFeatureMgrView

This method is obsolete and has been superseded by [ModelDoc2::ActivateFeatureMgrView](../ModelDoc2/ModelDoc2__ActivateFeatureMgrView.htm).

Description

This method activates a given tab in the FeatureManager design tree view.

Syntax (OLE Automation)

retval = ModelDoc.ActivateFeatureMgrView ( appView )

| Input: | (long) appView | CView to activate in the FeatureManager design tree view |
| --- | --- | --- |
| Return: | (long) retval | Pane in which the view was activated as defined in swFeatMgrPane_e |

Syntax (COM)

status = ModelDoc->ActivateFeatureMgrView ( appView, &retval )

| Input: | (long) appView | CView to activate in the FeatureManager design tree view |
| --- | --- | --- |
| Output: | (long) retval | Pane in which the view was activated as defined in swFeatMgrPane_e |
| Return: | (HRESULT) status | S_OK if successful; S_FALSE otherwise |

Remarks

The activated tab may be in a pane that is hidden. The retval argument will indicate if which pane the tab is activated in and if that pane is hidden.
