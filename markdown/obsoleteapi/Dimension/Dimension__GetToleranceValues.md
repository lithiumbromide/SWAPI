---
title: "Dimension::GetToleranceValues"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Dimension/Dimension__GetToleranceValues.htm"
---

# Dimension::GetToleranceValues

This method is obsolete and has been superseded by [DimensionTolerance::GetMaxValue](sldworksAPI.chm::/DimensionTolerance/DimensionTolerance__GetMaxValue.htm) and [DimensionTolerance::GetMinValue](sldworksAPI.chm::/DimensionTolerance/DimensionTolerance__GetMinValue.htm).

Description

This method gets the tolerance minimum and maximum values.

Syntax (OLE Automation)

retval = Dimension.GetToleranceValues ( )

| Return: | (VARIANT) retval | SafeArray of two doubles containing the minimum and maximum values |
| --- | --- | --- |

Syntax (COM)

status = Dimension->IGetToleranceValues ( retval )

| Output: | (double*) retval | Pointer to array of two doubles containing the minimum and maximum values |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
