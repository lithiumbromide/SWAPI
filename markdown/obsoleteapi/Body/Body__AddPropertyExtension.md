---
title: "Body::AddPropertyExtension"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__AddPropertyExtension.htm"
---

# Body::AddPropertyExtension

This property is obsolete and has been superseded by [Body2::AddPropertyExtension2](sldworksAPI.chm::/Body2/Body2__AddPropertyExtension2.htm).

Description

This method stores a float, string, or integer value on a body. To do this, you must first define the VARIANT type (float, string, or integer), give your variable a value, and then call this method to place the value on the body for future reference.

Syntax (OLE Automation)

retval = Body.AddPropertyExtension ( PropertyExtension)

| Input: | (VARIANT) PropertyExtension | Value you want to store on the body |
| --- | --- | --- |
| Return: | (long) retval | Unique identifier returned to allow you to access the Property Extension in the future using Body::GetPropertyExtension |

Syntax (COM)

status = Body->AddPropertyExtension ( PropertyExtension, &retval )

| Input: | (VARIANT) PropertyExtension | Value you want to store on the body |
| --- | --- | --- |
| Output: | (long) retval | Unique identifier returned to allow you to access the Property Extension in the future using Body::GetPropertyExtension |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

You should use the Attribute, AttributeDef, and Parameter objects instead of this method. They are newer and provide more flexibility.
