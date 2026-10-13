---
title: "Mate::GetMateEntities"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Mate/Mate__GetMateEntities.htm"
---

# Mate::GetMateEntities

This method is obsolete and has not been superseded.

Description

An assembly mate is always a relation between two entities. This method returns those two mate entities. You can use these returned objects to access the MateEntity interface, which provides methods for analyzing the mate entity.

Syntax (OLE Automation)

retval = Mate.GetMateEntities ()

| Return: | (VARIANT) retval | VARIANT of type SafeArray containing two Dispatch pointers to the MateEntity objects |
| --- | --- | --- |

Syntax (COM)

status = Mate->IGetMateEntities ( &entity1, &entity2 )

| Output: | (LPMATEENTITY) entity1 | Pointer to the first MateEntity object |
| --- | --- | --- |
| Output: | (LPMATEENTITY) entity2 | Pointer to the second MateEntity object |
| Return: | (HRESULT)status | S_OK if successful |

Remarks
