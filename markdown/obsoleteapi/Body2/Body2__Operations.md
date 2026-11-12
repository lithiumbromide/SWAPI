---
title: "Body2::Operations"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body2/Body2__Operations.htm"
---

# Body2::Operations

This method is obsolete and has been superseded by [Body2::Operations2](sldworksAPI.chm::/Body2/Body2__Operations2.htm).

Description

This method performs add, cut, and intersect (unite, subtract, and interfere) operations between two temporary bodies.

Syntax (OLE Automation)

retval = Body2.Operations ( operationType, toolBody, NumMaxSections )

| Input: | (int) operationType | One of the operation types: SWBODYADD SWBODYCUT SWBODYINTERSECT |
| --- | --- | --- |
| Input: | (LPDISPATCH) toolBody | Dispatch pointer for the tool body |
| Input: | (long) NumMaxSections | Maximum number of bodies that can be returned (set by the application) |
| Return: | (VARIANT) retval | SafeArray containing a set of LPDISPATCH pointers for the resulting bodies |

Syntax (COM)

status = Body2->IOperations ( operationType, toolBody, NumMaxSections, resultingBodies, &retval )

| Input: | (int) operationType | One of the operation types: SWBODYADD SWBODYCUT SWBODYINTERSECT |
| --- | --- | --- |
| Input: | (LPBODY2) toolBody | Pointer to the tool body |
| Input: | (long) NumMaxSections | Maximum number of bodies that can be returned (set by the application) |
| Input: | (LPBODY2*) resultingBodies | Array of pointers to the resulting bodies |
| Output: | (long) retval | Number of bodies returned |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method works with two temporary bodies: the target and the tool. The output is the list of bodies resulting from the operation.

Pointers to the two temporary bodies (Body and toolBody) are invalid when the operation is complete. COM applications should release these two pointers after calling this method. If your application needs to maintain these bodies, then use Body2::Copy to make copies before you pass them to this method.

Use the NumMaxSections argument with COM applications to limit the number of bodies returned so that the array does not overflow. For Dispatch applications, set NumMaxSections to -1 and SolidWorks returns all the resulting bodies.

To perform a SWBODYINTERSECT between a sheet body and a solid body, the sheet body must be the target body.
