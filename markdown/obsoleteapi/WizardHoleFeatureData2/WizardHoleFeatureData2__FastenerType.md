---
title: "WizardHoleFeatureData2::FastenerType"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/WizardHoleFeatureData2/WizardHoleFeatureData2__FastenerType.htm"
---

# WizardHoleFeatureData2::FastenerType

This method is obsolete and has been superseded by [WizardHoleFeatureData2::FastenerType2](sldworksAPI.chm::/WizardHoleFeatureData2/WizardHoleFeatureData2__FastenerType2.htm).

Description

This property gets the fastener type for this hole.

Syntax (OLE Automation)

fastenerType = WizardHoleFeatureData2.FastenerType ( ) (VB Get property)

fastenerType = WizardHoleFeatureData2.GetFastenerType ( ) (C++ Get property)

| Return: | (BSTR) fastenerType | Value of the fastener type associated with this hole (see Remarks ) |
| --- | --- | --- |

Syntax (COM)

status = WizardHoleFeatureData2->get_FastenerType ( &fastenerType ) (COM Get property)

| Output: | (BSTR) fastenerType | Value of the fastener type associated with this hole (see Remarks ) |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The fastenerType parameter can be:

| Bottoming Tapped Hole Tapped Hole Tapered Pipe Tap Binding Button Fillister Hex Bolt Hex Bolt (Finished) Hex Bolt (Heavy) Hex Screw Hex Washer Screw Pan Socket Cap Screw Socket Shoulder Screw | Square Truss Flat Head (100) Flat Head (82) Flat Socket (82) Oval All Drill sizes Fractional Drill Sizes H'coil Tap Drills Letter Drill Sizes Number Drill Sizes Pipe Tap Drills Screw Clearances Tap Drills |
| --- | --- |

To set the fastener size for a hole, use WizardHoleFeatureData2::ChangeStandard. To modify this property, use Modeler::CopyWizardHole.
