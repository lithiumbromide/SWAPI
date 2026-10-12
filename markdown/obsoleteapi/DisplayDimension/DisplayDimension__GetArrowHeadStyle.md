---
title: "DisplayDimension::GetArrowHeadStyle"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DisplayDimension/DisplayDimension__GetArrowHeadStyle.htm"
---

# DisplayDimension::GetArrowHeadStyle

This method is obsolete and has been superseded by [DisplayDimension::GetArrowHeadStyle2](sldworksAPI.chm::/DisplayDimension/DisplayDimension__GetArrowHeadStyle2.htm).

Description

This method gets the arrow head style used by this display dimension.

Syntax (OLE Automation)

retval = DisplayDimension.GetArrowHeadStyle ( )

| Return: | (long) retval | Arrow head style as defined in swArrowStyle_e |
| --- | --- | --- |

Syntax (COM)

status = DisplayDimension->GetArrowHeadStyle ( &retval )

| Output: | (long) retval | Arrow head style as defined in swArrowStyle_e |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You can control the arrow head style for a display dimension with a value that SolidWorks stores in one of two places: on the owning document or on the individual display dimension. Use DisplayDimension::GetUseDocArrowHeadStyle to determine whether the document or the individual display dimension is controlling the arrow head style.

This method returns the arrow head style for this display dimension. If this display dimension is set to use the document settings for arrow head style, then this method might return a value that different than what is displayed.

Use DisplayDimension::SetArrowHeadStyle to set the arrow head style.
