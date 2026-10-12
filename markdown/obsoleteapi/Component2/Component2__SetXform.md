---
title: "Component2::SetXform"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component2/Component2__SetXform.htm"
---

# Component2::SetXform

This method is obsolete and has been superseded by [Component2::Transform](Component2__Transform.htm).

Description

This method sets the component transform.

Syntax (OLE Automation)

retval = Component2.SetXform ( xformIn)

| Input: | (VARIANT) xformIn | SafeArray of 16 doubles; first 9 are elements of a standard 3x3 rotation matrix, the next 3 define translation, the 13th one is scaling, and the last 3 elements are unused; the transform specified should be in relation to the root component |
| --- | --- | --- |
| Return: | (VARIANT_BOOL) retval | Not used |

Syntax (COM)

status = Component2->ISetXform ( xformIn, retval )

| Input: | (double*) xformIn | Array of 16 doubles; first 9 are elements of a standard 3x3 rotation matrix, the next 3 define translation, the 13th one is scaling, and the last 3 elements are unused; the transform specified should be in relation to the root component |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | Not used |
| Return: | (HRESULT) status | S_OK if successful. |

Remarks

You must specify the transform in relation to the root component. See Configuration::GetRootComponent. This method does not support setting the transform of a component within a subassembly. To do this, open the subassembly document and get the desired component in the context of the subassembly document.

You can call ModelDoc2::Rebuild with the swUpdateMates argument to rebuild the model after transforming a component. This is much faster than rebuilding all the geometry for the model using [EditRebuild](../AssemblyDoc/AssemblyDoc__EditRebuild.htm).

This method allows you to violate existing mate relationships. If you place a component at an invalid location based on the mate definitions, then the ModelDoc2::Rebuild method recalculates existing mate relationships and moves your components to the closest valid location.

After you change a component's transform, you can call AssemblyDoc::UpdateBox to avoid clipping in shaded display mode.
