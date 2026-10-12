---
title: "SketchHatch::Select2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SketchHatch/SketchHatch__Select2.htm"
---

# SketchHatch::Select2

This method is obsolete and has been superseded by [SketchHatch::Select3](SketchHatch__Select3.htm).

Description

This method selects this hatch and marks it.

Syntax (OLE Automation)

retval = SketchHatch.Select2 ( Append, Mark )

| Input: | (VARIANT_BOOL) Append | TRUE appends the selections to the current selection list, FALSE replaces the current selection list |
| --- | --- | --- |
| Input: | (long) Mark | Value you want to use as a mark; this number is used by API functions that require ordered selection |
| Output: | (VARIANT_BOOL) retval | TRUE if the sketch hatch was selected, FALSE if not |

Syntax (COM)

status = SketchHatch->Select2 ( Append, Mark, &retval )

| Input: | (VARIANT_BOOL) Append | TRUE appends the selections to the current selection list, FALSE replaces the current selection list |
| --- | --- | --- |
| Input: | (long) Mark | Value you want to use as a mark; this number is used by API functions that require ordered selection |
| Output: | (VARIANT_BOOL) retval | TRUE if the sketch hatch was selected, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
