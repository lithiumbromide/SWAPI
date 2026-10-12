---
title: "Component2::SetTransformAndSolve"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component2/Component2__SetTransformAndSolve.htm"
---

# Component2::SetTransformAndSolve

This method is obsolete and has been superseded by [Component2::SetTransformAndSolve2](sldworksAPI.chm::/Component2/Component2__SetTransformAndSolve2.htm).

Description

This method sets the transform and solves for the mates.

Syntax (OLE Automation)

retval = Component2.SetTransformAndSolve ( xformIn, &retval )

| Input: | (LPMATHTRANSFORM) xformIn | Transform to set and solve |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the transform was set and solved, FALSE if not |

Syntax (COM)

status = Component2->SetTransformAndSolve ( xformIn, &retval )

| Input: | (LPMATHTRANSFORM) xformIn | Transform to set and solve |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the transform was set and solved, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The transform must be in relation to the root component. See Configuration::GetRootComponent.

This method does not currently support setting the transform of a component within a subassembly. To do this, you must open the subassembly document and get the desired component in the context of the subassembly document. After the component is transformed, the constraints are solved.

Transforming an object with this call can cause SolidWorks to transform several other mated or constrained objects.

After you have changed a component's transform, you can call AssemblyDoc::UpdateBox to avoid clipping in shaded display mode.
