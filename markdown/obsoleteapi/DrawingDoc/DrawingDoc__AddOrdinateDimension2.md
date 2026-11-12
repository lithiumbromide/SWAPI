---
title: "DrawingDoc::AddOrdinateDimension2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__AddOrdinateDimension2.htm"
---

# DrawingDoc::AddOrdinateDimension2

This method is obsolete and has been superseded by [ModelDocExtension::AddOrdinateDimension](sldworksAPI.chm::/ModelDocExtension/ModelDocExtension__AddOrdinateDimension.htm).

Description

This method inserts an ordinate dimension.

Syntax (OLE Automation)

retval = DrawingDoc.AddOrdinateDimension2 ( DimType, LocX, LocY, LocZ)

| Input: | (long) DimType | Dimension type as defined in swAddOrdinateDims_e |
| --- | --- | --- |
| Input: | (double) LocX | X location for the dimension |
| Input: | (double) LocY | Y location for the dimension |
| Input: | (double) LocZ | Z location for the dimension |
| Output: | (long*) retval | Error as defined by swCreateOrdDimError_e |

Syntax (COM)

status = DrawingDoc->AddOrdinateDimension2 ( DimType, LocX, LocY, LocZ, &retval)

| Input: | (long) DimType | Dimension type as defined in swAddOrdinateDims_e |
| --- | --- | --- |
| Input: | (double) LocX | X location for the dimension |
| Input: | (double) LocY | Y location for the dimension |
| Input: | (double) LocZ | Z location for the dimension |
| Output: | (long*) retval | Error as defined by swCreateOrdDimError_e |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method:

- Requires that you select two or more parallel edges. The ordinate origin is relative to the sheet origin and, depending on the type of ordinate dimension, either the X or Y value is ignored.
- Creates a complete set of ordinate dimensions based on the current set of selections. First, select your 0 location from which all other dimensions are measured. All other selections are used to create additional ordinate measurements.

Selections made after the method is called continue to add ordinate measurements to the set. When you have finished adding measurements for an ordinate dimension set, use ModelDoc2::SetPickMode to clear the state.

Any errors are returned as error codes, not dialog boxes.
