---
title: "Body2::SetXform"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body2/Body2__ISetXform.htm"
---

# Body2::SetXform

This method is obsolete and has been superseded by [Body2::ApplyTranform](sldworksAPI.chm::/Body2/Body2__ApplyTransform.htm).

Description

This method is intended for use with the Body2::GetIntersectionEdges method.

Syntax (OLE Automation)

retval = Body2.SetXform ( xformIn )

| Input: | (VARIANT) xformIn | SafeArray of 16 doubles representing the transform |
| --- | --- | --- |
| Return: | (VARIANT_BOOL) retval | TRUE if the Xform is set successfully, FALSE if not |

Syntax (COM)

status = Body2->ISetXform ( xformIn, &retval )

| Input: | (double*) xformIn | Pointer to an array of 16 doubles representing a transform |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the Xform is set successfully, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If there are two bodies in an assembly, then Body2::GetIntersectionEdges edges generates a list of the intersection edges between the two bodies. To do this, the second body must be transformed in its coordinate space so that it is positioned the same with respect to the first body as it is in assembly space.

To align the two bodies before call Body2::GetIntersectionEdges, calculate the transformation from the first body to the second body and set this as the transform for the second body using Body2::SetXform.

The xformIn argument contains a 16 element array defining the transform. The first nine are elements of 3x3 matrix, the next three define translation and the next one is scaling. The last three elements are unused. Specify the transform in relation to the model.

Body2::SetXform is intended for use with temporary body objects. If you call this method on the actual part or component body object, you might corrupt your file. You can make a copy of a Body object using Body2::Copy.
