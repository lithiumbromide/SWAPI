---
title: "RibFeatureData::Thickness"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/RibFeatureData/RibFeatureData__Thickness.htm"
---

# RibFeatureData::Thickness

This property is obsolete and has been superseded by [RibFeatureData2::Thickness](sldworksAPI.chm::/RibFeatureData2/RibFeatureData2__Thickness.htm).

Description

This property controls the overall thickness of the Rib.

Syntax (OLE Automation)

Thickness= RibFeatureData.Thickness (VB Get property)

RibFeatureData.Thickness= Thickness (VB Set property)

Thickness= RibFeatureData.GetThickness ( ) (C++ Get property)

RibFeatureData.SetThickness ( Thickness ) (C++ Set property)

| Property: | (double) Thickness | Thickness of the Rib |
| --- | --- | --- |

Syntax (COM)

status = RibFeatureData-> get_Thickness( &Thickness)

status = RibFeatureData-> put_Thickness( Thickness)

| Property: | (double) Thickness | Thickness of the Rib |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Changing the value of this property does not affect geometry until Feature::ModifyDefinition is called.
