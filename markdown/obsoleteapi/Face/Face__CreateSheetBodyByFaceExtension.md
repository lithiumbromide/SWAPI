---
title: "Face::CreateSheetBodyByFaceExtension"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__CreateSheetBodyByFaceExtension.htm"
---

# Face::CreateSheetBodyByFaceExtension

This method is obsolete and has been superseded by [Face2::CreateSheetBodyByFaceExtension](sldworksAPI.chm::/Face2/Face2__CreateSheetBodyByFaceExtension.htm).

Description

This method creates a sheet body by extending the face.

Syntax (OLE Automation)

retval = Face.CreateSheetBodyByFaceExtension ( boxLowIn, boxHighIn)

| Input: | (VARIANT) boxLowIn | VARIANT of type SafeArray of 3 doubles (x,y,z) |
| --- | --- | --- |
| Input: | (VARIANT) boxHighIn | VARIANT of type SafeArray of 3 doubles (x,y,z) |
| Return: | (LPDISPATCH) retval | Dispatch pointer to the newly created body |

Syntax (COM)

status = Face->ICreateSheetBodyByFaceExtension ( boxLowIn, boxHighIn, &retval )

| Input: | (double*) boxLowIn | Pointer to an array of 3 doubles (x,y,z) |
| --- | --- | --- |
| Input: | (double*) boxHighIn | Pointer to an array of 3 doubles (x,y,z) |
| Output: | (LPBODY) retval | Pointer to the newly created body |
| Return: | (HRESULT)status | S_OK if successful |
