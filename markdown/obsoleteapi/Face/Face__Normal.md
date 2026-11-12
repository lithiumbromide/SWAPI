---
title: "Face::Normal"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__Normal.htm"
---

# Face::Normal

This property is obsolete and has been superseded by [Face2::Normal](sldworksAPI.chm::/Face2/Face2__Normal.htm).

Description

This read-only property gets the unit normal vector for any planar face.

Syntax (OLE Automation)

Normal = Face.Normal (VB Get property)

Face.Normal = Normal (VB Set property)

Normal = Face.GetNormal ( ) (C++ Get property)

Face.SetNormal ( Normal ) (C++ Set property)

| Property: | (VARIANT) Normal | VARIANT of type SafeArray of 3 doubles (i,j,k) |
| --- | --- | --- |

Syntax (COM)

status = Face->get_INormal( Normal)

| Property: | (double*) Normal | Pointer to an array of 3 doubles (i,j,k) |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

If this is not a planar face, then this property returns 0,0,0.
