---
title: "DrawingDoc::GetEditBlock"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__GetEditBlock.htm"
---

# DrawingDoc::GetEditBlock

This method is obsolete and has been superseded by [SketchManager::EditSketchBlock](sldworksAPI.chm::/SketchManager/SketchManager__EditSketchBlock.htm) and [SketchManager::EndEditSketchBlock](sldworksAPI.chm::/SketchManager/SketchManager__EndEditSketchBlock.htm).

Description

This method gets whether or not a block is being edited in the drawing.

Syntax (OLE Automation)

retval = DrawingDoc.GetEditBlock ()

| Output: | (VARIANT_BOOL) retval | TRUE if a block is being edited, FALSE if not |
| --- | --- | --- |

Syntax (COM)

status = DrawingDoc->GetEditBlock ( &retval)

| Output: | (VARIANT_BOOL) retval | TRUE if a block is being edited, FALSE if not |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
