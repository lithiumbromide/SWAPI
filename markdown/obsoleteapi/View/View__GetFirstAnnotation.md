---
title: "View::GetFirstAnnotation"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetFirstAnnotation.htm"
---

# View::GetFirstAnnotation

This method is obsolete and has been superseded by [View::GetFirstAnnotation2](View__GetFirstAnnotation2.htm).

Description

This method gets the first annotation in the view.

Syntax (OLE Automation)

retval = View.GetFirstAnnotation( )

| Return: | (LPDISPATCH) retval | Dispatch object for the first annotation in the view |
| --- | --- | --- |

Syntax (COM)

status = View->IGetFirstAnnotation( &retval )

| Output: | (LPANNOTATION) retval | Pointer to the first annotation in the view |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
