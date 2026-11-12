---
title: "Face::GetFaceId"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__GetFaceId.htm"
---

# Face::GetFaceId

This method is obsolete and has been superseded by [Face2::GetFaceId](sldworksAPI.chm::/Face2/Face2__GetFaceId.htm).

Description

This method gets the face ID on an imported body.

Syntax (OLE Automation)

retval = Face.GetFaceId ()

| Return: | (int) retval | Face ID |
| --- | --- | --- |

Syntax (COM)

status = Face-> GetFaceId ( &retval)

| Output: | (int) retval | Face ID |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This face ID is used to track the specific faces of imported bodies (for example, IGES imports).

The face ID is a persistent ID that is not saved with the document. The face ID can be changed by any third party application. The intent is that you will assign an ID value to a particular face so that you can refer to that face within your application. Each ID value must be unique so it's best to let SolidWorks assign the ID value for you when an imported body or surfaces is created.

If you are interested in storing data with a face, refer to the Attribute object.
