---
title: "Modeler::ICreateBodyFromFaces"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Modeler/Modeler__ICreateBodyFromFaces.htm"
---

# Modeler::ICreateBodyFromFaces

This method is obsolete and has been superceded by [Modeler::ICreateBodyFromFaces3](sldworksAPI.chm::/Modeler/MODELER__ICREATEBODYFROMFACES3.HTM).

Description

This method creates a temporary body from a list of faces.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = Modeler->ICreateBodyFromFaces ( numFaces, faceList, doLocalCheck, localCheckResult, &retval )

| Input: | (long) numFaces | Number of Face objects in the faceList array |
| --- | --- | --- |
| Input: | (LPFACE* )faceList | Array of Face objects to be sewn |
| Input: | (VARIANT_BOOL) doLocalCheck | TRUE if you want to perform local checking on the resulting body, FALSE if not |
| Output: | (VARIANT_BOOL) localCheckResult | If doLocalCheck is TRUE and body is okay, then TRUE, otherwise FALSE |
| Output: | (LPBODY) retval | Pointer to a newly created Body object or NULL if the operation fails |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
