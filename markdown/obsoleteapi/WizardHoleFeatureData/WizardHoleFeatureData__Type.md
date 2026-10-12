---
title: "WizardHoleFeatureData::Type"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/WizardHoleFeatureData/WizardHoleFeatureData__Type.htm"
---

# WizardHoleFeatureData::Type

This property is obsolete and has been superseded by [WizardHoleFeatureData2::Type](sldworksAPI.chm::/WizardHoleFeatureData2/WizardHoleFeatureData2__Type.htm).

Description

This property gets or sets the hole wizard feature hole type.

Syntax (OLE Automation)

holeType = WizardHoleFeatureData.Type (VB Get property)

WizardHoleFeatureData.Type = holeType (VB Set property)

holeType = WizardHoleFeatureData.GetType ( ) (C++ Get property)

WizardHoleFeatureData.SetType ( holeType ) (C++ Set property)

| Property: | (int) holeType | Hole type as defined in swWzdHoleTypes_e |
| --- | --- | --- |

Syntax (COM)

status = WizardHoleFeatureData ->get_Type ( &holeType )

status = WizardHoleFeatureData ->put_Type ( holeType )

| Property: | (int) holeType | Hole type as defined in swWzdHoleTypes_e |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
