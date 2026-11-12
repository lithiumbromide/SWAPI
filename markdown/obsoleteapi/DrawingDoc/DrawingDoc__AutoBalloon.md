---
title: "DrawingDoc::AutoBalloon"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__AutoBalloon.htm"
---

# DrawingDoc::AutoBalloon

This method is obsolete and has been superseded by [DrawingDoc::AutoBalloon2](DrawingDoc__AutoBalloon2.htm).

Description

This method automatically inserts balloons in this drawing view.

Syntax (OLE Automation)

retval = DrawingDoc.AutoBalloon ( Layout)

| Input: | (long) Layout | Layout style of the balloons as defined by swBalloonLayoutType_e |
| --- | --- | --- |
| Output: | (VARIANT) retval | Array of Dispatch pointers of the notes created |

Syntax (COM)

status = DrawingDoc->AutoBalloon ( Layout, &retval)

| Input: | (long) Layout | Layout style of the balloons as defined by swBalloonLayoutType_e |
| --- | --- | --- |
| Output: | (VARIANT) retval | Array of Dispatch pointers of the notes created |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method automatically creates the BOM balloons for the selected drawing views. If a drawing sheet is selected, then all of the views in that sheet will have BOM balloons automatically created.

The Layout argument indicates how to initially lay out the balloons as defined by a value in swBalloonLayoutType_e. It provides options for laying out the balloons in a box or circle around the drawing view, or lined up along any of the edges of the drawing view. If this value is passed in as -1, then that indicates that the document default layout style should be used. To get or set that default value, use the ModelDoc2::GetUserPreferenceIntegerValue (swDetailingAutoBallonLayout) or ModelDoc2::SetUserPreferenceIntegerValue(swDetailingAutoBalloonLayout).

The balloon style follows the document defaults for single balloon style and balloon text. You can get and set balloon style and balloon using these APIs:

- ModelDoc2::GetUserPreferenceIntegerValue or ModelDoc2::SetUserPreferenceIntegerValue(swDetailingBOMBalloonStyle)
- ModelDoc2::GetUserPreferenceIntegerValue or ModelDoc2::SetUserPreferenceIntegerValue(swDetailingBOMBalloonFit)
- ModelDoc2::GetUserPreferenceIntegerValue or ModelDoc2::SetUserPreferenceIntegerValue(swDetailingBOMUpperText)
- ModelDoc2::GetUserPreferenceIntegerValue or ModelDoc2::SetUserPreferenceIntegerValue(swDetailingBOMLowerText)

This method also lets you get only the balloons just created.
