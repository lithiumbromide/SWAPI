---
title: "Component::SetXformAndSolve"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__SetXformAndSolve.htm"
---

# Component::SetXformAndSolve

This method is obsolete and has been superseded by [Component2::SetXformAndSolve](../Component2/Component2__SetXformAndSolve.htm).

Description

This method sets the component transform.

Syntax (OLE Automation)

retval = Component.SetXformAndSolve ( xformIn)

| Input: | (VARIANT) xformIn | SafeArray of 16 doubles; the first 9 elements of a standard 3x3 rotation matrix, the next 3 define translation, the next 1 is scaling, and the last 3 elements are unused |
| --- | --- | --- |
| Return: | (BOOL) retval | Not used |

Syntax (COM)

status = Component->ISetXformAndSolve ( xformIn, retval )

| Input: | (double*) xformIn | Array of 16 doubles; the first 9 elements of a standard 3x3 rotation matrix, the next 3 define translation, the next 1 is scaling, and the last 3 elements are unused |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | Not used |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The transform must be specified in relation to the root component (see Configuration::GetRootComponent). This method does not currently support the ability to set the transform of a component within a subassembly. To do this, you must open the subassembly document and get the desired component in the context of the subassembly document. After SolidWorks transforms the component, it solves the constraints.

Transforming one object with this call can cause the transforms of several other mated or constrained objects to change as well.

After you have changed a component's transform, you can avoid clipping in shaded display mode by calling AssemblyDoc::UpdateBox.
