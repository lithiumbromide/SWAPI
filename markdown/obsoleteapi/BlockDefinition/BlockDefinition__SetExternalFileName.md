---
title: "BlockDefinition::SetExternalFileName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/BlockDefinition/BlockDefinition__SetExternalFileName.htm"
---

# BlockDefinition::SetExternalFileName

This method is obsolete and has been superseded by [SketchBlockDefinition::FileName](sldworksAPI.chm::/SketchBlockDefinition/SketchBlockDefinition__FileName.htm).

Description

This method sets the name of the file that the block definition references.

Syntax (OLE Automation)

retval = BlockDefinition.SetExternalFileName ( Filename )

| Input: | (BSTR) Filename | Name of the file |
| --- | --- | --- |
| Output: | (long) retval | Status of the external file link as defined in swBlockDefinitionExtFileStatus_e |

Syntax (COM)

status = BlockDefinition->SetExternalFileName ( Filename, &retval )

| Input: | (BSTR) Filename | Name of the file |
| --- | --- | --- |
| Output: | (long) retval | Status of the external file link as defined in swBlockDefinitionExtFileStatus_e |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

To determine if this block definition is currently linked to an external file, use BlockDefinition::GetUseExternalFile. To get the name of the external file, use BlockDefinition::GetExternalFileName.
