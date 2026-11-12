---
title: "Body::Operations2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__Operations2.htm"
---

# Body::Operations2

This method is obsolete and has been superseded by [Body2::Operations2](sldworksAPI.chm::/Body2/Body2__Operations2.htm).

Description

This method performs add, cut, and intersect (unite, subtract, interfere) operations between two temporary bodies.

Syntax (OLE Automation)

retval = Body2.Operations2 ( operationType, toolBody, &errorCode )

| Input: | (int) operationType | One of the following operation types: SWBODYADD SWBODYCUT SWBODYINTERSECT |
| --- | --- | --- |
| Input: | (LPDISPATCH) toolBody | Dispatch pointer to the tool body |
| Output: | (long) errorCode | Error indicator as defined in swBodyOperationError_e ; returns swBodyOperationNoError if SolidWorks does not generate an error |
| Return: | (VARIANT) retval | Array of pointers to the resulting bodies |

Syntax (COM)

status = Body2->IOperations2 ( operationType, toolBody, &errorCode, &resultingBodies )

| Input: | (int) operationType | Operation types (see Remarks ) |
| --- | --- | --- |
| Input: | (LPBODY2) toolBody | Pointer to the tool body |
| Output: | (long) errorCode | Error indicator as defined in swBodyOperationError_e ; returns swBodyOperationNoError if SolidWorks does not generate an error |
| Output: | (LPENUMBODIES2) resultingBodies | Enumerated list of the resulting bodies |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If the target and tool bodies are the same in geometry, the result body of this method is NULL and the return value is be S_FALSE.

This method works with two temporary bodies, one is used as the target and one is used as the tool. The output is a list of bodies resulting from the operation.

The two temporary bodies used in this function (the Body and toolBody pointers) will be invalid once the operation is complete. COM applications should Release these two pointers after calling this function. If your application needs to maintain these bodies, then you should make a copy of them using Body2::Copy before passing them to this routine.

To perform a SWBODYINTERSECT between a sheet body and a solid body, the sheet body must be the target body.
