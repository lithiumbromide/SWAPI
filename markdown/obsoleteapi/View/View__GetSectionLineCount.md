---
title: "View::GetSectionLineCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetSectionLineCount.htm"
---

# View::GetSectionLineCount

This method is obsolete and has been superseded by [View::GetSectionLineCount2](sldworksAPI.chm::/View/View__GetSectionLineCount2.htm).

Description

This method gets the number of section lines in the view.

Syntax (OLE Automation)

retval = View.GetSectionLineCount ( size)

| Output: | (long) size | Number of elements in the array |
| --- | --- | --- |
| Return: | (long) retval | Number of section lines in the drawing view |

Syntax (COM)

status = View->GetSectionLineCount ( &size, &retval )

| Output: | (long) size | Number of elements in the array |
| --- | --- | --- |
| Output: | (long) retval | Number of section lines in the drawing view |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
