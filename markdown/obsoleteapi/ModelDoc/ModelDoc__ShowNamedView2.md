---
title: "ModelDoc::ShowNamedView2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__ShowNamedView2.htm"
---

# ModelDoc::ShowNamedView2

This method is obsolete and has been superseded by [ModelDoc2::ShowNamedView2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__ShowNamedView2.htm).

Description

This method displays the specified view.

Syntax (OLE Automation)

void ModelDoc.ShowNamedView2 ( vName, viewId)

| Input: | (BSTR) vName | Name of the view to be displayed or an empty string if you wish to use the viewId argument instead |
| --- | --- | --- |
| Input: | (long) viewId | ID of the view to be displayed or -1 if you wish to use the viewName argument instead; if you specify both the viewName and viewId, then viewId takes precedence if the two arguments do not resolve to the same view |

Syntax (COM)

status = ModelDoc->ShowNamedView2 ( vName, viewId )

| Input: | (BSTR) vName | Name of the view to be displayed or an empty string if you wish to use the viewId argument instead |
| --- | --- | --- |
| Input: | (long) viewId | ID of the view to be displayed or -1 if you wish to use the viewName argument instead; if you specify both the viewName and viewId, then viewId takes precedence if the two arguments do not resolve to the same view |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
