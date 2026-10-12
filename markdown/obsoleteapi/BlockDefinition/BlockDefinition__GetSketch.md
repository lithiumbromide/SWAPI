---
title: "BlockDefinition::GetSketch"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/BlockDefinition/BlockDefinition__GetSketch.htm"
---

# BlockDefinition::GetSketch

This method is obsolete and has been superseded by [SketchBlockDefinition::GetSketch](sldworksAPI.chm::/SketchBlockDefinition/SketchBlockDefinition__GetSketch.htm).

Description

This method gets the sketch for this block definition.

Syntax (OLE Automation)

retval = BlockDefinition.GetSketch ( )

| Output: | (LPSKETCH) retval | Pointer to the Sketch object |
| --- | --- | --- |

Syntax (COM)

status = BlockDefinition->GetSketch ( &retval )

| Output: | (LPSKETCH) retval | Pointer to the Sketch object |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You cannot modify the returned sketch. It is read-only.
