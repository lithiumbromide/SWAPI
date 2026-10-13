---
title: "SketchContour::Select"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SketchContour/SketchContour__Select.htm"
---

# SketchContour::Select

This method is obsolete and has been superseded by [SketchContour::Select2](sldworksAPI.chm::/SketchContour/SketchContour__Select2.htm).

Description

This method selects and marks this contour.

Syntax (OLE Automation)

retval = SketchContour.Select ( Append, Mark )

| Input: | (VARIANT_BOOL) Append | TRUE appends the sketch contour to the current selection list, FALSE replaces the current selection list |
| --- | --- | --- |
| Input: | (long) Mark | Value you want to use as a mark; this number is used by APIs that require ordered selection |
| Output: | (VARIANT_BOOL) retval | TRUE if the contour is selected, FALSE if not |

Syntax (COM)

status = SketchContour->Select ( Append, Mark, &retval )

| Input: | (VARIANT_BOOL) Append | TRUE appends the selected sketch contour to the current selection list, FALSE replaces the current selection list |
| --- | --- | --- |
| Input: | (long) Mark | Value you want to use as a mark; this number is used by APIs that require ordered selection |
| Output: | (VARIANT_BOOL) retval | TRUE if the contour is selected, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
