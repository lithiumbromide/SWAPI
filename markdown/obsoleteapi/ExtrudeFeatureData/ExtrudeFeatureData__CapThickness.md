---
title: "ExtrudeFeatureData::CapThickness"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ExtrudeFeatureData/ExtrudeFeatureData__CapThickness.htm"
---

# ExtrudeFeatureData::CapThickness

This property is obsolete and has been superseded by [ExtrudeFeatureData2::CapThickness](sldworksAPI.chm::/ExtrudeFeatureData2/ExtrudeFeatureData2__CapThickness.htm).

Description

This property gets or sets the end cap thickness for a thin base extrude feature.

Syntax (OLE Automation)

capThickness = ExtrudeFeatureData.CapThickness (VB Get property)

ExtrudeFeatureData.CapThickness = capThickness (VB Set property)

capThickness = ExtrudeFeatureData.GetCapThickness ( ) (C++ Get property)

ExtrudeFeatureData.SetCapThickness ( capThickness ) (C++ Set property)

| Property: | (double) capThickness | Thickness of the end cap |
| --- | --- | --- |

Syntax (COM)

status = ExtrudeFeatureData->get_CapThickness ( &capThickness )

status = ExtrudeFeatureData->put_CapThickness ( capThickness )

| Property: | (double) capThickness | Thickness of the end cap |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
