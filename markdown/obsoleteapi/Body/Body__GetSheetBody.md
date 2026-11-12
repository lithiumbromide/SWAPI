---
title: "Body::GetSheetBody"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__GetSheetBody.htm"
---

# Body::GetSheetBody

This method is obsolete and has been superseded by [Body2::GetSheetBody](sldworksAPI.chm::/Body2/Body2__GetSheetBody.htm).

Description

This method gets a sheet body in the body.

Syntax (OLE Automation)

retval = Body.GetSheetBody ( index )

| Input: | (int) index | Index of sheet body |
| --- | --- | --- |
| Return: | (LPDISPATCH) retval | Pointer to the sheet body corresponding to the index |

Syntax (COM)

status = Body->IGetSheetBody ( index, &retval )

| Input: | (int) index | Index of sheet body |
| --- | --- | --- |
| Output: | (LPBODY)retval | Pointer to the sheet body corresponding to the index |
| Return: | (HRESULT)status | S_OK if successful |
