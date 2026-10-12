---
title: "DrawingDoc::CreateLinearDim3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__CreateLinearDim3.htm"
---

# DrawingDoc::CreateLinearDim3

This method is obsolete and has been superseded by [DrawingDoc::CreateLinearDim4](sldworksAPI.chm::/DrawingDoc/DrawingDoc__CreateLinearDim4.htm).

Description

This method creates a non-associative linear dimension.

Syntax (OLE Automation)

retval = DrawingDoc.CreateLinearDim3 ( p0, p1, p2, p3, p4, val, primPrec, text, TextPoint, angle, textHeight, prefix, suffix, callout1, callout2, tolType, tolMin, tolMax, tolPrec, arrowSize, arrowStyle, arrowDir, WitnessGap, WitnessOvershoot, dualDisplay, dualPrec )

| Input: | (VARIANT) p0 | VARIANT of type SafeArray of 3 doubles (x,y,z), dimension point |
| --- | --- | --- |
| Input: | (VARIANT) p1 | VARIANT of type SafeArray of 3 doubles (x,y,z), dimension end |
| Input: | (VARIANT) p2 | VARIANT of type SafeArray of 3 doubles (x,y,z), normal to the plane of sketch |
| Input: | (VARIANT) p3 | VARIANT of type SafeArray of 3 doubles (x,y,z), extension line 1 reference point |
| Input: | (VARIANT) p4 | VARIANT of type SafeArray of 3 doubles (x,y,z), extension line 2 reference point |
| Input: | (double) val | Value for dimension |
| Input: | (long) primPrec | Number of digits after the decimal point for dimension values |
| Input: | (BSTR) text | Dimension text string |
| Input: | (VARIANT) TextPoint | VARIANT of type SafeArray of 3 doubles (x,y,z) containing position of text |
| Input: | (double) angle | Inclination angle of the text in radians |
| Input: | (double) textHeight | Text height in meters |
| Input: | (BSTR) prefix | Prefix for dimension |
| Input: | (BSTR) suffix | Suffix for dimension |
| Input: | (BSTR) callout1 | First callout |
| Input: | (BSTR) callout2 | Second callout |
| Input: | (long) tolType | Type of tolerance as defined in swTolType_e |
| Input: | (BSTR) tolMin | Minimum tolerance |
| Input: | (BSTR) tolMax | Maximum tolerance |
| Input: | (long) tolPrec | Number of digits after the decimal point for tolerance values |
| Input: | (double) arrowSize | Arrow size meters |
| Input: | (long) arrowStyle | Arrow style as defined in swArryowStyle_e |
| Input: | (long) arrowDir | Arrow direction as defined in swArrowDirection_e |
| Input: | (double) WitnessGap | Extension gap in meters |
| Input: | (double) WitnessOvershoot | Extension overshoot in meters |
| Input: | (BOOL) dualDisplay | TRUE to display dimensions in both English and metric units, FALSE to not |
| Input: | (long) dualPrec | Number of digits after the decimal point for dimension values |
| Return: | (LPDISPATCH) retval | Dispatch pointer for the newly created DisplayDimnesion object |

Syntax (COM)

status = DrawingDoc->ICreateLinearDim3 ( P0, P1, P2, P3, P4, val, primPrec, Text, &TextPoint, Angle, TextHeight, prefix, suffix, callout1, callout2, tolType, tolMin, tolMax, tolPrec, ArrowSize, arrowStyle, arrowDir, WitnessGap, WitnessOvershoot, dualDisplay, dualPrecision, &retval )

| Input: | (double*) P0 | Pointer to an array of 3 doubles (x,y,z), dimension point |
| --- | --- | --- |
| Input: | (double*) P1 | Pointer to an array of 3 doubles (x,y,z), dimension end |
| Input: | (double*) P2 | Pointer to an array of 3 doubles (x,y,z), normal to the plane of sketch |
| Input: | (double*) P3 | Pointer to an array of 3 doubles (x,y,z), extension line 1 reference point |
| Input: | (double*) P4 | Pointer to an array of 3 doubles (x,y,z), extension line 2 reference point |
| Input: | (double) val | Value of linear dimension |
| Input: | (long) primPrec | Number of digits after the decimal point for dimension values |
| Input: | (BSTR) Text | Dimension text string |
| Input: | (double) TextPoint | VARIANT of type SafeArray of 3 doubles (x,y,z) containing position of text |
| Input: | (double) Angle | Inclination angle of the text in radians |
| Input: | (double) TextHeight | Text height in meters |
| Input: | (BSTR) prefix | Prefix for dimension |
| Input: | (BSTR) suffix | Suffix for dimension |
| Input: | (BSTR) callout1 | First callout |
| Input: | (BSTR) callout2 | Second callout |
| Input: | (long) tolType | Type of tolerance as defined in swTolType_e |
| Input: | (BSTR) tolMin | Minimum tolerance |
| Input: | (BSTR) tolMax | Maximum tolerance |
| Input: | (long) tolPrec | Number of digits after the decimal point for tolerance values |
| Input: | (double) ArrowSize | Arrow size meters |
| Input: | (long) arrowStyle | Arrow style as defined in swArryowStyle_e |
| Input: | (long) arrowDir | Arrow direction as defined in swArrowDirection_e |
| Input: | (double) WitnessGap | Extension gap in meters |
| Input: | (double) WitnessOvershoot | Extension overshoot in meters |
| Input: | (VARIANT_BOOL) dualDisplay | TRUE to display dimensions in both English and metric units, FALSE to not |
| Input: | (long) dualPrecision | Number of digits after the decimal point for dimension values |
| Output: | (LPDISPLAYDIMENSION) retval | Pointer to DisplayDimension object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

SolidWorks creates this type of dimension between the two specified points. It has no relation to your geometry.
