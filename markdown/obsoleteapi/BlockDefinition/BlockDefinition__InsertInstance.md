---
title: "BlockDefinition::InsertInstance"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/BlockDefinition/BlockDefinition__InsertInstance.htm"
---

# BlockDefinition::InsertInstance

This method is obsolete and has been superseded by [SketchManager::InsertSketchBlockInstance](sldworksAPI.chm::/SketchManager/SketchManager__InsertSketchBlockInstance.htm).

Description

This method inserts an instance of a block from the block definition.

NOTE: This method does not work for drawings opened in view-only mode.

Syntax (OLE Automation)

retval = BlockDefinition.InsertInstance ( X, Y, Angle, Scale )

| Input: | (double) X | X coordinate of the instance position |
| --- | --- | --- |
| Input: | (double) Y | Y coordinate of the instance position |
| Input: | (double) Angle | Angle of the instance |
| Input: | (double) Scale | Scale of the instance |
| Output: | (LPBLOCKINSTANCE) retval | Pointer to the new instance |

Syntax (COM)

status = BlockDefinition->InsertInstance ( X, Y, Angle, Scale, &retval )

| Input: | (double) X | X coordinate of the instance position |
| --- | --- | --- |
| Input: | (double) Y | Y coordinate of the instance position |
| Input: | (double) Angle | Angle of the instance |
| Input: | (double) Scale | Scale of the instance |
| Output: | (LPBLOCKINSTANCE) retval | Pointer to the new instance |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
