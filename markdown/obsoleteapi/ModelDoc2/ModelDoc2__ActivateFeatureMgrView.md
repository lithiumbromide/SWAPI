---
title: "ModelDoc2::ActivateFeatureMgrView"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__ActivateFeatureMgrView.htm"
---

# ModelDoc2::ActivateFeatureMgrView

This method is obsolete and has been superseded by [FeatMgrView::ActivateView](sldworksAPI.chm::/FeatMgrView/FeatMgrView__ActivateView.htm).

Description

This method activates a tab in the FeatureManager design tree view.

Syntax (OLE Automation)

retval = ModelDoc2.ActivateFeatureMgrView ( appView )

| Input: | (long) appView | CView to activate in the FeatureManager design tree view |
| --- | --- | --- |
| Return: | (long) retval | Pane in which the view is activated as defined in swFeatMgrPane_e |

Syntax (COM)

status = ModelDoc2->ActivateFeatureMgrView ( appView, &retval )

| Input: | (long) appView | CView to activate in the FeatureManager design tree view |
| --- | --- | --- |
| Output: | (long) retval | Pane in which the view is activated as defined in swFeatMgrPane_e |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The activated tab may be in a pane that is hidden. The retval argument indicates the pane in which the tab is activated and if that pane is hidden.
