---
title: "ModelDoc::CreateLine"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateLine.htm"
---

# ModelDoc::CreateLine

This method is obsolete and has been superseded by [ModelDoc::CreateLine2](ModelDoc__CreateLine2.htm).

Description

This method creates a line from P1 to P2. It also enables automatic relations for the line, which may not be suitable for creating very small segments in database.

Syntax (OLE Automation)

retval = ModelDoc.CreateLine ( P1, P2)

| Input: | (VARIANT) P1 | VARIANT of type SafeArray of 3 doubles (x1, y1, z1) in meters that describe the first point of the line |
| --- | --- | --- |
| Input: | (VARIANT) P2 | VARIANT of type SafeArray of 3 doubles (x2, y2, z2) in meters that describe the second point of the line |
| Return: | (BOOL) retval | TRUE if success, FALSE if fail |

Syntax (COM)

status = ModelDoc->ICreateLine ( P1, P2 )

| Input: | (double*) P1 | Pointer to an array of 3 doubles (x1, y1, z1) in meters that describe the first point of the line |
| --- | --- | --- |
| Input: | (double*) P2 | Pointer to an array of 3 doubles (x2, y2, z2) in meters that describe the second point of the line |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The ModelDoc::SetAddToDB method increases performance during entity creation by adding entities directly to the SolidWorks database, and it also avoids inferencing.
