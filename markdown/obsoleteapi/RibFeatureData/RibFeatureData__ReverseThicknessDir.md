---
title: "RibFeatureData::ReverseThicknessDir"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/RibFeatureData/RibFeatureData__ReverseThicknessDir.htm"
---

# RibFeatureData::ReverseThicknessDir

This property is obsolete and has been superseded by [RibFeatureData2::ReverseThicknessDir](sldworksAPI.chm::/RibFeatureData2/RibFeatureData2__ReverseThicknessDir.htm).

Description

If a rib is single-sided, then this property specifies whether the extrusion is on the reverse side.

Syntax (OLE Automation)

Reverse= RibFeatureData.ReverseThicknessDir (VB Get property)

RibFeatureData.ReverseThicknessDir= Reverse (VB Set property)

Reverse= RibFeatureData.GetReverseThicknessDir ( ) (C++ Get property)

RibFeatureData.SetReverseThicknessDir ( Reverse) (C++ Set property)

| Property: | (BOOL) Reverse | TRUE if the rib is extruded on the reverse side |
| --- | --- | --- |

Syntax (COM)

status = RibFeatureData-> get_ReverseThicknessDir( &Reverse)

status = RibFeatureData-> put_ReverseThicknessDir( Reverse)

| Property: | (VARIANT_BOOL) Reverse | TRUE if the rib is extruded on the reverse side |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Changing the value of this property does not affect geometry until Feature::ModifyDefinition is called.
