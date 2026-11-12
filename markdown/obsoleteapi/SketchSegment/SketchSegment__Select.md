---
title: "SketchSegment::Select"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SketchSegment/SketchSegment__Select.htm"
---

# SketchSegment::Select

This method is obsolete and has been superseded by [SketchSegment::Select2](SketchSegment__Select2.htm).

Description

This method selects the SketchSegment object and appends it to the current set of selections or replaces the entire selection list.

Syntax (OLE Automation)

retval = SketchSegment.Select ( appendFlag )

| Input: | (BOOL) appendFlag | TRUE to append to the current selection list, FALSE to replace the current selection list with this item |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if successfully selected, FALSE otherwise |

Syntax (COM)

status = SketchSegment->Select ( appendFlag, &retval )

| Input: | (VARIANT_BOOL) appendFlag | TRUE to append to the current selection list, FALSE to replace the current selection list with this item |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if successfully selected, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use ModelDoc2::SelectByID instead of using this method. This method does not work well when a PropertyManager page is open or a command is running. ModelDoc2::SelectByID handles selection correctly whether or not a command is running.

To select or deselect a sketch segment, the owning document of that SketchSegment object needs to be open and visible.

Sketch segment selections are accessible through the SelectionMgr of the owning document of the SketchSegment object, even if the owning document is not active.

Selection or deselection does not work for a sketch segment in a document within a drawing. Selection or deselection of sketch segments owned by the drawing works, but only if the drawing document is active.

If the owning sketch of a sketch segment was active, or inactive, when the sketch segment was obtained, then it must be active, or inactive, to deSelect it. For example, if the owning sketch of a sketch segment was active when the sketch segment was obtained, then the owning sketch must be active to select or deselect the sketch segment. Likewise, if the owning sketch of a sketch segment was inactive when the sketch segment was obtained, then the owning sketch must be inactive to select or deselect the sketch segment.
