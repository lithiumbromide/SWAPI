---
title: "Component2::SetXformAndSolve"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component2/Component2__SetXformAndSolve.htm"
---

# Component2::SetXformAndSolve

This method is obsolete and has been superseded by [Component2::SetTransformAndSolve](Component2__SetTransformAndSolve.htm).

Description

This method sets the component transform.

Syntax (OLE Automation)

retval = Component2.SetXformAndSolve ( xformIn)

| Input: | (VARIANT) xformIn | SafeArray of 16 doubles; first 9 are elements of a standard 3x3 rotation matrix, the next 3 define translation, the 13th one is scaling, and the last 3 elements are unused; the transform specified should be in relation to the root component |
| --- | --- | --- |
| Return: | (VARIANT_BOOL) retval | Not used |

Syntax (COM)

status = Component2->ISetXformAndSolve ( xformIn, retval )

| Input: | (double*) xformIn | Array of 16 doubles; first 9 are elements of a standard 3x3 rotation matrix, the next 3 define translation, the 13th one is scaling, and the last 3 elements are unused; the transform specified should be in relation to the root component |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | Not used |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

You must specify the transform in relation to the root component. See Configuration::GetRootComponent.

This method does not support setting the transform of a component within a subassembly. To do this, you must open the subassembly document and get the desired component in the context of the subassembly document. After the component is transformed, the constraints are solved.

Transforming an object with this call can cause SolidWorks to transform several other mated or constrained objects.

After you have changed a component's transform, you can call AssemblyDoc::UpdateBox to avoid clipping in shaded display mode.
