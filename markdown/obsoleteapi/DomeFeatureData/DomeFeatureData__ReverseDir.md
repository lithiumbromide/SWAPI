---
title: "DomeFeatureData::ReverseDir"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DomeFeatureData/DomeFeatureData__ReverseDir.htm"
---

# DomeFeatureData::ReverseDir

This property is obsolete and has been superseded by [DomeFeatureData2::ReverseDir](sldworksAPI.chm::/DomeFeatureData2/DomeFeatureData2__ReverseDir.htm).

Description

This property controls whether the dome is convex or concave.

Syntax (OLE Automation)

ReverseDir= DomeFeatureData.ReverseDir (VB Get property)

DomeFeatureData.ReverseDir= ReverseDir (VB Set property)

ReverseDir= DomeFeatureData.GetReverseDir ( ) (C++ Get property)

DomeFeatureData.SetReverseDir ( ReverseDir) (C++ Set property)

| Property: | (BOOL) ReverseDir | TRUE if the dome is concave, FALSE if it is convex |
| --- | --- | --- |

Syntax (COM)

status = DomeFeatureData-> get_ReverseDir( &ReverseDir)

status = DomeFeatureData-> put_ReverseDir( ReverseDir)

| Property: | (VARIANT_BOOL) ReverseDir | TRUE if the dome is concave, FALSE if it is convex |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This property does not affect geometry until you call Feature::ModifyDefinition.
