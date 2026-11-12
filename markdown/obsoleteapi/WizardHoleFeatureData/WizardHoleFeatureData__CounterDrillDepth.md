---
title: "WizardHoleFeatureData::CounterDrillDepth"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/WizardHoleFeatureData/WizardHoleFeatureData__CounterDrillDepth.htm"
---

# WizardHoleFeatureData::CounterDrillDepth

This property is obsolete and has been superseded by [WizardHoleFeatureData2::CounterDrillDepth](sldworksAPI.chm::/WizardHoleFeatureData2/WizardHoleFeatureData2__CounterDrillDepth.htm).

Description

This property gets or sets the hole wizard feature counter drill depth.

Syntax (OLE Automation)

cdrillDepth = WizardHoleFeatureData.CounterDrillDepth (VB Get property)

WizardHoleFeatureData.CounterDrillDepth = cdrillDepth (VB Set property)

cdrillDepth = WizardHoleFeatureData.GetCounterDrillDepth ( ) (C++ Get property)

WizardHoleFeatureData.SetCounterDrillDepth ( cdrillDepth ) (C++ Set property)

| Property: | (double) cdrillDepth | Counter drill depth of the hole wizard feature |
| --- | --- | --- |

Syntax (COM)

status = WizardHoleFeatureData ->get_CounterDrillDepth ( &cdrillDepth )

status = WizardHoleFeatureData ->put_CounterDrillDepth ( cdrillDepth )

| Property: | (double) cdrillDepth | Counter drill depth of the hole wizard feature |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This property is relevant only for counter-drilled and counter-drilled drilled holes.
