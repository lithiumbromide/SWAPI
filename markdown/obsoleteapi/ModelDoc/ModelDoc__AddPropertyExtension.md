---
title: "ModelDoc::AddPropertyExtension"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__AddPropertyExtension.htm"
---

# ModelDoc::AddPropertyExtension

This method is obsolete and has been superseded by [ModelDoc2::AddPropertyExtension.](sldworksAPI.chm::/ModelDoc2/ModelDoc2__AddPropertyExtension.htm)

Description

This method stores a float, string, or integer value with this document. To do this, you must first define the VARIANT type (float, string, or integer), give your variable a value, and then call this method to place the value on the document for future reference.

Syntax (OLE Automation)

retval = ModelDoc.AddPropertyExtension ( PropertyExtension)

| Input: | (VARIANT) PropertyExtension | Value you wish to store with the SolidWorks document |
| --- | --- | --- |
| Return: | (long) retval | Unique identifier returned that allows access to this property extension in the future |

Syntax (COM)

status = ModelDoc->AddPropertyExtension ( PropertyExtension, &retval )

| Input: | (VARIANT) PropertyExtension | Value you wish to store with the SolidWorks document |
| --- | --- | --- |
| Output: | (long) retval | Unique identifier returned that allows access to this property extension in the future |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

It is recommended that you use the Attribute, AttributeDef, and Parameter classes instead of this method. These three classes provide more flexibility.
