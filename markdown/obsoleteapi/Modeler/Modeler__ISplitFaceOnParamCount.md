---
title: "Modeler::ISplitFaceOnParamCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Modeler/Modeler__ISplitFaceOnParamCount.htm"
---

# Modeler::ISplitFaceOnParamCount

This method is obsolete and has been superseded by [Modeler::ISplitFaceOnParamCount2](sldworksAPI.chm::/Modeler/Modeler__ISplitFaceOnParamCount2.htm).

Description

This method sets up and counts the number of new faces split on the U or V parameter

Syntax (OLE Automation)

Not available.

NOTE: Use the upper bound on the SafeArray returned from Modeler::SplitFaceOnParam.

Syntax (COM)

status = Modeler->ISplitFaceOnParamCount ( face, UVFlag, parameter, &retval, &newFaceCount,)

| Input: | (LPFACE) face | Pointer to the face |
| --- | --- | --- |
| Input: | (long) UVFlag | The parametric axis; either swSplitFaceOnParamU or swSplitFaceOnParamV |
| Input: | (double) parameter | Position along the parametric axis at which the split will be performed |
| Output: | (VARIANT_BOOL) retval | TRUE if the operation was successful, FALSE otherwise |
| Output: | (long) newFaceCount | Number of new faces |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
