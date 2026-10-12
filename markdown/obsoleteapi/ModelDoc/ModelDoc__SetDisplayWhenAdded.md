---
title: "ModelDoc::SetDisplayWhenAdded"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetDisplayWhenAdded.htm"
---

# ModelDoc::SetDisplayWhenAdded

This method is obsolete and has been superseded by [ModelDoc2::SetDisplayWhenAdded](../ModelDoc2/ModelDoc2__SetDisplayWhenAdded.htm).

Description

This method sets whether new sketch entities are displayed upon creation. The sketch entities will appear on the screen once a ModelDoc::GraphicsRedraw2 or ModelDoc::EditRebuild is performed (ModelDoc::GraphicsRedraw2 is much faster than an ModelDoc::EditRebuild).

Syntax (OLE Automation)

void ModelDoc.SetDisplayWhenAdded ( setting)

| Input: | (BOOL) setting | TRUE if new sketch entities are to be displayed when added, FALSE otherwise |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->SetDisplayWhenAdded ( setting )

| Input: | (VARIANT_BOOL) setting | TRUE if new sketch entities are to be displayed when added, FALSE otherwise |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This setting remains even after your program run has ended. Therefore, it is recommended that you reset this parameter to TRUE at the end of your program. For example, if you have ended your program and the display is set to FALSE, then the user would have difficulty performing selections and newly created entities would not be seen until a redraw or a rebuild.

The ModelDoc::SetAddToDB and ModelDoc::SetDisplayWhenAdded functions also increase performance during sketch entity creation.

NOTE: ModelDoc::SetDisplayWhenAdded settings are ignored unless ModelDoc::SetAddToDB is TRUE.
