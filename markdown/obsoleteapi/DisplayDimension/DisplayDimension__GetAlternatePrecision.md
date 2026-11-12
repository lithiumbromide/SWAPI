---
title: "DisplayDimension::GetAlternatePrecision"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DisplayDimension/DisplayDimension__GetAlternatePrecision.htm"
---

# DisplayDimension::GetAlternatePrecision

This method is obsolete and has been superseded by [DisplayDimension::GetAlternatePrecision2](sldworksAPI.chm::/DisplayDimension/DisplayDimension__GetAlternatePrecision2.htm).

Description

This method gets the precision displayed in the value of this dual dimension. This is the precision used in the alternate units of the dimension value.

Syntax (OLE Automation)

retval = DisplayDimension.GetAlternatePrecision ( )

| Return: | (long) retval | Number of decimal places displayed (see below) |
| --- | --- | --- |

Syntax (COM)

status = DisplayDimension->GetAlternatePrecision ( &retval )

| Output: | (long) retval | Number of decimal places displayed (see below) |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You can use [DisplayDimension::GetPrimaryPrecision](DisplayDimension__GetPrimaryPrecision.htm) to determine the primary dimension precision.

The displayed precision of a dimension and its tolerance values are controlled by a value that SolidWorks stores in one of two places; on the owning document or on the individual display dimension. Use [DisplayDimension::GetUseDocPrecision](DisplayDimension__GetUseDocPrecision.htm) to determine whether this display dimension is using the default document values.

This method gets the alternate precision value stored on this display dimension. If this display dimension is set to use the document settings for display dimension precision, then the value returned by this method might be different than what is currently displayed by SolidWorks.

Use [DisplayDimension::SetPrecision](DisplayDimension__SetPrecision.htm) to set precision values on this display dimension.
