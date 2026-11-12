---
title: "RibFeatureData::IsTwoSided"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/RibFeatureData/RibFeatureData__IsTwoSided.htm"
---

# RibFeatureData::IsTwoSided

This property is obsolete and has been superseded by [RibFeatureData2::IsTwoSided](sldworksAPI.chm::/RibFeatureData2/RibFeatureData2__IsTwoSided.htm).

Description

This property controls whether the rib is created on two sides of the Mid Plane, or in a single direction (see RibFeatureData::ReverseThicknessDir).

Syntax (OLE Automation)

IsTwoSided= RibFeatureData.IsTwoSided (VB Get property)

RibFeatureData.IsTwoSided= IsTwoSided (VB Set property)

IsTwoSided= RibFeatureData.GetIsTwoSided ( ) (C++ Get property)

RibFeatureData.SetIsTwoSided ( IsTwoSided) (C++ Set property)

| Property: | (BOOL) IsTwoSided | TRUE if the rib is extruded either side of the midplane, FALSE if it is single sided |
| --- | --- | --- |

Syntax (COM)

status = RibFeatureData-> get_IsTwoSided( &IsTwoSided)

status = RibFeatureData-> put_IsTwoSided( IsTwoSided)

| Property: | (VARIANT_BOOL) IsTwoSided | TRUE if the rib is extruded either side of the midplane, FALSE if it is single sided |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Changing the value of this property does not affect geometry until Feature::ModifyDefinition is called.
