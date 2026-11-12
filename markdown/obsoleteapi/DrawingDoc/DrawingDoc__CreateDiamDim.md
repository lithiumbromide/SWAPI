---
title: "DrawingDoc::CreateDiamDim"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__CreateDiamDim.htm"
---

# DrawingDoc::CreateDiamDim

This method is obsolete and has been superseded by [DrawingDoc::CreateDiamDim2](DrawingDoc__CreateDiamDim2.htm).

Description

This method creates a non-associative diameter dimension.

Syntax (OLE Automation)

retval = DrawingDoc.CreateDiamDim ( dimVal, vP0, vP1, vP2, vP3, arrowSize, text, textHeight, witnessGap, witnessOvershoot)

| Input: | (double) dimVal | Dimension value in meters |
| --- | --- | --- |
| Input: | (VARIANT) vP0 | VARIANT of type SafeArray of 3 doubles (x,y,z), Location of text |
| Input: | (VARIANT) vP1 | VARIANT of type SafeArray of 3 doubles (x,y,z), Nearest point on circle |
| Input: | (VARIANT) vP2 | VARIANT of type SafeArray of 3 doubles (x,y,z), Farthest point on circle diametrically opposite to vP1 |
| Input: | (VARIANT) vP3 | VARIANT of type SafeArray of 3 doubles (x,y,z), Plane normal |
| Input: | (double) arrowSize | Arrow size in meters |
| Input: | (BSTR) text | Dimension text string |
| Input: | (double) textHeight | Text height in meters |
| Input: | (double) witnessGap | Extension gap in meters |
| Input: | (double) witnessOvershoot | Extension overshoot in meters |
| Return: | (BOOL) retval | TRUE if success, FALSE if not |

Syntax (COM)

status = DrawingDoc->ICreateDiamDim ( DimValue, P0, P1, P2, P3, ArrowSize, Text, TextHeight, WitnessGap, WitnessOvershoot )

| Input: | (double) DimValue | Dimension value in meters |
| --- | --- | --- |
| Input: | (double*) P0 | Pointer to an array of 3 doubles (x,y,z), Location of text |
| Input: | (double*) P1 | Pointer to an array of 3 doubles (x,y,z), Nearest point on circle |
| Input: | (double*) P2 | Pointer to an array of 3 doubles (x,y,z), Farthest point on circle diametrically opposite to vP1 |
| Input: | (double*) P3 | Pointer to an array of 3 doubles (x,y,z), Plane normal |
| Input: | (double) ArrowSize | Arrow size in meters |
| Input: | (BSTR) Text | Dimension text string |
| Input: | (double) TextHeight | Text height in meters |
| Input: | (double) WitnessGap | Extension gap in meters |
| Input: | (double) WitnessOvershoot | Extension overshoot in meters |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

SolidWorks creates this type of dimension between the specified points. It has no relation to your geometry.
