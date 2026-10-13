---
title: "Face2::RemoveMaterialProperty"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face2/Face2__RemoveMaterialProperty.htm"
---

# Face2::RemoveMaterialProperty

This method is obsolete and is superseded by [Face2::RemoveMaterialProperty2](sldworksAPI.chm::/Face2/Face2__RemoveMaterialProperty2.htm).

Description

This method removes the material property values from this face.

Syntax (OLE Automation)

retval = Face2.RemoveMaterialProperty ( )

| Return: | (BOOL) retval | TRUE if the material property has been removed, FALSE if not |
| --- | --- | --- |

Syntax (COM)

status = Face2->RemoveMaterialProperty ( &retval )

| Output: | (VARIANT_BOOL) retval | TRUE if the material property has been removed, FALSE if not |
| --- | --- | --- |
| Return: | (HRESULT) retval | S_OK if successful |

Remarks

This method is intended to be used on faces with changed material properties (for example, color).
