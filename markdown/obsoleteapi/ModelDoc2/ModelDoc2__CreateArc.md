---
title: "ModelDoc2::CreateArc"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CreateArc.htm"
---

# ModelDoc2::CreateArc

This method is obsolete and has been superseded by [ModelDoc2::CreateArc2](ModelDoc2__CreateArc2.htm).

Description

This function creates an arc from P1 as center, from P2 to P3. You can use ModelDoc2::CreateArcVB in Visual Basic and other forms of Basic that do not support SafeArrays.

Syntax (OLE Automation)

retval = ModelDoc2.CreateArc ( P1, P2, P3, dir)

| Input: | (VARIANT) P1 | VARIANT of type SafeArray of 3 doubles (x1, y1, z1) in meters that describe the center point of the arc |
| --- | --- | --- |
| Input: | (VARIANT) P2 | VARIANT of type SafeArray of 3 double s(x2, y2, z2) in meters that describe the first point of the arc |
| Input: | (VARIANT) P3 | VARIANT of type SafeArrayof 3 doubles(x2, y2, z2) in meters that describe the second point of the arc |
| Input: | (short) dir | Direction of arc ( +1 or -1) |
| Return: | (VARIANT_BOOL) retval | TRUE if success, FALSE if fail |

Syntax (COM)

status = ModelDoc2->ICreateArc ( P1, P2, P3, dir )

| Input: | (double) P1 | VARIANT of type SafeArray of 3 doubles (x1, y1, z1) in meters that describe the center point of the arc |
| --- | --- | --- |
| Input: | (double) P2 | VARIANT of type SafeArray of 3 doubles (x2, y2, z2) in meters that describe the first point of the arc |
| Input: | (double) P3 | VARIANT of type SafeArray of 3 doubles (x2, y2, z2) in meters that describe the second point of the arc |
| Input: | (short) dir | Direction of arc ( +1 or -1) |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This method enables automatic relations for the arc that may not be suitable for creating very small arcs in database.
