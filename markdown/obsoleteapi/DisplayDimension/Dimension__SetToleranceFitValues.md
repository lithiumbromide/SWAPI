---
title: "Dimension::SetToleranceFitValues"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DisplayDimension/Dimension__SetToleranceFitValues.htm"
---

# Dimension::SetToleranceFitValues

This method is obsolete and has been superseded by [DimensionTolerance::SetFitValues](sldworksAPI.chm::/DimensionTolerance/DimensionTolerance__SetFitValues.htm).

Description

This method sets the tolerance values for fit tolerances.

Syntax (OLE Automation)

retval = Dimension.SetToleranceFitValues ( newLValue, newUValue )

| Input: | (BSTR) newLValue | Lower tolerance value (a single character) |
| --- | --- | --- |
| Input: | (BSTR) newUValue | Upper tolerance value (a single character) |
| Return: | (BOOL) retval | TRUE if the values were set successfully, FALSE if they were not |

Syntax (COM)

status = Dimension->SetToleranceFitValues ( newLValue, newUValue, &retval )

| Input: | (BSTR) newLValue | Lower tolerance value (a single character) |
| --- | --- | --- |
| Input: | (BSTR) newUValue | Upper tolerance value (a single character) |
| Output: | (VARIANT_BOOL) retval | TRUE if the values were set successfully, FALSE if they were not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You cannot set the tolerance values if the tolerance type is swTolNONE.
