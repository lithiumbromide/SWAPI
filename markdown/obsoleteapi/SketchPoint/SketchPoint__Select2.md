---
title: "SketchPoint::Select2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SketchPoint/SketchPoint__Select2.htm"
---

# SketchPoint::Select2

This method is obsolete and has been superseded by [SketchPoint::Select3](SketchPoint__Select3.htm).

Description

This method selects this point and marks it.

Syntax (OLE Automation)

retval = SketchPoint.Select2 ( Append, Mark )

| Input: | (VARIANT_BOOL) Append | TRUE appends the selections to the current selection list, FALSE replaces the current selection list with this item |
| --- | --- | --- |
| Input: | (long) Mark | Value you want to use as a mark; this number is used by certain API functions that require ordered selection |
| Output: | (VARIANT_BOOL) retval | TRUE if the sketch point was selected, FALSE if not |

Syntax (COM)

status = SketchPoint->Select2 ( Append, Mark, &retval )

| Input: | (VARIANT_BOOL) Append | TRUE appends the selections to the current selection list, FALSE replaces the current selection list with this item |
| --- | --- | --- |
| Input: | (long) Mark | Value you want to use as a mark; this number is used by API functions that require ordered selection |
| Output: | (VARIANT_BOOL) retval | TRUE if the sketch point was selected, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
