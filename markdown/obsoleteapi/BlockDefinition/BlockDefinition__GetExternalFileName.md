---
title: "BlockDefinition::GetExternalFileName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/BlockDefinition/BlockDefinition__GetExternalFileName.htm"
---

# BlockDefinition::GetExternalFileName

This method is obsolete and has been superseded by [SketchBlockDefinition::FileName](sldworksAPI.chm::/SketchBlockDefinition/SketchBlockDefinition__FileName.htm).

Description

This method gets the name of the file that this block definition references.

Syntax (OLE Automation)

Filename = BlockDefinition.GetExternalFileName ( )

| Output: | (BSTR) Filename | Name of the file |
| --- | --- | --- |

Syntax (COM)

status = BlockDefinition->GetExternalFileName ( &Filename )

| Output: | (BSTR) Filename | Name of the file |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method gets the name of the file with which this block definition is associated, regardless of whether or not the link is enabled. SolidWorks continues to store the name of the file if the link is disabled.

Use BlockDefiniton::GetUseExternalFile to determine whether this block definition is linked to an external file. Use BlockDefinition::SetExternalFileName to set the name of the external file and enable or disable the link.
