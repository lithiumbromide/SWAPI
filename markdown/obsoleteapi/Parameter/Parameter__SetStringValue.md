---
title: "Parameter::SetStringValue"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Parameter/Parameter__SetStringValue.htm"
---

# Parameter::SetStringValue

This method is obsolete and has been superseded by [Parameter::SetStringValue2](sldworksAPI.chm::/Parameter/Parameter__SetStringValue2.htm).

Description

This method adds string data to a parameter.

Syntax (OLE Automation)

retval = Parameter.SetStringValue ( StringValue)

| Input: | (BSTR) StringValue | Value for the parameter |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if successfully added, FALSE if not |

Syntax (COM)

status = Parameter->SetStringValue ( StringValue, &retval )

| Input: | (BSTR) StringValue | Value for the parameter |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if successfully added, if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
