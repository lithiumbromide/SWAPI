---
title: "DrawingDoc::GetBlockDefinitions"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__GetBlockDefinitions.htm"
---

# DrawingDoc::GetBlockDefinitions

This method is obsolete and has been superseded by [SketchManager::GetSketchBlockDefinitions](sldworksAPI.chm::/SketchManager/SketchManager__GetSketchBlockDefinitions.htm).

Description

This method gets the block definitions in this drawing.

Syntax (OLE Automation)

retval = DrawingDoc.GetBlockDefinitions ( )

| Output: | (VARIANT) retval | Array of block definitions |
| --- | --- | --- |

Syntax (COM)

status = DrawingDoc->IGetBlockDefinitions ( Count, retval )

| Input: | (long) Count | Number of block definitions |
| --- | --- | --- |
| Output: | (LPBLOCKDEFINITION*) retval | Array of block definitions of size Count |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
