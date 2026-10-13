---
title: "ModelDoc::GetLines"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetLines.htm"
---

# ModelDoc::GetLines

This method is obsolete and has been superseded by [ModelDoc2::GetLines](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetLines.htm).

Description

This method gets all of the lines in the current sketch.

Syntax (OLE Automation)

retval = ModelDoc.GetLines ()

| Return: | (VARIANT) retval | VARIANT of type SafeArray |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->IGetLines ( retval )

| Output: | (double*) retval | Pointer to an array doubles |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The return value is the following array of doubles:

[ LineType, StartPtX, StartPtY, StartPtZ, EndPtX, EndPtY, EndPtZ, ... ]

where this array of 7 values repeats itself for each line in the current sketch. The number of doubles returned will be (number of lines * 7). To determine the number of lines in the current sketch, use [ModelDoc::GetLineCount](ModelDoc__GetLineCount.htm).

See swLineTypes_e for valid line types.
