---
title: "WizardHoleFeatureData::Standard"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/WizardHoleFeatureData/WizardHoleFeatureData__Standard.htm"
---

# WizardHoleFeatureData::Standard

This property is obsolete and has been superseded by [WizardHoleFeatureData2::Standard](../WizardHoleFeatureData2/WizardHoleFeatureData2__Standard.htm).

Description

This property gets or sets the design standard for this hole.

Syntax (OLE Automation)

standard = WizardHoleFeatureData.Standard ( ) (VB Get property)

WizardHoleFeatureData.Standard = standard (VB Set property)

standard = WizardHoleFeatureData.GetStandard ( ) (C++ Get property)

WizardHoleFeatureData.SetStandard =( standard ) (C++ Set property)

| Return: | (BSTR) standard | Value of the design standard associated with this hole |
| --- | --- | --- |

Syntax (COM)

status = WizardHoleFeatureData->get_Standard ( &standard ) (COM Get property)

status = WizardHoleFeatureData->put_Standard ( standard ) (COM Set property)

| Output: | (BSTR) standard | Value of the design standard associated with this hole |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The following table contains the list of the strings that can be used for this property:

- "Ansi Inch"
- "Ansi Metric"
- "BSI"
- "DIN"
- "ISO"
