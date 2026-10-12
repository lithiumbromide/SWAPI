---
title: "ModelDoc::GetTitle"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetTitle.htm"
---

# ModelDoc::GetTitle

This method is obsolete and has been superseded by [ModelDoc2::GetTitle](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetTitle.htm).

Description

This method retrieves the title of the document that appears in the active window title bar.

Syntax (OLE Automation)

retval = ModelDoc.GetTitle ()

| Return: | (BSTR) retval | Title string, usually displayed on the window title bar |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->GetTitle ( &retval )

| Output: | (BSTR) retval | Title string, usually displayed on the window title bar |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The document name that appears in the window header changes based on your Microsoft Internet Explorer settings. If you chose to suppress known file extensions, then the title shown in the window, and subsequently returned by this method, will vary (for example, Part1.sldprt vs. Part1).
