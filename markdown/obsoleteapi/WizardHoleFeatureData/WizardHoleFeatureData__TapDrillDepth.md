---
title: "WizardHoleFeatureData::TapDrillDepth"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/WizardHoleFeatureData/WizardHoleFeatureData__TapDrillDepth.htm"
---

# WizardHoleFeatureData::TapDrillDepth

This property is obsolete and has been superseded by [WizardHoleFeatureData2::TapDrillDepth](sldworksAPI.chm::/WizardHoleFeatureData2/WizardHoleFeatureData2__TapDrillDepth.htm).

Description

This property gets or sets the hole wizard feature tap drill depth.

Syntax (OLE Automation)

tapdrillDepth = WizardHoleFeatureData.TapDrillDepth (VB Get property)

WizardHoleFeatureData.TapDrillDepth = tapdrillDepth (VB Set property)

tapdrillDepth = WizardHoleFeatureData.GetTapDrillDepth ( ) (C++ Get property)

WizardHoleFeatureData.SetTapDrillDepth ( tapdrillDepth ) (C++ Set property)

| Property: | (double) tapdrillDepth | Tap drill depth |
| --- | --- | --- |

Syntax (COM)

status = WizardHoleFeatureData ->get_TapDrillDepth ( &tapdrillDepth )

status = WizardHoleFeatureData ->put_TapDrillDepth ( tapdrillDepth )

| Property: | (double) tapdrillDepth | Tap drill depth |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This property is relevant only for tapped holes.
