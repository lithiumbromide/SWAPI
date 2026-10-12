---
title: "ModelDoc::GetAngularUnits"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetAngularUnits.htm"
---

# ModelDoc::GetAngularUnits

This method is obsolete and has been superseded by [ModelDoc2::GetAngularUnits](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetAngularUnits.htm).

Description

This method gets the current angular unit settings.

Syntax (OLE Automation)

retval = ModelDoc.GetAngularUnits ()

| Return: | (VARIANT) retval | VARIANT of type SafeArray of 5 shorts |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->IGetAngularUnits ( &retval )

| Output: | (short) retval | Pointer to an array of 5 shorts |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The format of the returned data is an array of five shorts:

[ AngleUnit, FractionBase, FractionValue, SignificantDigits, RoundToFraction ]

where

AngleUnit = The current angular units. The most up-to-date unit types can be found in the swAngleUnit_e enumeration

FractionBase = Not Currently Supported. The return value in this field should not be used.

FractionValue = Not Currently Supported. The return value in this field should not be used.

SignificantDigits = The significant digits if using Decimal units.

RoundToFraction = Not Currently Supported. The return value in this field should not be used.
