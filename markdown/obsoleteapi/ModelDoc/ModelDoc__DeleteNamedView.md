---
title: "ModelDoc::DeleteNamedView"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__DeleteNamedView.htm"
---

# ModelDoc::DeleteNamedView

This method is obsolete and has been superseded by [ModelDoc2::DeleteNamedView](sldworksAPI.chm::/ModelDoc2/ModelDoc2__DeleteNamedView.htm).

Description

This method deletes the specified model view.

Syntax (OLE Automation)

retval = ModelDoc.DeleteNamedView ( viewname)

| Input: | (BSTR) viewname | Name of the view you wish to delete |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if the view was deleted successfully, FALSE if not |

Syntax (COM)

status = ModelDoc->DeleteNamedView ( viewname, &retval )

| Input: | (BSTR) viewname | Name of the view you wish to delete |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the view was deleted successfully, if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
