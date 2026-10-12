---
title: "ModelDoc2::SetAddToDB"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__SetAddToDB.htm"
---

# ModelDoc2::SetAddToDB

This method is obsolete and has been superseded by [SketchManager::AddToDB](sldworksAPI.chm::/SketchManager/SketchManager__AddToDB.htm).

Description

This method sets whether sketch entities are added directly to the SolidWorks database.

Syntax (OLE Automation)

void ModelDoc2.SetAddToDB ( setting)

| Input: | (BOOL) setting | TRUE to add items directly to the SolidWorks database, FALSE otherwise |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc2->SetAddToDB ( setting )

| Input: | (VARIANT_BOOL) setting | TRUE to add items directly to the SolidWorks database, FALSE otherwise |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

One of the benefits of adding sketch entities directly to the database is that you can avoid grid and entity snapping. For example, if you create a sketch line whose endpoint is near another entity or near a grid point, the new line endpoint snaps to the other item or grid point. Setting ModelDoc2::SetAddToDB to TRUE avoids this behavior during sketch entity creation.

ModelDoc2::SetAddToDB and ModelDoc2::SetDisplayWhenAdded also increase performance during sketch entity creation. ModelDoc2::SetDisplayWhenAdded requires that ModelDoc2::SetAddToDB is TRUE.

If you want to constrain all the sketch entities after creation, use Sketch::ConstrainAll.

After setting ModelDoc2::SetAddToDB to TRUE, you must set it back to FALSE to restore SolidWorks to its normal operating mode.
