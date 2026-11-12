---
title: "SketchRegion::Select"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SketchRegion/SketchRegion__Select.htm"
---

# SketchRegion::Select

This method is obsolete and has been superseded by [SketchRegion::Select2](sldworksAPI.chm::/SketchRegion/SketchRegion__Select2.htm).

Description

This method selects this sketch region and marks it.

Syntax (OLE Automation)

retval = SketchRegion.Select ( Append, Mark )

| Input: | (VARIANT_BOOL) Append | TRUE appends the sketch region to the current selection list, FALSE replaces the current selection list with this sketch region |
| --- | --- | --- |
| Input: | (long) Mark | Value you want to use as a mark; this value is used by other functions that require ordered selection |
| Output: | (VARIANT_BOOL) retval | TRUE if the sketch region is selected, FALSE if not |

Syntax (COM)

status = SketchRegion->Select ( Append, Mark, &retval )

| Input: | (VARIANT_BOOL) Append | TRUE appends the sketch region to the current selection list, FALSE replaces the current selection list with this sketch region |
| --- | --- | --- |
| Input: | (long) Mark | Value you want to use as a mark; this value is used by other functions that require ordered selection |
| Output: | (VARIANT_BOOL) retval | TRUE if the sketch region is selected, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
