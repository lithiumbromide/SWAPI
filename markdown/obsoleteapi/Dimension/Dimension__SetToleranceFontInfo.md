---
title: "Dimension::SetToleranceFontInfo"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Dimension/Dimension__SetToleranceFontInfo.htm"
---

# Dimension::SetToleranceFontInfo

This method is obsolete and has been superseded by [DimensionTolerance::SetFont](sldworksAPI.chm::/DimensionTolerance/DimensionTolerance__SetFont.htm).

Description

This method sets the tolerance font information.

Syntax (OLE Automation)

retval = Dimension.SetToleranceFontInfo ( useFontScale, tolScale, tolHeight )

| Input: | (long) useFontScale | TRUE if the tolerance font size is a scaled value of the dimension font size |
| --- | --- | --- |
| Input: | (double) tolScale | Tolerance font size scale factor based on the dimension font size if useFontScale is TRUE |
| Input: | (double) tolHeight | Tolerance height in meters if useFontScale is FALSE |
| Return: | (BOOL) retval | TRUE if the values were set successfully, FALSE if they were not |

Syntax (COM)

status = Dimension->SetToleranceFontInfo ( useFontScale, tolScale, tolHeight, &retval )

| Input: | (long) useFontScale | TRUE if the tolerance font size is a scaled value of the dimension font size |
| --- | --- | --- |
| Input: | (double) tolScale | Tolerance font size scale factor based on the dimension font size if useFontScale is TRUE |
| Input: | (double) tolHeight | Tolerance height in meters if useFontScale is FALSE |
| Output: | (VARIANT_BOOL) retval | TRUE if the values were set successfully, FALSE if they were not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

For example, to use the dimension font size, set useFontScale to TRUE and tolScale to 1.0

You cannot set tolerance values if the tolerance type is swTolNONE.
