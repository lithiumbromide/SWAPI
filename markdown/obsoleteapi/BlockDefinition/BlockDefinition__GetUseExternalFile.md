---
title: "BlockDefinition::GetUseExternalFile"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/BlockDefinition/BlockDefinition__GetUseExternalFile.htm"
---

# BlockDefinition::GetUseExternalFile

This method is obsolete and has been superseded by [SketchBlockDefinition::LinkToFile](sldworksAPI.chm::/SketchBlockDefinition/SketchBlockDefinition__LinkToFile.htm).

Description

This method determines whether this block definition is currently linked to an external file.

Syntax (OLE Automation)

UseFile = BlockDefinition.GetUseExternalFile ( )

| Output: | (BOOL) UseFile | TRUE if this block definition is linked to an external file, FALSE if not |
| --- | --- | --- |

Syntax (COM)

status = BlockDefinition->GetUseExternalFile ( &UseFile )

| Output: | (VARIANT_BOOL) UseFile | TRUE if this block definition is linked to an external file, FALSE if not |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method indicates whether the block definition is linked to an external file, which you can enable or disable on the block definition without destroying the file name. That is, the file name continues to be stored even if the link is disabled.

To get the name of the external file, use BlockDefinition::GetExternalFileName. To set the name of the external file and enable or disable the link, use BlockDefinition::SetUseExternalFileName.
