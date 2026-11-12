---
title: "Dimension::SetToleranceType"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Dimension/Dimension__SetToleranceType.htm"
---

# Dimension::SetToleranceType

This method is obsolete and has been superseded by [DimensionTolerance::Type](sldworksAPI.chm::/DimensionTolerance/DimensionTolerance__Type.htm).

Description

This method sets the tolerance type of the dimension.

Syntax (OLE Automation)

retval = Dimension.SetToleranceType ( newType )

| Input: | (long) newType | Tolerance type as defined in swTolType_e |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if the tolerance type was set successfully, FALSE if it was not |

Syntax (COM)

status = Dimension->SetToleranceType ( newType, &retval )

| Input: | (long) newType | Tolerance type as defined in swTolType_e |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the tolerance type was set successfully, FALSE if it was not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
