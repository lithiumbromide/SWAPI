---
title: "WizardHoleFeatureData::FastenerType"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/WizardHoleFeatureData/WizardHoleFeatureData__FastenerType.htm"
---

# WizardHoleFeatureData::FastenerType

This property is obsolete and has been superseded by [WizardHoleFeatureData2::FastenerType](../WizardHoleFeatureData2/WizardHoleFeatureData2__FastenerType.htm).

Description

This property gets or sets the fastener type for this hole.

Syntax (OLE Automation)

fastenerType = WizardHoleFeatureData.FastenerType ( ) (VB Get property)

WizardHoleFeatureData.FastenerType = fastenerType (VB Set property)

fastenerType = WizardHoleFeatureData.GetFastenerType ( ) (C++ Get property)

WizardHoleFeatureData.SetFastenerType =( fastenerType ) (C++ Set property)

| Return: | (BSTR) fastenerType | String value of the fastener type associated with this hole |
| --- | --- | --- |

Syntax (COM)

status = WizardHoleFeatureData->get_FastenerType ( &fastenerType ) (COM Get property)

status = WizardHoleFeatureData->put_FastenerType ( fastenerType ) (COM Set property)

| Output: | (BSTR) fastenerType | String value of the fastener type associated with this hole |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You can set the fastenerType parameter to the following types:

| Bottoming Tapped Hole Tapped Hole Tapered Pipe Tap Binding Button Fillister Hex Bolt Hex Bolt (Finished) Hex Bolt (Heavy) Hex Screw Hex Washer Screw Pan Socket Cap Screw Socket Shoulder Screw | Square Truss Flat Head (100) Flat Head (82) Flat Socket (82) Oval All Drill sizes Fractional Drill Sizes H'coil Tap Drills Letter Drill Sizes Number Drill Sizes Pipe Tap Drills Screw Clearances Tap Drills |
| --- | --- |

To modify this property, use Modeler::CopyWizardHole.
