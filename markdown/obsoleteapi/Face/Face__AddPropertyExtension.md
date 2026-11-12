---
title: "Face::AddPropertyExtension"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__AddPropertyExtension.htm"
---

# Face::AddPropertyExtension

This method is obsolete and has been superseded by [Face2::AddPropertyExtension](sldworksAPI.chm::/Face2/Face2__AddPropertyExtension.htm).

Description

This method allows you to store a float, string, or integer value on a face. To do this, you must first define the VARIANT type (float, string, or integer), give your variable a value, and then call this method to place the value on the face for future reference.

Syntax (OLE Automation)

retval = Face.AddPropertyExtension ( PropertyExtension)

| Input: | (VARIANT) PropertyExtension | Value you want to store on the face |
| --- | --- | --- |
| Return: | (long) retval | Unique identifier returned to allow you to access the property extension |

Syntax (COM)

status = Face->AddPropertyExtension ( PropertyExtension, &retval )

| Input: | (VARIANT) PropertyExtension | Value you want to store on the face |
| --- | --- | --- |
| Output: | (long*) retval | Unique identifier returned to allow you to access the property extension |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Use the Attribute, AttributeDef, and Parameter classes instead of this method. These classes are newer and provide more flexibility.

Please note that this method is currently unsupported for faces obtained from reference surface bodies.
