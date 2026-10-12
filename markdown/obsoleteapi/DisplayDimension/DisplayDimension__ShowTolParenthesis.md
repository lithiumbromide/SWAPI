---
title: "DisplayDimension::ShowTolParenthesis"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DisplayDimension/DisplayDimension__ShowTolParenthesis.htm"
---

# DisplayDimension::ShowTolParenthesis

This property is obsolete and has been superseded by [DimensionTolerance::ShowParenthesis](sldworksAPI.chm::/DimensionTolerance/DimensionTolerance__ShowParenthesis.htm).

Description

This property gets or sets whether the dimension tolerance is displayed with parenthesis around the text.

Syntax (OLE Automation)

retval = DisplayDimension.ShowTolParenthesis (VB Get property)

DisplayDimension.ShowTolParenthesis = show (VB Set property)

retval = DisplayDimension.GetShowTolParenthesis ( ) (C++ Get property)

DisplayDimension.SetShowTolParenthesis ( show ) (C++ Set property)

| Output: | (VARIANT_BOOL) retval | TRUE displays dimension tolerance text in parenthesis, FALSE does not |
| --- | --- | --- |

Syntax (COM)

status = DisplayDimension->get_ShowTolParenthesis ( &retval )

status = DisplayDimension->put_ShowTolParenthesis ( show )

| Output: | (VARIANT_BOOL) retval | TRUE displays dimension tolerance text in parenthesis, FALSE does not |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
