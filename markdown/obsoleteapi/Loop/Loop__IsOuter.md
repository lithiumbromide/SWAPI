---
title: "Loop::IsOuter"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Loop/Loop__IsOuter.htm"
---

# Loop::IsOuter

This method is obsolete and has been superseded by [Loop2::IsOuter](sldworksAPI.chm::/Loop2/Loop2__IsOuter.htm).

Description

This method tells you if the loop is the outermost loop on the face.

Syntax (OLE Automation)

retval = Loop.IsOuter ()

| Return: | (BOOL) retval | TRUE if the loop is the outermost loop, FALSE if not |
| --- | --- | --- |

Syntax (COM)

status = Loop->IsOuter ( &retval )

| Output: | (VARIANT_BOOL) retval | TRUE if the loop is the outermost loop, FALSE if not |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Some situations exist where no clear outer loop is defined. For example, the cylindrical face of an extruded circle has two loops that could be considered outer loops.
