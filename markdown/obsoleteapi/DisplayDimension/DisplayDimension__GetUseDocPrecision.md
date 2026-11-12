---
title: "DisplayDimension::GetUseDocPrecision"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DisplayDimension/DisplayDimension__GetUseDocPrecision.htm"
---

# DisplayDimension::GetUseDocPrecision

This method is obsolete and was not been superceded.

Description

This method determines if this display dimension uses the document default setting for the displayed precision of the dimension and tolerance values.

Syntax (OLE Automation)

retval = DisplayDimension.GetUseDocPrecision ( )

| Return: | (BOOL) retval | TRUE if this display dimension uses the document setting, FALSE if it uses the local setting |
| --- | --- | --- |

Syntax (COM)

status = DisplayDimension->GetUseDocPrecision ( &retval )

| Output: | (VARIANT_BOOL) retval | TRUE if this display dimension uses the document setting, FALSE if it uses the local setting |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The displayed precision of a dimension and its tolerance values can be controlled by a value in one of two places: on the owning document or on the individual display dimension. This method determines whether this display dimension uses the document default setting for precision.

Use [DisplayDimension::SetPrecision](DisplayDimension__SetPrecision.htm) to set this value.
