---
title: "ModelDoc2::CreateFeatureMgrView3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CreateFeatureMgrView3.htm"
---

# ModelDoc2::CreateFeatureMgrView3

This method is obsolete and has been superseded by [ModelViewManager::CreateFeatureMgrView2](sldworksAPI.chm::/ModelViewManager/ModelViewManager__CreateFeatureMgrView2.htm).

Description

This method creates a new FeatureManager design tree view. This method also provides a parameter for adding a tab, which the user clicks to activate your view.

Syntax (OLE Automation)

retval = ModelDoc2.CreateFeatureMgrView3 ( bitmap, toolTip, whichPane )

| Input: | (long*) bitmap | Pointer to the bitmap you wish to use for the FeatureManager design tree tab. The bitmap should be no larger than 16x18. This standard pointer is created by performing a New on CBitmap |
| --- | --- | --- |
| Input: | (BSTR) toolTip | ToolTip string |
| Input: | (long) whichPane | Pane to add the view as defined by swFeatMgrPane_e |
| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the FeatMgrView created |

Syntax (COM)

status = ModelDoc2->ICreateFeatureMgrView3 ( bitmap, toolTip, whichPane, &retval )

| Input: | (long*) bitmap | Pointer to the bitmap you wish to use for the FeatureManager design tree tab. The bitmap should be no larger than 16x18. This standard pointer is created by performing a New on CBitmap |
| --- | --- | --- |
| Input: | (BSTR) toolTip | ToolTip string |
| Input: | (long) whichPane | Pane to add the view as defined by swFeatMgrPane_e |
| Output: | (LPFEATMGRVIEW) retval | pointer to the FeatMgrView created |
| Return: | (HRESULT)status | S_OK if successful, S_FALSE if the view was not created |

Remarks

This method is identical to the earlier version, ModelDoc2::CreateFeatureMgrView2, except that this method provides the ability to place your newly created Feature Manager tab on either the top or bottom pane. The pane may or may not be visible. However, the tab is added to the specified pane.

Under certain conditions, for example while the Surface, Extend command is active in the user interface, SolidWorks locks the bottom pane and does not allow the activation of any other tab. If your application needs the ability to activate your new tab at all times, consider adding it either to the top pane or to both panes. If you add it to the top pane only, it may not be apparent to the user until the top pane is made visible.

If you receive a non-NULL return value, you can use FeatMgrView::GetFeatMgrViewWnd to get the new view handle. Because the view created is empty, you can use the new view handle in combination with standard MFC calls to draw, as desired, into the view.

The FeatureManager design tree view added to this document is not persistent. In other words, the FeatureManager design tree view is not stored with this document and must be recreated upon reloading the document.

This method automatically sets up to receive FeatMgrView::ActivateNotify and DeactivateNotify events. On the appropriate notification, you can call ModelDoc2::DeleteFeatureMgrView to clean up and delete your view.
