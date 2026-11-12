---
title: "Body::GetIgesErrorCode"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__GetIgesErrorCode.htm"
---

# Body::GetIgesErrorCode

This method is obsolete and has been superseded by [Body2::GetIgesErrorCode](sldworksAPI.chm::/Body2/Body2__GetIgesErrorCode.htm).

Description

This method gets the current IGES error code.

Syntax (OLE Automation)

retval = Body.GetIgesErrorCode ( index)

| Input: | (long) index | Indexed position of the error within the current list of errors |
| --- | --- | --- |
| Return: | (long) retval | IGES error code |

Syntax (COM)

status = Body->GetIgesErrorCode ( index, &retval )

| Input: | (long) index | Indexed position of the error within the current list of errors |
| --- | --- | --- |
| Output: | (long) retval | IGES error code |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This method is intended for use during IGES processing only.
