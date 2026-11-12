---
title: "Body2::GetPropertyExtension"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body2/Body2__GetPropertyExtension.htm"
---

# Body2::GetPropertyExtension

This method is obsolete and has been superseded by [Body2::GetPropertyExtension2](sldworksAPI.chm::/Body2/Body2__GetPropertyExtension2.htm).

Description

This gets a float, string, or integer value from a body.

Syntax (OLE Automation)

retval = Body2.GetPropertyExtension ( Id)

| Input: | (long) Id | Unique identifier for the desired property extension |
| --- | --- | --- |
| Return: | (VARIANT) retval | Value stored using Body2::AddPropertyExtension |

Syntax (COM)

status = Body2->GetPropertyExtension ( Id, retval )

| Input: | (long) Id | Unique identifier for the desired property extension |
| --- | --- | --- |
| Output: | (VARIANT) retval | Value stored using Body2::AddPropertyExtension |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The VARIANT returned is based on the how the data was placed on the body.

Use the Attribute, AttributeDef, and Parameter classes instead of this method. They provide more flexibility.
