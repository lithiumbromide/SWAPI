---
title: "DrawingDoc::AddOrdinateDimension"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__AddOrdinateDimension.htm"
---

# DrawingDoc::AddOrdinateDimension

This method is obsolete and has been superseded by [DrawingDoc::AddOrdinateDimension2](DrawingDoc__AddOrdinateDimension2.htm).

Description

This method inserts an ordinate dimension, based on the current selections.

Syntax (OLE Automation)

retval = DrawingDoc.AddOrdinateDimension ( DimType, LocX, LocY, LocZ )

| Input: | (long) DimType | Dimension type as defined in swAddOrdinateDims_e |
| --- | --- | --- |
| Input: | (double) LocX | X location for the dimension |
| Input: | (double) LocY | Y location for the dimension |
| Input: | (double) LocZ | Z location for the dimension |
| Return: | (BOOL) retval | TRUE if created, FALSE if not |

Syntax (COM)

status = DrawingDoc->AddOrdinateDimension ( DimType, LocX, LocY, LocZ, &retval )

| Input: | (long) DimType | Dimension type as defined in swAddOrdinateDims_e |
| --- | --- | --- |
| Input: | (double) LocX | X location for the dimension |
| Input: | (double) LocY | Y location for the dimension |
| Input: | (double) LocZ | Z location for the dimension |
| Output: | (VARIANT_BOOL) retval | TRUE if created, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method creates a complete set of ordinate dimensions based on the current set of selections. First, select your 0 location from which all other dimensions are measured. SolidWorks uses all other selections to create additional ordinate measurements.

Selections made after the method is called continue to add ordinate measurements to the set. When you have finished adding measurements for an ordinate dimension set, use ModelDoc2::SetPickMode to clear the state.
