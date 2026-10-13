---
title: "Component::FindAttribute"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__FindAttribute.htm"
---

# Component::FindAttribute

This method is obsolete and has been superseded by [Component2::FindAttribute](sldworksAPI.chm::/Component2/Component2__FindAttribute.htm).

Description

This method finds an attribute on a component.

Syntax (OLE Automation)

retval = Component.FindAttribute ( attributeDef, whichOne )

| Input: | (LPDISPATCH) attributeDef | Pointer to an attribute definition that you are looking for on this component |
| --- | --- | --- |
| Input: | (long) whichOne | Index number of the attribute that you want to return (there can be several attributes on a component) |
| Return: | (LPDISPATCH) retval | Pointer to the attribute object for which you searched the component |

Syntax (COM)

status = Component->IFindAttribute ( attributeDef, whichOne, &retval)

| Input: | (LPATTRIBUTEDEF) attributeDef | Pointer to an attribute definition that you are looking for on this component |
| --- | --- | --- |
| Input: | (long) whichOne | Index number of the attribute that you want to return (there can be several attributes on a component) |
| Output: | (LPATTRIBUTE) retval | Pointer to the attribute object for which you searched the component |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
