---
title: "Component::SetXform"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__SetXform.htm"
---

# Component::SetXform

This method is obsolete and has been superseded by [Component2::SetXform](../Component2/Component2__SetXform.htm).

Description

This method sets the component transform.

Syntax (OLE Automation)

retval = Component.SetXform ( xformIn)

| Input: | (VARIANT) xformIn | SafeArray of 16 doubles; the first 9 elements of a standard 3x3 rotation matrix, the next 3 define translation, the next 1 is scaling, and the last 3 elements are unused Specify the transform in relation to the root component |
| --- | --- | --- |
| Return: | (BOOL) retval | Not used |

Syntax (COM)

status = Component->ISetXform ( xformIn, retval )

| Input: | (double*) xformIn | SafeArray of 16 doubles; the first 9 elements of a standard 3x3 rotation matrix, the next 3 define translation, the next 1 is scaling, and the last 3 elements are unused Specify the transform in relation to the root component |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | Not used |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The transform must be specified in relation to the root component (see Configuration::GetRootComponent). This method does not currently support the ability to set the transform of a component within a subassembly. To do this, you need to open the subassembly document and get the desired component in the context of the subassembly document.

To rebuild the model after transforming a component, you can call ModelDoc2::Rebuild with the swUpdateMates argument. This is faster than using AssemblyDoc::EditRebuild to rebuild the geometry for the model.

Be aware SetXform allows you to violate existing mate relationships. If you place a component at an invalid location based on the mate definitions, then the ModelDoc2::Rebuild method recalculates any existing mate relationships and moves your components to the closest valid location.

When you change a component transform, you can use AssemblyDoc::UpdateBox to avoid clipping in shaded display mode.
