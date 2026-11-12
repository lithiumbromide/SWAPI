---
title: "Dimension::GetToleranceFontInfo"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Dimension/Dimension__GetToleranceFontInfo.htm"
---

# Dimension::GetToleranceFontInfo

This method is obsolete and has been superseded by [DimensionTolerance::GetFontUseDimension](sldworksAPI.chm::/DimensionTolerance/DimensionTolerance__GetFontUseDimension.htm), [DimensionTolerance::GetFontUseScale](sldworksAPI.chm::/DimensionTolerance/DimensionTolerance__GetFontUseScale.htm), [DimensionTolerance::GetFontScale](sldworksAPI.chm::/DimensionTolerance/DimensionTolerance__GetFontScale.htm), and [DimensionTolerance::GetFontHeight](sldworksAPI.chm::/DimensionTolerance/DimensionTolerance__GetFontHeight.htm).

Description

This method gets the tolerance font information for this dimension.

Syntax (OLE Automation)

retval = Dimension.GetToleranceFontInfo ( )

| Return: | (VARIANT) retval | SafeArray of 3 doubles (see Remarks ) |
| --- | --- | --- |

Syntax (COM)

status = Dimension->IGetToleranceFontInfo ( retval )

| Output: | (double*) retval | Pointer to array of 3 doubles (see Remarks ) |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method returns font information that contains three values packed into an array of doubles:

[ long useFontScale, double tolScale, double tolHeight ]

| useFontScale | TRUE if the tolerance font size is a scaled value of the dimension font size |
| --- | --- |
| TolScale | Tolerance font size scale factor based on the dimension font size if useFontScale is TRUE |
| TolHeight | Tolerance height in meters if useFontScale is FALSE |
