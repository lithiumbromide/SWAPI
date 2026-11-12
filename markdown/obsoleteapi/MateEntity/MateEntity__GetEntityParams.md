---
title: "MateEntity::GetEntityParams"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/MateEntity/MateEntity__GetEntityParams.htm"
---

# MateEntity::GetEntityParams

This method is obsolete and has been superseded by [MateEntity2::EntityParams](sldworksAPI.chm::/MateEntity2/MateEntity2__EntityParams.htm).

Description

This method returns the parameters of this particular mate entity. Use MateEntity::GetEntityType to know what parameters to expect.

Syntax (OLE Automation)

retval = MateEntity.GetEntityParams ()

| Return: | (VARIANT) retval | VARIANT of type SafeArray; this is an array of doubles representing the mate entity parameters |
| --- | --- | --- |

Syntax (COM)

status = MateEntity->IGetEntityParams ( retval )

| Output: | (double*) retval | Pointer to an array of doubles |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The return value is the following array of doubles:

[ pointX, pointY, pointZ, vectorI, vectorJ, vectorK, radius1, radius2 ]

where

- pointX is the X location of this mate entity in the assembly model space
- pointY is the Y location of this mate entity in the assembly model space
- pointZ is the Z location of this mate entity in the assembly model space
- vectorI is the i component of the assembly mate vector
- vectorJ is the j component of the assembly mate vector
- vectorK is the k component of the assembly mate vector
- radius1 is the value for the first radius
- radius2 is the value for the second radius

To define the mate entity, the following information is returned based upon the mate type. All coordinate information is given in terms of the assembly coordinate system where the mate resides.

| Mate Type | Returned |
| --- | --- |
| swMatePoint | pointX, pointY, pointZ |
| swMateLine | pointX, pointY, pointZ, vectorI, vectorJ, vectorK where the point is a point on the line and the vector represents the line direction. |
| swMatePlane | pointX, pointY, pointZ, vectorI, vectorJ, vectorK where the point is a point on the plane and the vector represents the plane normal. |
| swMateCylinder | pointX, pointY, pointZ, vectorI, vectorJ, vectorK, radius1 where the point is a point on the cylinder axis and the vector represents the cylinder axis. |
| swMateCone | pointX, pointY, pointZ, vectorI, vectorJ, vectorK, radius1, radius2 where the point is a point on the cone axis and the vector represents the cone axis. |

To get to the MateEntity interface, use Mate::GetMateEntities.
