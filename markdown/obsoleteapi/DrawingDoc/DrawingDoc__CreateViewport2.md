---
title: "DrawingDoc::CreateViewport2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__CreateViewport2.htm"
---

# DrawingDoc::CreateViewport2

This method is obsolete and has been superseded by [DrawingDoc::CreateViewport3](sldworksAPI.chm::/DrawingDoc/DrawingDoc__CreateViewport3.htm).

Description

This method creates a viewport on a drawing.

Syntax (OLE Automation)

retval = DrawingDoc.CreateViewport2 ( LowerLeftX, LowerLeftY, UpperRightX, UpperRightY, sketchSize, scale)

| Input: | (double) LowerLeftX | X value for the lower-left corner of the new viewport |
| --- | --- | --- |
| Input: | (double) LowerLeftY | Y value for the lower-left corner of the new viewport |
| Input: | (double) UpperRightX | X value for the upper-right corner of the new viewport |
| Input: | (double) UpperRightY | Y value for the upper-right corner of the new viewport |
| Input: | (short) sketchSize | Approximate number of entities |
| Input: | (double) scale | Scale to be used for this viewport |
| Return: | (BSTR) retval | Name of the newly created viewport |

Syntax (COM)

status = DrawingDoc->CreateViewport2 ( LowerLeftX, LowerLeftY, UpperRightX, UpperRightY, sketchSize, scale, &retval )

| Input: | (double) LowerLeftX | X value for the lower-left corner of the new viewport |
| --- | --- | --- |
| Input: | (double) LowerLeftY | Y value for the lower-left corner of the new viewport |
| Input: | (double) UpperRightX | X value for the upper-right corner of the new viewport |
| Input: | (double) UpperRightY | Y value for the upper-right corner of the new viewport |
| Input: | (short) sketchSize | Approximate number of entities |
| Input: | (double) scale | Scale to be used for this viewport |
| Output: | (BSTR) retval | Name of the newly created viewport |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The default sketchSize value is 0. If you are creating more than 500 sketch entities, specify a value instead of using the default.

After you use this method, you can create sketch entities in the new viewport. One advantage is that users can move the entities around the drawing by dragging the viewport instead of selecting all the entities.
