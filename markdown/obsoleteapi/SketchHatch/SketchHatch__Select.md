---
title: "SketchHatch::Select"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SketchHatch/SketchHatch__Select.htm"
---

# SketchHatch::Select

This method is obsolete and has been superseded by [SketchHatch::Select2](SketchHatch__Select2.htm).

Description

This method selects this hatch and appends it to the current set of selections or replaces the entire selection list.

Syntax (OLE Automation)

retval = SketchHatch.Select2 ( Append, Mark )

| Input: | (VARIANT_BOOL) Append | TRUE appends the selections to the current selection list, FALSE replaces the current selection list |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the sketch hatch was selected, FALSE if not |

Syntax (COM)

status = SketchHatch->Select2 ( Append, Mark, &retval )

| Input: | (VARIANT_BOOL) Append | TRUE appends the selections to the current selection list, FALSE replaces the current selection list |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the sketch hatch was selected, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
