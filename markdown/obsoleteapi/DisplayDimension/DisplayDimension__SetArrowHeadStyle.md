---
title: "DisplayDimension::SetArrowHeadStyle"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DisplayDimension/DisplayDimension__SetArrowHeadStyle.htm"
---

# DisplayDimension::SetArrowHeadStyle

This method is obsolete and has been superseded by [DisplayDimension::SetArrowHeadStyle2](sldworksAPI.chm::/DisplayDimension/DisplayDimension__SetArrowHeadStyle2.htm).

Description

This method sets the arrow head style of this display dimension.

Syntax (OLE Automation)

void DisplayDimension.SetArrowHeadStyle ( useDoc, arrowHeadStyle )

| Input: | (BOOL) useDoc | TRUE uses the document setting for arrow head style, FALSE uses the setting on this display dimension |
| --- | --- | --- |
| Input: | (BOOL) arrowHeadStyle | Arrow head style as defined in swArrowStyle_e if useDoc is FALSE |

Syntax (COM)

status = DisplayDimension->SetArrowHeadStyle ( useDoc, arrowHeadStyle )

| Input: | (VARIANT_BOOL) useDoc | TRUE uses the document setting for arrow head style, FALSE uses the setting on this display dimension |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) arrowHeadStyle | Arrow head style as defined in swArrowStyle_e if useDoc is FALSE |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The arrow head style for a display dimension is controlled by a value stored in one of two places: on the owning document or on the individual display dimension. Use DisplayDimension::GetUseDocArrowHeadStyle and DisplayDimension::GetArrowHeadStyle to get the current values for these settings.

The useDoc argument indicates if the document default setting for arrow head style should be used. If you set useDoc to FALSE, the arrowHeadStyle argument indicates the arrow head style used for this display dimension.

When you change the arrow head style, use ModelDoc2::GraphicsRedraw2 to redraw the graphics window and see your changes .
