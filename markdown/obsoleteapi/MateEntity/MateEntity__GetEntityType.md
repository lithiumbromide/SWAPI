---
title: "MateEntity::GetEntityType"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/MateEntity/MateEntity__GetEntityType.htm"
---

# MateEntity::GetEntityType

This method is obsolete and has been superseded by [MateEntity2::ReferenceType2](sldworksAPI.chm::/MateEntity2/MateEntity2__ReferenceType2.htm).

Description

This method returns the entity type for this mate entity.

Syntax (OLE Automation)

retval = MateEntity.GetEntityType ()

| Return: | (long) retval | Type of entity as defined in swMateEntityTypes_e |
| --- | --- | --- |

Syntax (COM)

status = MateEntity->GetEntityType ( &retval )

| Output: | (long) retval | Type of entity as defined in swMateEntityTypes_e |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Based on the entity type, you know what to expect in the Mate::GetMateParams return value. To get to the MateEntity interface, use Mate::GetMateEntities.
