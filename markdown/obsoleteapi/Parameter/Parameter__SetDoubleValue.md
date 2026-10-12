---
title: "Parameter::SetDoubleValue"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Parameter/Parameter__SetDoubleValue.htm"
---

# Parameter::SetDoubleValue

This method is obsolete and has been superseded by [Parameter::SetDoubleValue2](sldworksAPI.chm::/Parameter/Parameter__SetDoubleValue2.htm).

Description

This method sets the value of an attribute parameter. This method works with values of types double and integer and is in system units. Integer values cannot be negative.

Syntax (OLE Automation)

retval = Parameter.SetDoubleValue ( value)

| Input: | (double) value | Value to store in the attribute |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if successful, FALSE if not |

Syntax (COM)

status = Parameter->SetDoubleValue ( value, &retval )

| Input: | (double) value | Value to store in the attribute |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if successful, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If you need to store a negative value, define the attribute parameter as type double. Negative integer values are not allowed.
