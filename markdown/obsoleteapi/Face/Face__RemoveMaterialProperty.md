---
title: "Face::RemoveMaterialProperty"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__RemoveMaterialProperty.htm"
---

# Face::RemoveMaterialProperty

This method is obsolete and has been superseded by [Face2::RemoveMaterialProperty](../Face2/Face2__RemoveMaterialProperty.htm).

Description

This method removes the material property values from this face.

Syntax (OLE Automation)

retval = Face.RemoveMaterialProperty ( )

| Return: | (BOOL) retval | TRUE if the material property was removed, FALSE if not |
| --- | --- | --- |

Syntax (COM)

status = Face->RemoveMaterialProperty ( &retval )

| Output: | (VARIANT_BOOL) retval | TRUE if the material property was removed, FALSE if not |
| --- | --- | --- |
| Return: | (HRESULT) retval | S_OK if successful |

Remarks

This method is intended to be used on faces with changed material properties (for example, color).
