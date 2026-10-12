---
title: "WizardHoleFeatureData::ThruTapDrillDiameter"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/WizardHoleFeatureData/WizardHoleFeatureData__ThruTapDrillDiameter.htm"
---

# WizardHoleFeatureData::ThruTapDrillDiameter

This property is obsolete and has been superseded by [WizardHoleFeatureData2::ThruTapDrillDiameter](sldworksAPI.chm::/WizardHoleFeatureData2/WizardHoleFeatureData2__ThruTapDrillDiameter.htm).

Description

This property gets or sets the hole wizard feature through tap drill diameter.

Syntax (OLE Automation)

tapdrillDia = WizardHoleFeatureData.ThruTapDrillDiameter (VB Get property)

WizardHoleFeatureData.ThruTapDrillDiameter = tapdrillDia (VB Set property)

tapdrillDia = WizardHoleFeatureData.GetThruTapDrillDiameter ( ) (C++ Get property)

WizardHoleFeatureData.SetThruTapDrillDiameter ( tapdrillDia ) (C++ Set property)

| Property: | (double) tap drillDia | Through tap drill diameter |
| --- | --- | --- |

Syntax (COM)

status = WizardHoleFeatureData ->get_ThruTapDrillDiameter ( &tapdrillDia )

status = WizardHoleFeatureData ->put_ThruTapDrillDiameter ( tapdrillDia )

| Property: | (double) tap drillDia | Through tap drill diameter |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This property is relevant only for tapped holes.
