---
title: "SketchPoint::Select3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SketchPoint/SketchPoint__Select3.htm"
---

# SketchPoint::Select3

This method is obsolete and has been superseded by [SketchPoint::Select4](sldworksAPI.chm::/SketchPoint/SketchPoint__Select4.htm).

Description

This method selects this point.

Syntax (OLE Automation)

retval = SketchPoint.Select3 ( Append, Mark, Callout )

| Input: | (BOOL) Append | TRUE appends the sketch point to the selection list, FALSE replaces the current selection list with this sketch point |
| --- | --- | --- |
| Input: | (long) Mark | Value you want to use as a selection mark |
| Input: | (LPCALLOUT) Callout | Pointer to the associated callout |
| Output: | (BOOL) retval | TRUE if the entity was selected, FALSE if not |

Syntax (COM)

status = SketchPoint->Select3 ( Append, Mark, Callout, &retval )

| Input: | (VARIANT_BOOL) Append | TRUE appends the sketch point to the selection list, FALSE replaces the current selection list with this sketch point |
| --- | --- | --- |
| Input: | (long) Mark | Value you want to use as a selection mark |
| Input: | (LPCALLOUT) Callout | Pointer to the associated callout |
| Output: | (VARIANT_BOOL) retval | TRUE if the entity was selected, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
