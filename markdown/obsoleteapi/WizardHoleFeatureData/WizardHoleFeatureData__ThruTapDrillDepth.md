---
title: "WizardHoleFeatureData::ThruTapDrillDepth"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/WizardHoleFeatureData/WizardHoleFeatureData__ThruTapDrillDepth.htm"
---

# WizardHoleFeatureData::ThruTapDrillDepth

This property is obsolete and has been superseded by [WizardHoleFeatureData2::ThruTapDrillDepth](sldworksAPI.chm::/WizardHoleFeatureData2/WizardHoleFeatureData2__ThruTapDrillDepth.htm).

Description

This property gets or sets the hole wizard feature through tap drill depth.

Syntax (OLE Automation)

tapdrillDepth = WizardHoleFeatureData.ThruTapDrillDepth (VB Get property)

WizardHoleFeatureData.ThruTapDrillDepth= tapdrillDepth (VB Set property)

tapdrillDepth = WizardHoleFeatureData.GetThruTapDrillDepth ( ) (C++ Get property)

WizardHoleFeatureData.SetThruTapDrillDepth ( tapdrillDepth ) (C++ Set property)

| Property: | (double) tapdrillDepth | Through tap drill depth |
| --- | --- | --- |

Syntax (COM)

status = WizardHoleFeatureData ->get_ThruTapDrillDepth ( &tapdrillDepth )

status = WizardHoleFeatureData ->put_ThruTapDrillDepth ( tapdrillDepth )

| Property: | (double) tapdrillDepth | Through tap drill depth |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This property is relevant only for tapped holes.
