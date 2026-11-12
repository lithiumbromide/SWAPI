---
title: "Face::GetPropertyExtension"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__GetPropertyExtension.htm"
---

# Face::GetPropertyExtension

This method is obsolete and has been superseded by [Face2::GetPropertyExtension](sldworksAPI.chm::/Face2/Face2__GetPropertyExtension.htm).

Description

This method gets a float, string, or integer value from a face.

Syntax (OLE Automation)

retval = Face.GetPropertyExtension ( Id )

| Input: | (long) Id | Unique identifier for the desired property extension |
| --- | --- | --- |
| Return: | (VARIANT) retval | Value stored using Face::AddPropertyExtension |

Syntax (COM)

status = Face->GetPropertyExtension ( Id, &retval )

| Input: | (long) Id | Unique identifier for the desired property extension |
| --- | --- | --- |
| Output: | (VARIANT) retval | Value stored using Face::AddPropertyExtension |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use the Attribute, AttributeDef, and Parameter classes instead of this method. These classes are newer and provide more flexibility.
