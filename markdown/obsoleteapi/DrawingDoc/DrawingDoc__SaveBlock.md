---
title: "DrawingDoc::SaveBlock"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__SaveBlock.htm"
---

# DrawingDoc::SaveBlock

This method is obsolete and has been superseded by [SketchBlockDefinition::Save](sldworksAPI.chm::/SketchBlockDefinition/SketchBlockDefinition__Save.htm).

Description

This method saves the selected block instance and its definition to a block file (.sldblk).

Syntax (OLE Automation)

retval = DrawingDoc.SaveBlock ( fileName )

| Input: | (BSTR) fileName | Full path name of the block file (.sldblk) into which to save the block |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the block is saved to the file, FALSE if not |

Syntax (COM)

status = DrawingDoc->SaveBlock ( fileName, &retval )

| Input: | (BSTR) fileName | Full path name of the block file (.sldblk) into which to save the block |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the block is saved to the file, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

To insert a block instance into the drawing from a block file (.sldblk), use DrawingDoc::InsertBlock.

If a block definition or block instance is not preselected, then this method returns False.
