---
title: "Component::AddPropertyExtension"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__AddPropertyExtension.htm"
---

# Component::AddPropertyExtension

This method is obsolete and has been superseded by [Component2::AddPropertyExtension](sldworksAPI.chm::/Component2/Component2__AddPropertyExtension.htm).

Description

This method allows you to store a float, string, or integer value on this Component object. You must first define the VARIANT type (float, string, or integer), give your variable a value, and then call this method to place the value on the component for future reference.

Syntax (OLE Automation)

retval = Component.AddPropertyExtension ( PropertyExtension)

| Input: | (VARIANT) PropertyExtension | Value you want to store on the component |
| --- | --- | --- |
| Return: | (long) retval | Unique identifier returned to allow access to the property extension in the future; SolidWorks returns -1 if it cannot set the property |

Syntax (COM)

status = Component->AddPropertyExtension ( PropertyExtension, &retval )

| Input: | (VARIANT) PropertyExtension | Value you want to store on the component |
| --- | --- | --- |
| Output: | (long) retval | Unique identifier returned to allow access to the property extension in the future; SolidWorks returns -1 if it cannot set the property |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use the Attribute, AttributeDef, and Parameter classes instead of this method. These classes are provide more flexibility.
