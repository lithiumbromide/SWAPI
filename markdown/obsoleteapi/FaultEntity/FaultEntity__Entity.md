---
title: "FaultEntity::Entity"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/FaultEntity/FaultEntity__Entity.htm"
---

# FaultEntity::Entity

This property is obsolete and has been superseded by [FaultEntity::Entity2](sldworksAPI.chm::/FaultEntity/FaultEntity__Entity2.htm).

Description

This property gets the entity.

Syntax (OLE Automation)

entity = FaultEntity.Entity ( index ) (VB Get property)

entity = FaultEntity.GetEntity ( index ) (C++ Get property)

| Input: | (long) index | 0-based index number indicating the entity to get |
| --- | --- | --- |
| Output: | (LPENTITY) entity | Pointer to the Entity object |

Syntax (COM)

status = FaultEntity->get_Entity ( index, &entity )

| Input: | (long) index | 0-based index number indicating the entity to get |
| --- | --- | --- |
| Output: | (LPENTITY) entity | Pointer to the Entity object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
