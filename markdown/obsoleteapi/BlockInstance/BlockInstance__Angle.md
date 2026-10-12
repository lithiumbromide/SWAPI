---
title: "BlockInstance::Angle"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/BlockInstance/BlockInstance__Angle.htm"
---

# BlockInstance::Angle

This property is obsolete and has been superseded by [SketchBlockInstance::Angle](sldworksAPI.chm::/SketchBlockInstance/SketchBlockInstance__Angle.htm).

Description

This property gets or sets the rotation angle of this block.

Syntax (OLE Automation)

Angle = BlockInstance.Angle (VB Get property)

BlockInstance.Angle = Angle (VB Set property)

Angle = BlockInstance.GetAngle ( ) (C++ Get property)

BlockInstance.SetAngle ( Angle ) (C++ Set property)

| Property: | (double) Angle | Block angle |
| --- | --- | --- |

Syntax (COM)

status = BlockInstance->get_Angle ( &Angle )

status = BlockInstance->put_Angle ( Angle )

| Property: | (double) Angle | Block angle |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
