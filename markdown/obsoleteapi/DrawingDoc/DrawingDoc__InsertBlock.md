---
title: "DrawingDoc::InsertBlock"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__InsertBlock.htm"
---

# DrawingDoc::InsertBlock

This method is obsolete and has been superseded by [SketchManager::InsertSketchBlockInstance](sldworksAPI.chm::/SketchManager/SketchManager__InsertSketchBlockInstance.htm).

Description

This method inserts a new block instance into the drawing from a local block or block file (.sldblk).

NOTE: This method does not work for drawings opened in view-only mode.

Syntax (OLE Automation)

retval = DrawingDoc.InsertBlock ( blockName, X, Y, Angle, Scale )

| Input: | (BSTR) blockName | Local block name or full path of the .sldblk file from which to insert the block |
| --- | --- | --- |
| Input: | (double) X | X coordinate of the location of the origin of the block instance |
| Input: | (double) Y | Y coordinate of the location of the origin of the block instance |
| Input: | (double) Angle | Rotation angle of the block instance |
| Input: | (double) Scale | Scale of the block instance |
| Output: | (LPBLOCKINSTANCE) retval | Pointer to the block instance that is created |

Syntax (COM)

status = DrawingDoc->InsertBlock ( blockName, X, Y, Angle, Scale, &retval )

| Input: | (BSTR) blockName | Local block name or full path of the .sldblk file from which to insert the block |
| --- | --- | --- |
| Input: | (double) X | X coordinate of the location of the origin of the block instance |
| Input: | (double) Y | Y coordinate of the location of the origin of the block instance |
| Input: | (double) Angle | Rotation angle of the block instance |
| Input: | (double) Scale | Scale of the block instance |
| Output: | (LPBLOCKINSTANCE) retval | Pointer to the block instance that is created |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method creates a block definition if the block definition does not exist.

- or -

If the definition exists, then this method uses that block definition to create the block instance. The name of the block instance is the same as the filename of the block file, without the filename extension.

TIP: Instead of using this method multiple times to insert the same block, use it once to insert the first block instance. Next, use the return interface pointer to get the block definition, BlockInstance::Definition, and then use the BlockDefinition::InsertInstance method to insert the rest of the blocks.

To save a block instance and its definition into a block file (.sldblk), use DrawingDoc::SaveBlock.
