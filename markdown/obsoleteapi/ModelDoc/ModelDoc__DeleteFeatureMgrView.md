---
title: "ModelDoc::DeleteFeatureMgrView"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__DeleteFeatureMgrView.htm"
---

# ModelDoc::DeleteFeatureMgrView

This method is obsolete and has been superseded by [ModelDoc2::DeleteFeatureMgrView](sldworksAPI.chm::/ModelDoc2/ModelDoc2__DeleteFeatureMgrView.htm).

Description

This method removes a tab from the FeatureManager design tree view. On the appropriate notification, you can call this method to clean up and delete your FeatureManager design tree view.

Syntax (OLE Automation)

void ModelDoc.DeleteFeatureMgrView ( appView)

| Input: | (long*) appView | View handle of the FeatureManager design tree view that you wish to delete |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->DeleteFeatureMgrView ( appView )

| Input: | (long*) appView | View handle of the FeatureManager design tree view that you wish to delete |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Use this method with ModelDoc::AddFeatureMgrView or ModelDoc::CreateFeatureMgrView.

If your Feature Manager design tree view was created using ModelDoc::CreateFeatureMgrView, then calling this method destroys the CView object used for the FeatureManager design tree view. If your FeatureManager design tree view was created using ModelDoc::AddFeatureMgrView, then your application allocated the Cview object and calling this method does not destroy the Cview object. You are responsible for destroying the Cview object using the appropriate destructor. Never use the delete operator directly on the view object. Always use one of the appropriate MFC view destructors.
