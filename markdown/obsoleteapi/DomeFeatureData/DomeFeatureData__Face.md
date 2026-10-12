---
title: "DomeFeatureData::Face"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DomeFeatureData/DomeFeatureData__Face.htm"
---

# DomeFeatureData::Face

This method is obsolete and has been superseded by [DomeFeatureData2::Face](../DomeFeatureData2/DomeFeatureData2__Face.htm).

Description

This property gets or sets the planar face associated with the dome.

Syntax (OLE Automation)

Set Face = DomeFeatureData.Face (VB Get property)

Set DomeFeatureData.Face= Face (VB Set property)

Face = DomeFeatureData.GetFace ( ) (C++ Get property)

DomeFeatureData.SetFace ( Face) (C++ Set property)

| Property: | (LPDISPATCH) Face | Dispatch pointer for the face associated with the dome |
| --- | --- | --- |

Syntax (COM)

status = DomeFeatureData-> get_Face( &Face)

status = DomeFeatureData-> put_Face( Face)

| Property: | (LPFACE) Face | Pointer to the face associated with the dome |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This property does not affect geometry until you call Feature::ModifyDefinition.
