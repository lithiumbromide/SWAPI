---
title: "DrawingDoc::GetLineFontName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__GetLineFontName.htm"
---

# DrawingDoc::GetLineFontName

This method is obsolete and has been superseded by [DrawingDoc::GetLineFontName2](sldworksAPI.chm::/DrawingDoc/DrawingDoc__GetLineFontName2.htm).

Description

This method returns the descriptive name for the line font style at the specified index.

Syntax (OLE Automation)

retval = DrawingDoc.GetLineFontName ( index)

| Input: | (long) index | Index position of the line font style |
| --- | --- | --- |
| Return: | (BSTR) retval | Line font style name |

Syntax (COM)

status = DrawingDoc->GetLineFontName ( index, &retval )

| Input: | (long) index | Index position of the line font style |
| --- | --- | --- |
| Output: | (BSTR) retval | Line font style name |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Example or style names are:

- Visible
- Hidden
- Sketch
- Detail
- Section
- Dimensions
- Centerlines
- Crosshatch
- TanVisible

You can also use DrawingDoc::GetLineFontName2, which returns the actual name of the line fonts (for example, Solid, Center, Dashed, Centerline, and so on.).
