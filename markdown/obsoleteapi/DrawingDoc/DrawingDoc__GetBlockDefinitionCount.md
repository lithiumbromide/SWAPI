---
title: "DrawingDoc::GetBlockDefinitionCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__GetBlockDefinitionCount.htm"
---

# DrawingDoc::GetBlockDefinitionCount

This method is obsolete and has been superseded by [SketchManager::GetSketchBlockDefinitionCount](sldworksAPI.chm::/SketchManager/SketchManager__GetSketchBlockDefinitionCount.htm).

Description

This method gets the number of block definitions in this drawing.

Syntax (OLE Automation)

retval = DrawingDoc.GetBlockDefinitionCount ( )

| Output: | (long) retval | Number of block definitions |
| --- | --- | --- |

Syntax (COM)

status = DrawingDoc->GetBlockDefinitionCount ( &retval )

| Output: | (long) retval | Number of block definitions |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
