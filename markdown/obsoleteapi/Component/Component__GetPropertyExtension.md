---
title: "Component::GetPropertyExtension"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__GetPropertyExtension.htm"
---

# Component::GetPropertyExtension

This property is obsolete and has been superseded by [Component2::GetPropertyExtension](sldworksAPI.chm::/Component2/Component2__GetPropertyExtension.htm).

Description

This method retrieves a float, string, or integer value from a component.

Syntax (OLE Automation)

retval = Component.GetPropertyExtension ( Id)

| Input: | (long) Id | Unique identifier of the property extension |
| --- | --- | --- |
| Return: | (VARIANT) retval | Value that was stored using Component::AddPropertyExtension |

Syntax (COM)

status = Component->GetPropertyExtension ( Id, &retval )

| Input: | (long) Id | Unique identifier of the property extension |
| --- | --- | --- |
| Output: | (VARIANT) retval | Value that was stored using Component::AddPropertyExtension |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The VARIANT type returned by this method is based on the how the data was placed on the component. See Component::AddPropertyExtension.

Use Attribute, AttributeDef, and Parameter instead of this method. These classes are newer and provide more flexibility.
