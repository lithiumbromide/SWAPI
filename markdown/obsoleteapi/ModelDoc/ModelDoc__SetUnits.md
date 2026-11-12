---
title: "ModelDoc::SetUnits"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetUnits.htm"
---

# ModelDoc::SetUnits

This method is obsolete and has been superseded by [ModelDoc2::SetUnits](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetUnits.htm).

Description

This method sets the units used by the user for the model. This setting does not affect the units used by the SolidWorks API, which consistently requires and returns meters unless otherwise noted.

Syntax (OLE Automation)

void ModelDoc.SetUnits ( uType, fractBase, fractDenom, sigDigits, roundToFraction)

| Input: | (short) uType | The desired model units as defined in swLengthUnit_e |
| --- | --- | --- |
| Input: | (short) fractBase | Decimal vs. fraction as defined in swFractionDisplay_e |
| Input: | (short) fractDenom | Used only for fractional inches and is the denominator for the smallest fraction to be used; for example, 64 for 1/64 |
| Input: | (short) sigDigits | Significant digits if using decimal units |
| Input: | (BOOL) roundToFraction | Flag denoting whether or not to round to the fraction; for example, if 4 was the denominator value given in fractDenom and the actual value is 0.27, it would be rounded to 0.25 |

Syntax (COM)

status = ModelDoc->SetUnits ( uType, fractBase, fractDenom, sigDigits, roundToFraction)

| Input: | (short) uType | The desired model units as defined in swLengthUnit_e |
| --- | --- | --- |
| Input: | (short) fractBase | Decimal vs. fraction as defined in swFractionDisplay_e |
| Input: | (short) fractDenom | Used only for fractional inches and is the denominator for the smallest fraction to be used; for example, 64 for 1/64 |
| Input: | (short) sigDigits | Significant digits if using decimal units |
| Input: | (VARIANT_BOOL) roundToFraction | Fag denoting whether or not to round to the fraction; for example, if 4 was the denominator value given in fractDenom and the actual value is 0.27, it would be rounded to 0.25 |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Fractional units are only valid if uType is swINCHES or swFEETINCHES.
