---
title: "ModelDoc2::CreateLine"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CreateLine.htm"
---

# ModelDoc2::CreateLine

This method is obsolete and has been superseded by [ModelDoc2::CreateLine2](ModelDoc2__CreateLine2.htm).

Description

This method creates a line from P1 to P2.

NOTE: use ModelDoc2::CreateLineVB in Visual Basic and other forms of Basic that do not support SafeArrays. ModelDoc2::CreateLine and ModelDoc2::CreateLineVB enable automatic relations for the line that may not be suitable for creating very small segments in database.

Syntax (OLE Automation)

retval = ModelDoc2.CreateLine ( P1, P2)

| Input: | (VARIANT) P1 | VARIANT of type SafeArray of 3 doubles(x1, y1, z1) in meters that describe the first point of the line |
| --- | --- | --- |
| Input: | (VARIANT) P2 | VARIANT of type SafeArray of 3 doubles(x2, y2, z2) in meters that describe the second point of the line |
| Return: | (VARIANT_BOOL) retval | TRUE if success, FALSE if failure |

Syntax (COM)

status = ModelDoc2->ICreateLine ( P1, P2 )

| Input: | (double*) P1 | Pointer to an array of 3 doubles (x1, y1, z1) in meters that describe the first point of the line |
| --- | --- | --- |
| Input: | (double*) P2 | Pointer to an array of 3 doubles (x2, y2, z2) in meters that describe the second point of the line |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

ModelDoc2::SetAddToDB increases performance during entity creation by adding entities directly to the SolidWorks database. It also avoids inferencing.
