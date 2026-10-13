---
title: "Mate::GetEntity"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Mate/Mate__GetEntity.htm"
---

# Mate::GetEntity

This method is obsolete and has been superseded by [Mate2::MateEntity](sldworksAPI.chm::/Mate2/Mate2__MateEntity.htm).

Description

This method gets an entity that is associated with an assembly mate.

Syntax (OLE Automation)

entity = Mate.GetEntity( whichOne )

| Input: | (int) whichOne | 0-based index of the entity associated with the mate |
| --- | --- | --- |
| Return: | (LPDISPATCH) entity | Dispatch pointer for the entity (face, edge and so on) or NULL if a MateEntity is the origin of a component |

Syntax (COM)

status = Mate->IGetEntity ( whichOne, &entity )

| Input: | (int) whichOne | 0-based index of the entity associated with the mate |
| --- | --- | --- |
| Output: | (LPENTITY) entity | Pointer to an Entity object (underlying face, edge and so on) or NULL if a MateEntity is the origin of a component |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The Entity object returned is only valid in the context of its owning mate. In other words, the Entity object returned is only valid in the assembly that owns this mate. You cannot use this Entity object at the PartDoc level.

Lightweight components are unable to return an Entity object from this method. For more information, see Working With Lightweight Components.
