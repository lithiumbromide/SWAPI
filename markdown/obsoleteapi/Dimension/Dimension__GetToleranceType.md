---
title: "Dimension::GetToleranceType"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Dimension/Dimension__GetToleranceType.htm"
---

# Dimension::GetToleranceType

This method is obsolete and has been superseded by [DimensionTolerance::Type](sldworksAPI.chm::/DimensionTolerance/DimensionTolerance__Type.htm).

Description

This method gets the type of tolerance of the dimension.

Syntax (OLE Automation)

retval = Dimension.GetToleranceType ( )

| Return: | (long) retval | Tolerance type as defined in swTolType_e |
| --- | --- | --- |

Syntax (COM)

status = Dimension->GetToleranceType ( &retval )

| Output: | (long) retval | Tolerance type as defined in swTolType_e |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
