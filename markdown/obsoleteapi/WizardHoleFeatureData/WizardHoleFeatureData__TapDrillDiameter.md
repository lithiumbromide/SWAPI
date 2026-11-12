---
title: "WizardHoleFeatureData::TapDrillDiameter"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/WizardHoleFeatureData/WizardHoleFeatureData__TapDrillDiameter.htm"
---

# WizardHoleFeatureData::TapDrillDiameter

This property is obsolete and has been superseded by [WizardHoleFeatureData2::TapDrillDiameter](sldworksAPI.chm::/WizardHoleFeatureData2/WizardHoleFeatureData2__TapDrillDiameter.htm).

Description

This property gets or sets the hole wizard feature tap drill diameter.

Syntax (OLE Automation)

tapdrillDia = WizardHoleFeatureData.TapDrillDiameter (VB Get property)

WizardHoleFeatureData.TapDrillDiameter= tapdrillDia (VB Set property)

tapdrillDia = WizardHoleFeatureData.GetTapDrillDiameter ( ) (C++ Get property)

WizardHoleFeatureData.SetTapDrillDiameter ( tapdrillDia ) (C++ Set property)

| Property: | (double) tap drillDia | Tap drill diameter |
| --- | --- | --- |

Syntax (COM)

status = WizardHoleFeatureData ->get_TapDrillDiameter ( &tapdrillDia )

status = WizardHoleFeatureData ->put_TapDrillDiameter ( tapdrillDia )

| Property: | (double) tap drillDia | Tap drill diameter |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This property is relevant only for tapped holes.
