---
title: "Body::SetXform"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__SetXform.htm"
---

# Body::SetXform

This method is obsolete and has been superseded by [Body2::SetXform](../Body2/Body2__ISetXform.htm).

Description

Use this method with the Body::GetIntersectionEdges method.

Syntax (OLE Automation)

retval = Body.SetXform ( xformIn )

| Input: | (VARIANT) xformIn | SafeArray of 16 doubles representing the transform (see Remarks ) |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if the transform is set successfully, FALSE if not |

Syntax (COM)

status = Body->ISetXform ( xformIn, &retval )

| Input: | (double*) xformIn | Pointer to an array of 16 doubles representing a transform (see Remarks ) |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the transform is set successfully, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If there are two bodies in an assembly, then Body::GetIntersectionEdges generates a list of the intersection edges between the two bodies. To do this, the second body must be transformed in its coordinate space so that it is in the same place with respect to the first body as it is in assembly space.

To align the two bodies before calling Body::GetIntersectionEdges, calculate the transformation from the first body to the second in the assembly and set this as the transform for the second body using this method.

The xformIn argument contains a 16 element array defining the transform. The first 9 are elements of 3x3 matrix, the next 3 define translation, and the next 1 is scaling. The last 3 elements are unused. Specify the transform in relation to the model.

Use this method with temporary body objects. If you call this method on the actual part or component body object, you might corrupt your file. You can use Body::Copy to make a copy of a body object.
