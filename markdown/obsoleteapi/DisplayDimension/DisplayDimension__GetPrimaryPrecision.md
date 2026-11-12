---
title: "DisplayDimension::GetPrimaryPrecision"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DisplayDimension/DisplayDimension__GetPrimaryPrecision.htm"
---

# DisplayDimension::GetPrimaryPrecision

This method is obsolete and has been superseded by [DisplayDimension::GetPrimaryPrecision2](sldworksAPI.chm::/DisplayDimension/DisplayDimension__GetPrimaryPrecision2.htm).

Description

This method gets the precision displayed by this display dimension.

Syntax (OLE Automation)

retval = DisplayDimension.GetPrimaryPrecision ( )

| Return: | (long) retval | Number of decimal places to be displayed (see below) |
| --- | --- | --- |

Syntax (COM)

status = DisplayDimension->GetPrimaryPrecision ( &retval )

| Output: | (long) retval | Number of decimal places to be displayed (see below) |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method returns the precision used in the primary units of the dimension value.

The display precision of a dimension and its tolerance values are controlled by a value that SolidWorks stores in one of two places: on the owning document or on the individual display dimension. Use [DisplayDimension::GetUseDocPrecision](DisplayDimension__GetUseDocPrecision.htm) to determine whether this display dimension is using the document default values.

If this display dimension is set to use the document settings for display dimension precision, then this method might return a value that different from what is displayed. You can use [DisplayDimension::GetUseDocPrecision](DisplayDimension__GetUseDocPrecision.htm) to determine if this display dimension uses the document default values.

Use [DisplayDimension::SetPrecision](DisplayDimension__SetPrecision.htm) to set precision values on this display dimension.
