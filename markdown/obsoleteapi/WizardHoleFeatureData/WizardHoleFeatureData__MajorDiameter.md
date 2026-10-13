---
title: "WizardHoleFeatureData::MajorDiameter"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/WizardHoleFeatureData/WizardHoleFeatureData__MajorDiameter.htm"
---

# WizardHoleFeatureData::MajorDiameter

This property is obsolete and has been superseded by [WizardHoleFeatureData2::MajorDiameter](sldworksAPI.chm::/WizardHoleFeatureData2/WizardHoleFeatureData2__MajorDiameter.htm).

Description

This property gets or sets the hole wizard feature major diameter for tapered hole.

Syntax (OLE Automation)

majorDia = WizardHoleFeatureData.MajorDiameter (VB Get property)

WizardHoleFeatureData.MajorDiameter = majorDia (VB Set property)

majorDia = WizardHoleFeatureData.GetMajorDiameter ( ) (C++ Get property)

WizardHoleFeatureData.SetMajorDiameter ( majorDia ) (C++ Set property)

| Property: | (double) majorDia | Major diameter for tapered hole |
| --- | --- | --- |

Syntax (COM)

status = WizardHoleFeatureData ->get_MajorDiameter ( &majorDia )

status = WizardHoleFeatureData ->put_MajorDiameter ( majorDia )

| Property: | (double) majorDia | Major diameter for tapered hole |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This property is relevant only for tapered and tapered drilled holes.
