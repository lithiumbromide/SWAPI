---
title: "ModelDoc::SetTitle2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetTitle2.htm"
---

# ModelDoc::SetTitle2

This method is obsolete and has been superseded by [ModelDoc2::SetTitle2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetTitle2.htm).

Description

This method sets the title of a new document. This title appears in the active window title bar.

Syntax (OLE Automation)

retval = ModelDoc.SetTitle2 ( newTitle )

| Input: | Input: (BSTR) | New title to give to the document window |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if successfully renamed, FALSE otherwise |

Syntax (COM)

status = ModelDoc->SetTitle2 ( newTitle, &retval )

| Input: | Input: (BSTR) | New title to give to the document window |
| --- | --- | --- |
| OUTPUT | (VARIANT_BOOL) retval | TRUE if successfully renamed, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method does not save this ModelDoc object to disk; it only renames the document window.

This method is only valid when called on a new document that has not yet been saved. It will not change the title of a document that has been saved and already exists on disk. If you want to rename an existing document, use ModelDoc::SaveAs2.

To retrieve the title of a document, use ModelDoc::GetTitle.
