---
title: "ModelDoc::GetFirstModelView"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetFirstModelView.htm"
---

# ModelDoc::GetFirstModelView

This method is obsolete and has been superseded by [ModelDoc2::GetFirstModelView](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetFirstModelView.htm).

Description

This method gets the first view in a model document.

Syntax (OLE Automation)

retval = ModelDoc.GetFirstModelView ( )

| Return: | (LPDISPATCH)retval | Pointer to a Dispatch object, the first model view in this document |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->IGetFirstModelView ( &retval )

| Output: | (LPMODELVIEW) retval | Pointer to the first model view in this document |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if Successful, S_FALSE if no model view is being returned |

Remarks

You can traverse through the model views in a document by using this method to get the initial view, and ModelView::GetNext to get each of the following views. When ModelView::GetNext returns NULL, you have reached the end of the list.

See also [ModelDoc::EnumModelViews](ModelDoc__EnumModelViews.htm) for a method for traversing the model views on a document.
