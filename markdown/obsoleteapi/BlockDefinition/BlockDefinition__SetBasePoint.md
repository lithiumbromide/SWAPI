---
title: "BlockDefinition::SetBasePoint"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/BlockDefinition/BlockDefinition__SetBasePoint.htm"
---

# BlockDefinition::SetBasePoint

This method is obsolete and has been superseded by [SketchBlockDefinition::InsertionPoint](sldworksAPI.chm::/SketchBlockDefinition/SketchBlockDefinition__InsertionPoint.htm).

Description

This method sets the base point of this block definition.

Syntax (OLE Automation)

retval = BlockDefinition.SetBasePoint ( BasePoint)

| Input: | (VARIANT) BasePoint | VARIANT of type SafeArray identifying the x,y,z values of the base point NOTE: These values are not absolute coordinates, but a translation vector. |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if base point is set, FALSE if not |

Syntax (COM)

status = BlockDefinition->ISetBasePoint ( BasePoint, &retval)

| Property: | (double) BasePoint | Array of doubles identifying the x,y,z values of the base point NOTE: These values are not absolute coordinates, but a translation vector. |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if base point is set, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

When you insert a block in a drawing, the block instance is located so that its base point is at the insertion point.

The base point of a block definition is the point around which instances of the block rotate or scale. It is the origin of the sketch containing the geometry that is part of the block definition. This implies that the base point of a block definition is always (0,0,0), because the sketch origin is (0,0). Therefore, BlockDefinition::GetBasePoint always returns (0,0,0).

The BlockDefinition::SetBasePoint values are specified relative to the current base point. However, when the base point is changed, it must become the sketch origin again, that is, it must become the (0,0,0) point again. So, if you use the this method and then immediately use BlockDefintion::GetBasePoint, it returns (0,0,0).

Changing the base point does not affect how instances of the block look in a drawing, so when the base point changes, the sketch geometry in the definition is adjusted to allow for that behavior. This means that if you get the block definition sketch and sketch geometry, the sketch geometry coordinates will be different after the base point is changed.
