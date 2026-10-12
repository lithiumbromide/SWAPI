---
title: "DrawingDoc::ExplodeBlockInstance"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__ExplodeBlockInstance.htm"
---

# DrawingDoc::ExplodeBlockInstance

This method is obsolete and has been superseded by [SketchManager::ExplodeSketchBlockInstance](sldworksAPI.chm::/SketchManager/SketchManager__ExplodeSketchBlockInstance.htm).

Description

This method explodes the selected block instances into individual entities.

Syntax (OLE Automation)

retval = DrawingDoc.ExplodeBlockInstance ( )

| Output: | (VARIANT_BOOL) retval | TRUE if the block instance is exploded, FALSE if not |
| --- | --- | --- |

Syntax (COM)

status = DrawingDoc->ExplodeBlockInstance ( &retval )

| Output: | (VARIANT_BOOL) retval | TRUE if the block instance is exploded, FALSE if not |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
