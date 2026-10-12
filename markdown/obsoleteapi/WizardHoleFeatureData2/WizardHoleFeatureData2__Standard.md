---
title: "WizardHoleFeatureData2::Standard"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/WizardHoleFeatureData2/WizardHoleFeatureData2__Standard.htm"
---

# WizardHoleFeatureData2::Standard

This property is obsolete and has been superseded by [WizardHoleFeatureData2::Standard2](sldworksAPI.chm::/WizardHoleFeatureData2/WizardHoleFeatureData2__Standard2.htm).

Description

This property gets the design standard for this hole.

Syntax (OLE Automation)

standard = WizardHoleFeatureData2.Standard ( ) (VB Get property)

standard = WizardHoleFeatureData2.GetStandard ( ) (C++ Get property)

| Return: | (BSTR) standard | Value of the design standard associated with this hole as defined in swWzdHoleStandards_e |
| --- | --- | --- |

Syntax (COM)

status = WizardHoleFeatureData2->get_Standard ( &standard ) (COM Get property)

| Output: | (BSTR) standard | Value of the design standard associated with this hole as defined in swWzdHoleStandards_e |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

To set the fastener size for a hole, use WizardHoleFeatureData2::ChangeStandard. To modify this property, use Modeler::CopyWizardHole.
