---
title: "ModelDoc2::CreateFeatureMgrView"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CreateFeatureMgrView.htm"
---

# ModelDoc2::CreateFeatureMgrView

This method is obsolete and has been superseded by [ModelDoc2::CreateFeatureMgrView2](ModelDoc2__CreateFeatureMgrView2.htm).

Description

This method creates a new FeatureManager design tree view. This method also provides a parameter for adding a tab, which the user clicks to activate your view.

Syntax (OLE Automation)

retval = ModelDoc2.CreateFeatureMgrView ( bitmap)

| Input: | (long*) bitmap | Pointer to the bitmap you wish to use for the FeatureManager design tree tab; the bitmap should be no larger than 16x18; this standard pointer is created by performing a New on CBitmap |
| --- | --- | --- |
| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the FeatMgrView created |

Syntax (COM)

status = ModelDoc2->ICreateFeatureMgrView ( bitmap, &retval )

| Input: | (long*) bitmap | Pointer to the bitmap you wish to use for the FeatureManager design tree tab; the bitmap should be no larger than 16x18; this standard pointer is created by performing a New on CBitmap |
| --- | --- | --- |
| Output: | (LPFEATMGRVIEW) retval | Pointer to the FeatMgrView created |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

If you receive a non-NULL return value, you can use FeatMgrView::GetFeatMgrViewWnd to get the new view handle. Because the view created is empty, you may use the new view handle in combination with standard MFC calls to draw, as desired, into the view.

The FeatureManager design tree view added to this document is not persistent. In other words, the FeatureManager design tree view is not stored with this document and must be recreated upon reloading the document.

This method will be automatically set up to receive FeatMgrView::ActivateNotify and DeactivateNotify events. On the appropriate notification, you can call ModelDoc2::DeleteFeatureMgrView to cleanup and delete your view.
