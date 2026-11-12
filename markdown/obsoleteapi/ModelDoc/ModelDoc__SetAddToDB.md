---
title: "ModelDoc::SetAddToDB"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetAddToDB.htm"
---

# ModelDoc::SetAddToDB

This method is obsolete and has been superseded by [ModelDoc2::SetAddToDB](../ModelDoc2/ModelDoc2__SetAddToDB.htm).

Description

This method sets whether sketch entities are added directly to the SolidWorks database.

Syntax (OLE Automation)

void ModelDoc.SetAddToDB ( setting)

| Input: | (BOOL) setting | TRUE if you want items added directly to the SolidWorks database, FALSE otherwise |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->SetAddToDB ( setting )

| Input: | (VARIANT_BOOL) setting | TRUE if you want items added directly to the SolidWorks database, FALSE otherwise |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

One of the benefits of adding sketch entities directly to the database is that you can avoid grid and entity snapping. For example, if you create a sketch line whose endpoint is near another entity or near a grid point, the new line endpoint will snap to the other item or grid point. Using SetAddToDB( True ) will avoid this behavior during sketch entity creation.

The [SetAddToDB](ModelDoc__SetAddToDB.htm) and [SetDisplayWhenAdded](ModelDoc__SetDisplayWhenAdded.htm) functions will also will increase performance during sketch entity creation. [SetDisplayWhenAdded](ModelDoc__SetDisplayWhenAdded.htm) requires that SetAddToDB is TRUE.

If you want to constrain all the sketch entities after creation, you can use the Sketch::ConstrainAll function.
