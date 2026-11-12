---
title: "BlockDefinition::GetBasePoint"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/BlockDefinition/BlockDefinition__GetBasePoint.htm"
---

# BlockDefinition::GetBasePoint

This method is obsolete and has been superseded by [SketchBlockDefinition::InsertionPoint](sldworksAPI.chm::/SketchBlockDefinition/SketchBlockDefinition__InsertionPoint.htm).

Description

This method gets the base point of this block definition.

Syntax (OLE Automation)

retval = BlockDefinition.GetBasePoint ()

| Output: | (VARIANT) retval | VARIANT of type SafeArray identifying the x,y,z values of the base point |
| --- | --- | --- |

Syntax (COM)

status = BlockDefinition->IGetBasePoint ( retval)

| Output: | (double) retval | Array of doubles identifying the x,y,z values of the base point |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The base point of a block definition is the point around which instances of the block rotate or scale. It is the origin of the sketch containing the geometry that is part of the block definition. This implies that the base point of a block definition is always (0,0,0), because the sketch origin is (0,0). Therefore, BlockDefinition::GetBasePoint always returns (0,0,0).

The BlockDefinition::SetBasePoint values are specified relative to the current base point. However, when the base point is changed, it must become the sketch origin again, that is, it must become the (0,0,0) point again. So, if you use the this method and then immediately use BlockDefintion::GetBasePoint, it returns (0,0,0).

Changing the base point does not affect how instances of the block look in a drawing, so when the base point changes, the sketch geometry in the definition is adjusted to allow for that behavior. This means that if you get the block definition sketch and sketch geometry, the sketch geometry coordinates will be different after the base point is changed.

If you use Annotation::GetPosition and Annotation::SetPosition on instances of the block, you will notice that the instance position is also affected by a change in the block definition base point, even though the instance does not appear different on the drawing. The instance position is where the base point of the definition is in the instance, so if the base point of the definition changes, the instance position value will be different.
