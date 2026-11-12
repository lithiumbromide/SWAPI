---
title: "Body::GetPropertyExtension"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__GetPropertyExtension.htm"
---

# Body::GetPropertyExtension

This property is obsolete and has been superseded by [Body2::GetPropertyExtension](../Body2/Body2__GetPropertyExtension.htm).

Description

This method gets a float, string, or integer value from a body. The VARIANT type returned is based on the how the data was placed on the body. See Body::AddPropertyExtension for details.

Syntax (OLE Automation)

retval = Body.GetPropertyExtension ( Id)

| Input: | (long) Id | Unique identifier for the desired property extension |
| --- | --- | --- |
| Return: | (VARIANT) retval | Value which was stored using Body::AddPropertyExtension |

Syntax (COM)

status = Body->GetPropertyExtension ( Id, retval )

| Input: | (long) Id | Unique identifier for the desired property extension |
| --- | --- | --- |
| Output: | (VARIANT) retval | Value which was stored using Body::AddPropertyExtension |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Use the Attribute, AttributeDef, and Parameter objects instead of this method. They provide more flexibility.
