---
title: "Body2::AddPropertyExtension"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body2/Body2__AddPropertyExtension.htm"
---

# Body2::AddPropertyExtension

This method is obsolete and has been superseded by [Body2::AddPropertyExtension2](sldworksAPI.chm::/Body2/Body2__AddPropertyExtension2.htm).

Description

This method allows you to store a float, string, or integer value on a body.

Syntax (OLE Automation)

retval = Body2.AddPropertyExtension ( PropertyExtension)

| Input: | (VARIANT) PropertyExtension | Value you wish to store |
| --- | --- | --- |
| Return: | (long) retval | Unique identifier returned to allow you to access the property extension in the future using Body2::GetPropertyExtension |

Syntax (COM)

status = Body2->AddPropertyExtension ( PropertyExtension, &retval )

| Input: | (VARIANT) PropertyExtension | Value you want to store |
| --- | --- | --- |
| Output: | (long) retval | Unique identifier returned to allow you to access the property extension in the future using Body2::GetPropertyExtension |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

To do this, you must first define the VARIANT type (float, string, or integer), give your variable a value, and then call this method to place the value on the body for future reference.

It is recommended that you use the Attribute, AttributeDef, and Parameter classes instead of this method. These three classes are newer and provide more flexibility.
