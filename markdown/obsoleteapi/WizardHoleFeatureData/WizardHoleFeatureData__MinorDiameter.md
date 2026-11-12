---
title: "WizardHoleFeatureData::MinorDiameter"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/WizardHoleFeatureData/WizardHoleFeatureData__MinorDiameter.htm"
---

# WizardHoleFeatureData::MinorDiameter

This property is obsolete and has been superseded by [WizardHoleFeatureData2::MinorDiameter](sldworksAPI.chm::/WizardHoleFeatureData2/WizardHoleFeatureData2__MinorDiameter.htm).

Description

This property gets or sets the hole wizard feature minor diameter for tapered hole.

Syntax (OLE Automation)

minorDia = WizardHoleFeatureData.MinorDiameter (VB Get property)

WizardHoleFeatureData.MinorDiameter = minorDia (VB Set property)

minorDia = WizardHoleFeatureData.GetMinorDiameter ( ) (C++ Get property)

WizardHoleFeatureData.SetMinorDiameter ( minorDia ) (C++ Set property)

| Property: | (double) minorDia | Minor diameter for tapered hole |
| --- | --- | --- |

Syntax (COM)

status = WizardHoleFeatureData ->get_MinorDiameter ( &minorDia )

status = WizardHoleFeatureData ->put_MinorDiameter ( minorDia )

| Property: | (double) minorDia | Minor diameter for tapered hole |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This property is relevant only for tapered and tapered drilled holes.
