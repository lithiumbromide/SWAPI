---
title: "Face::GetShellType"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__GetShellType.htm"
---

# Face::GetShellType

This method is obsolete and has been superseded by [Face2::GetShellType](sldworksAPI.chm::/Face2/Face2__GetShellType.htm).

Description

This method gets the shell type (open, internal, external) for this face.

Syntax (OLE Automation)

retval = Face.GetShellType ( )

| Return: | (int) retval | Shell type: 0 = An open shell. For example, a face belonging to a sheet body or reference surface. 1 = An internal shell. For example, a face which belongs to a cavity. Face helps define an internal volume. 2 = An external shell. For example, a typical face on a solid body (ie: helps "hold in" the body mass). This would include all external faces including faces belonging to bosses, pockets, holes, etc. |
| --- | --- | --- |

Syntax (COM)

status = Face->GetShellType ( &retval )

| Output: | (int) retval | Shell type: 0 = An open shell. For example, a face belonging to a sheet body or reference surface. 1 = An internal shell. For example, a face which belongs to a cavity. Face helps define an internal volume. 2 = An external shell. For example, a typical face on a solid body (ie: helps "hold in" the body mass). This would include all external faces including faces belonging to bosses, pockets, holes, etc. |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful; S_FALSE otherwise |

Remarks
