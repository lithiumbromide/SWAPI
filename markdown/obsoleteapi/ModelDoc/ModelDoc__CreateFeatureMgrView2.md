---
title: "ModelDoc::CreateFeatureMgrView2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateFeatureMgrView2.htm"
---

# ModelDoc::CreateFeatureMgrView2

This method is obsolete and has been superseded by [ModelDoc::CreateFeatureMgrView3](ModelDoc__CreateFeatureMgrView3.htm).

Description

This method creates a new FeatureManager design tree view. This method also provides a parameter for adding a tab, which the user can click to activate your view.

Syntax (OLE Automation)

retval = ModelDoc.CreateFeatureMgrView2 ( bitmap, toolTip)

| Input: | (long*) bitmap | Pointer to the bitmap you wish to use for the FeatureManager design tree tab; the bitmap should be no larger than 16x18 this standard pointer is created by performing a New on CBitmap |
| --- | --- | --- |
| Input: | (BSTR) toolTip | ToolTip string |
| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the Feature Manager view |

Syntax (COM)

status = ModelDoc->ICreateFeatureMgrView2 ( bitmap, toolTip, &retval )

| Input: | (long*) bitmap | Pointer to the bitmap you wish to use for the FeatureManager design tree tab; the bitmap should be no larger than 16x18 this standard pointer is created by performing a New on CBitmap |
| --- | --- | --- |
| Input: | (BSTR) toolTip | ToolTip string |
| Output: | (LPFEATMGRVIEW) retval | Pointer to the newly created FeatMgrView object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If you receive a non-NULL return value, you can use FeatMgrView::GetFeatMgrViewWnd to get the new view handle. Because the view created is empty, you can use the new view handle in combination with standard MFC calls to draw, as desired, into the view.

The FeatureManager design tree view added to this document is not persistent. The FeatureManager design tree view is not stored with this document and must be recreated upon reloading the document.

This method will be automatically set up to receive FeatMgrView::ActivateNotify and DeactivateNotify events. On the appropriate notification, you can call ModelDoc2::DeleteFeatureMgrView to cleanup and delete your view.
