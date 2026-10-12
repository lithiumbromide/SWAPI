---
title: "ModelDoc2::SetDisplayWhenAdded"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__SetDisplayWhenAdded.htm"
---

# ModelDoc2::SetDisplayWhenAdded

This method is obsolete and has been superseded by [SketchManager::DisplayWhenAdded](sldworksAPI.chm::/SketchManager/SketchManager__DisplayWhenAdded.htm).

Description

This method sets whether new sketch entities are displayed when created.

Syntax (OLE Automation)

void ModelDoc2.SetDisplayWhenAdded ( setting)

| Input: | (BOOL) setting | TRUE to display new sketch entities when added, FALSE otherwise |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc2->SetDisplayWhenAdded ( setting )

| Input: | (VARIANT_BOOL) setting | TRUE to display new sketch entities when added, FALSE otherwise |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The sketch entities appear on the screen after performing ModelDoc2::GraphicsRedraw2 or ModelDoc2::EditRebuild3 is performed. Also, ModelDoc2::SetAddToDB must be TRUE to use this method's settings.

This display setting remains even after your program run has ended. Therefore, it is recommended that you reset this parameter to TRUE at the end of your program. For example, if you have ended your program and the display is set to FALSE, then the user would have difficulty performing selections and newly created entities would not be seen until a redraw or a rebuild.

NOTES:

- ModelDoc2::GraphicsRedraw2 is much faster than ModelDoc2::EditRebuild3.
- ModelDoc2::SetAddToDB and ModelDoc2::SetDisplayWhenAdded also increase performance during sketch entity creation.
