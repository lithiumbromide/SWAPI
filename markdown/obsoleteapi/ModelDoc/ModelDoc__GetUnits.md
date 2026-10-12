---
title: "ModelDoc::GetUnits"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetUnits.htm"
---

# ModelDoc::GetUnits

This method is obsolete and has been superseded by [ModelDoc2::GetUnits](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetUnits.htm).

Description

This method gets the current unit settings, along with the fraction base, the fraction value, and the significant digits being used. You can also use ModelDoc::LengthUnit, which provides access to the LengthUnit parameter.

Syntax (OLE Automation)

retval = ModelDoc.GetUnits ()

| Return: | (VARIANT) retval | VARIANT of type SafeArray of 5 shorts |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->IGetUnits ( &retval )

| Output: | (short) retval | Pointer to an array of 5 shorts |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The format of the returned data is an array of shorts:

[ LengthUnit, FractionBase, FractionValue, SignificantDigits, RoundToFraction ]

where:

LengthUnit = the current model units as defined in swLengthUnit_e.

FractionBase = decimal vs. fraction. This return is one of the swFractionDisplay_e enumerations. Fractional units are only valid if the user has specified swINCHES or swFEETINCHES.

FractionValue = the denominator value if using fractional units.

SignificantDigits = the significant digits if using decimal units.

RoundToFraction = a flag denoting whether or not to round the fraction. For example, if 4 was the denominator value and the actual value was .27, then it would be rounded to .25.
