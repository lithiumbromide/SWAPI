---
title: "BlockDefinition::GetNotes"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/BlockDefinition/BlockDefinition__GetNotes.htm"
---

# BlockDefinition::GetNotes

This method is obsolete and has been superseded by [SketchBlockDefinition::GetNotes](sldworksAPI.chm::/SketchBlockDefinition/SketchBlockDefinition__GetNotes.htm).

Description

This method gets the notes in the block definition.

Syntax (OLE Automation)

retval = BlockDefinition.GetNotes ( )

| Output: | (VARIANT) retval | Notes in the block definition |
| --- | --- | --- |

Syntax (COM)

status = BlockDefinition->IGetNotes ( numNotes, retval )

| Input: | (long) numNotes | Number of notes in the block definition |
| --- | --- | --- |
| Output: | (LPNOTE*) retval | Array of notes of size numNotes |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
