---
title: "ModelDoc::GetPropertyExtension"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetPropertyExtension.htm"
---

# ModelDoc::GetPropertyExtension

This method is obsolete and has been superseded by [ModelDoc2::GetPropertyExtension](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetPropertyExtension.htm).

Description

This method retrieves a float, string, or integer value from a document. The VARIANT type returned is based on the how the data was placed on the part. See ModelDoc::AddPropertyExtension for details.

Syntax (OLE Automation)

retval = ModelDoc.GetPropertyExtension ( Id)

| Input: | (long) Id | Unique identifier for the desired property extension |
| --- | --- | --- |
| Return: | (VARIANT) retval | Value that was stored using ModelDoc::AddPropertyExtension |

Syntax (COM)

status = ModelDoc->GetPropertyExtension ( Id, &retval )

| Input: | (long) Id | Unique identifier for the desired property extension |
| --- | --- | --- |
| Output: | (VARIANT) retval | Value that was stored using ModelDoc::AddPropertyExtension |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

It is recommended that you use the Attribute, AttributeDef, and Parameter classes instead of this method. These three classes provide more flexibility.
