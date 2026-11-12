---
title: "BlockInstance::Scale2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/BlockInstance/BlockInstance__Scale2.htm"
---

# BlockInstance::Scale2

This property is obsolete and has been superseded by [SketchBlockInstance::Scale](sldworksAPI.chm::/SketchBlockInstance/SketchBlockInstance__Scale.htm).

Description

This property gets or sets the scale for the block.

Syntax (OLE Automation)

Scale = BlockInstance.Scale2 (VB Get property)

BlockInstance.Scale2 = Scale (VB Set property)

Scale = BlockInstance.GetScale2 ( ) (C++ Get property)

BlockInstance.SetScale2 ( Scale ) (C++ Set property)

| Property: | (double) Scale | Block scale: 0.0000001 to 500000 |
| --- | --- | --- |

Syntax (COM)

status = BlockInstance->get_Scale2 ( &Scale )

status = BlockInstance->put_Scale2 ( Scale )

| Property: | (double) Scale | Block scale: 0.0000001 to 500000 |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
