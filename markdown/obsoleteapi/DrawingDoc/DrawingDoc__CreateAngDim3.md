---
title: "DrawingDoc::CreateAngDim3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__CreateAngDim3.htm"
---

# DrawingDoc::CreateAngDim3

This method is obsolete and has been superseded by [DrawingDoc::CreateAngDim4](sldworksAPI.chm::/DrawingDoc/DrawingDoc__CreateAngDim4.htm).

Description

This method creates a non-associative angular dimension.

Syntax (OLE Automation)

retval = DrawingDoc.CreateAngDim3 ( vP0, vP1, vP2, vP3, vP4, vP5, vP6, arrowSize, text, textHeight, witnessGap, witnessOvershoot, vTextPoint )

| Input: | (VARIANT) vP0 | VARIANT of type SafeArray of 3 doubles (x,y,z), DimEnd Point |
| --- | --- | --- |
| Input: | (VARIANT) vP1 | VARIANT of type SafeArray of 3 doubles (x,y,z), DimPoint |
| Input: | (VARIANT) vP2 | VARIANT of type SafeArray of 3 doubles (x,y,z), Extension1 Start Point |
| Input: | (VARIANT) vP3 | VARIANT of type SafeArray of 3 doubles (x,y,z), Extension1 End Point |
| Input: | (VARIANT) vP4 | VARIANT of type SafeArray of 3 doubles (x,y,z), Extension2 Start Point |
| Input: | (VARIANT) vP5 | VARIANT of type SafeArray of 3 doubles (x,y,z), Extension2 End Point |
| Input: | (VARIANT) vP6 | VARIANT of type SafeArray of 3 doubles (x,y,z), Plane Normal |
| Input: | (double) arrowSize | Arrow size in meters |
| Input: | (BSTR) text | Dimension text string |
| Input: | (double) textHeight | Text height in meters |
| Input: | (double) witnessGap | Extension gap in meters |
| Input: | (double) witnessOvershoot | Extension overshoot in meters |
| Input: | (VARIANT) vTextPoint | Pointer to an array of 3 doubles (x,y,z), Position of text |
| Return: | (LPDISPATCH) retval | Dispatch pointer for the DisplayDimension created |

Syntax (COM)

status = DrawingDoc->ICreateAngDim3 ( P0, P1, P2, P3, P4, P5, P6, ArrowSize, text, TextHeight, WitnessGap, WitnessOvershoot, &TextPoint, &retval )

| Input: | (double*) P0 | Pointer to an array of 3 doubles (x,y,z), DimEnd Point |
| --- | --- | --- |
| Input: | (double*) P1 | Pointer to an array of 3 doubles (x,y,z), DimPoint |
| Input: | (double*) P2 | Pointer to an array of 3 doubles (x,y,z), Extension1 Start Point |
| Input: | (double*) P3 | Pointer to an array of 3 doubles (x,y,z), Extension1 End Point |
| Input: | (double*) P4 | Pointer to an array of 3 doubles (x,y,z), Extension2 Start Point |
| Input: | (double*) P5 | Pointer to an array of 3 doubles (x,y,z), Extension2 End Point |
| Input: | (double*) P6 | Pointer to an array of 3 doubles (x,y,z), Plane Normal |
| Input: | (double) ArrowSize | Arrow size in meters |
| Input: | (BSTR) text | Dimension text string |
| Input: | (double) TextHeight | Text height in meters |
| Input: | (double) WitnessGap | Extension gap in meters |
| Input: | (double) WitnessOvershoot | Extension overshoot in meters |
| Input: | (double) TextPoint | Pointer to an array of 3 doubles (x,y,z), Position of text |
| Output: | (LPDISPLAYDIMENSION) retval | Pointer to DisplayDimension object |
| Return: | (HRESULT) status | S_OK if Successful |

Remarks

SolidWorks creates this type of dimension between the specified points. It has no relation to your geometry.
