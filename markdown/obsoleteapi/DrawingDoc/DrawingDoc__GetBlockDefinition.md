---
title: "DrawingDoc::GetBlockDefinition"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__GetBlockDefinition.htm"
---

# DrawingDoc::GetBlockDefinition

This method is obsolete and has been superseded by [SketchManager::GetSketchBlockDefinitions](sldworksAPI.chm::/SketchManager/SketchManager__GetSketchBlockDefinitions.htm).

Description

This method gets the specified block definition.

Syntax (OLE Automation)

retval = DrawingDoc.GetBlockDefinition ( Name )

| Input: | (BSTR) Name | Block definition name |
| --- | --- | --- |
| Output: | (LPBLOCKDEFINITION) retval | Pointer to the block definition |

Syntax (COM)

status = DrawingDoc->GetBlockDefinition ( Name, &retval )

| Input: | (BSTR) Name | Block definition name |
| --- | --- | --- |
| Output: | (LPBLOCKDEFINITION) retval | Pointer to the block definition |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
