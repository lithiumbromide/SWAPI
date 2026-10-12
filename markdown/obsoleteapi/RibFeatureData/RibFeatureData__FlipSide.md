---
title: "RibFeatureData::FlipSide"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/RibFeatureData/RibFeatureData__FlipSide.htm"
---

# RibFeatureData::FlipSide

This property is obsolete and has been superseded by [RibFeatureData2::FlipSide](sldworksAPI.chm::/RibFeatureData2/RibFeatureData2__FlipSide.htm).

Description

This property controls whether the material is added to the reverse side.

Syntax (OLE Automation)

FlipSide= RibFeatureData.FlipSide (VB Get property)

RibFeatureData.FlipSide= FlipSide (VB Set property)

FlipSide= RibFeatureData.GetFlipSide ( ) (C++ Get property)

RibFeatureData.SetFlipSide ( FlipSide) (C++ Set property)

| Property: | (BOOL) FlipSide | TRUE if the material is added to the reverse side |
| --- | --- | --- |

Syntax (COM)

status = RibFeatureData-> get_FlipSide( &FlipSide)

status = RibFeatureData-> put_FlipSide( FlipSide)

| Property: | (VARIANT_BOOL) FlipSide | TRUE if the material is added to the reverse side |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Changing the value of this property does not affect geometry until Feature::ModifyDefinition is called.
