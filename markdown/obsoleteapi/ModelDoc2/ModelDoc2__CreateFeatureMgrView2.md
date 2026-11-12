---
title: "ModelDoc2::CreateFeatureMgrView2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CreateFeatureMgrView2.htm"
---

# ModelDoc2::CreateFeatureMgrView2

This method is obsolete and has been superseded by [ModelDoc2::CreateFeatureMgrView3](ModelDoc2__CreateFeatureMgrView3.htm).

Description

This method creates a new FeatureManager design tree view. This method also provides a parameter for adding a tab, which a user can click to activate your view.

Syntax (OLE Automation)

retval = ModelDoc2.CreateFeatureMgrView2 ( bitmap, toolTip)

| Input: | (long*) bitmap | Pointer to the bitmap you wish to use for the FeatureManager design tree tab; the bitmap should be no larger than 16x18; this standard pointer is created by performing a New on CBitmap |
| --- | --- | --- |
| Input: | (BSTR) toolTip | ToolTip string |
| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the FeatMgrView created |

Syntax (COM)

status = ModelDoc2->ICreateFeatureMgrView2 ( bitmap, toolTip, &retval )

| Input: | (long*) bitmap | Pointer to the bitmap you wish to use for the FeatureManager design tree tab; the bitmap should be no larger than 16x18; this standard pointer is created by performing a New on CBitmap |
| --- | --- | --- |
| Input: | (BSTR) toolTip | ToolTip string |
| Output: | (LPFEATMGRVIEW) retval | Pointer to the FeatMgrView created. |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is identical to the earlier version, ModelDoc2::CreateFeatureMgrView, except this method provides an option for tool tips on your newly created FeatureManager design tree tab.

If you receive a non-NULL return value, you can use FeatMgrView::GetFeatMgrViewWnd to get the new view handle. Because the view created is empty, you may use the new view handle with standard MFC calls to draw, as desired, into the view.

The FeatureManager design tree view added to this document is not persistent. In other words, the FeatureManager design tree view is not stored with this document and must be recreated upon reloading the document.

This method is automatically set up to receive FeatMgrView::ActivateNotify and DeactivateNotify events. On the appropriate notification, you can call ModelDoc2::DeleteFeatureMgrView to clean up and delete your view.
