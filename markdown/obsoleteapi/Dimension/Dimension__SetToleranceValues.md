---
title: "Dimension::SetToleranceValues"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Dimension/Dimension__SetToleranceValues.htm"
---

# Dimension::SetToleranceValues

This method is obsolete and has been superseded by [DimensionTolerance::SetValues](sldworksAPI.chm::/DimensionTolerance/DimensionTolerance__SetValues.htm).

Description

This method sets the tolerance minimum and maximum values.

Syntax (OLE Automation)

retval = Dimension.SetToleranceValues ( tolMin, tolMax )

| Input: | (double) tolMin | Minimum tolerance value |
| --- | --- | --- |
| Input: | (double) tolMax | Maximum tolerance value |
| Return: | (BOOL) retval | TRUE if the values were set successfully, FALSE if they were not |

Syntax (COM)

status = Dimension->SetToleranceValues ( tolMin, tolMax, &retval )

| Input: | (double) tolMin | Minimum tolerance value |
| --- | --- | --- |
| Input: | (double) tolMax | Maximum tolerance value |
| Output: | (VARIANT_BOOL) retval | TRUE if the values were set successfully, FALSE if they were not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

For symmetric tolerances, this method uses the tolMax value.

You cannot set the tolerance values if the tolerance type is swTolNONE.
