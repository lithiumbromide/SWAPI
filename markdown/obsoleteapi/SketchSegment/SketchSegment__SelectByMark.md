---
title: "SketchSegment::SelectByMark"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SketchSegment/SketchSegment__SelectByMark.htm"
---

# SketchSegment::SelectByMark

This method is obsolete and has been superseded by [SketchSegment::Select2](SketchSegment__Select2.htm).

Description

This method selects the sketch segment and appends it to the current set of selections or replaces the entire selection list. The selection is also marked with the value specified. This mark is used by certain API functions that require multiple selections.

Syntax (OLE Automation)

retval = SketchSegment.SelectByMark ( appendFlag, markValue )

| Input: | (BOOL) appendFlag | TRUE if you want to append to the current selection list, FALSE if you want this item to replace the current selection list |
| --- | --- | --- |
| Input: | (long) markValue | Number you want to use as a mark; this number is used by certain API functions that require ordered entity selection |
| Return: | (BOOL) retval | TRUE if successfully selected, FALSE if not |

Syntax (COM)

status = SketchSegment->SelectByMark ( appendFlag, markValue, &retval )

| Input: | (BOOL) appendFlag | TRUE if you want to append to the current selection list, FALSE if you want this item to replace the current selection list |
| --- | --- | --- |
| Input: | (long) markValue | Number you want to use as a mark; this number is used by certain API functions that require ordered entity selection |
| Output: | (BOOL) retval | TRUE if successfully selected, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use ModelDoc2::SelectByMark instead of using this method. This method does not work well when a PropertyManager page is open or a command is running. ModelDoc2::SelectByMark handles selection correctly whether or not a command is running.
