---
title: "DisplayDimension::SetPrecision"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DisplayDimension/DisplayDimension__SetPrecision.htm"
---

# DisplayDimension::SetPrecision

This method is obsolete and has been superseded by [DisplayDimension::SetPrecison2](sldworksAPI.chm::/DisplayDimension/DisplayDimension__SetPrecision2.htm).

Description

This method sets the displayed precisions of this display dimension and its tolerance values.

Syntax (OLE Automation)

retval = DisplayDimension.SetPrecision ( useDoc, primary, alternate, primaryTol, alternateTol )

| Input: | (BOOL) useDoc | TRUE uses the document settings, FALSE uses the settings on this display dimension (see below) |
| --- | --- | --- |
| Input: | (long) primary | Number of decimal places displayed in the dimension value |
| Input: | (long) alternate | Number of decimal places displayed in the dual dimension value |
| Input: | (long) primaryTol | Number of decimal places displayed in the tolerance value |
| Input: | (long) alternateTol | Number of decimal places displayed in the dual tolerance value |
| Return: | (long) retval | Return status (see below) |

Syntax (COM)

status = DisplayDimension->SetPrecision ( useDoc, primary, alternate, primaryTol, alternateTol, &retval )

| Input: | (BOOL) useDoc | TRUE uses the document settings, FALSE uses the settings on this display dimension (see below) |
| --- | --- | --- |
| Input: | (long) primary | Number of decimal places displayed in the dimension value |
| Input: | (long) alternate | Number of decimal places displayed in the dual dimension value |
| Input: | (long) primaryTol | Number of decimal places displayed in the tolerance value |
| Input: | (long) alternateTol | Number of decimal places displayed in the dual tolerance value |
| Output: | (long) retval | Return status (see below) |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The displayed precision of a dimension and its tolerance values can be controlled by a value is stored in one of two places: on the owning document or on the individual display dimension. The useDoc argument allows you to control whether to use the default document settings or the values specified in the primary, alternate, primaryTol, and alternateTol arguments.

If useDoc is TRUE, then SolidWorks ignores the primary, alternate, primaryTol, and alternateTol arguments.

The specified precision values must be in the range between 0 and 8. This indicates to SolidWorks how many decimal places to display. You can also set the precision to -1, which maintains the current setting. SolidWorks considers any other values invalid. If a precision is invalid, SolidWorks uses the current setting and continues processing he other precision values.

retval indicates the success or failure of this method. In general, a value less than 0 indicates that the command failed and SolidWorks did not set any precision values. A value of 0 indicates success. A value greater than 0 indicates that a problem occurred, but the command did not fail.

| -1 | Command failed, no precision values were set |
| --- | --- |
| 0 | Command was successful, all precision values were set |
| 1 | Primary precision argument was invalid |
| 2 | Alternate precision argument was invalid |
| 3 | Primary tolerance precision argument was invalid |
| 4 | Alternate tolerance precision argument was invalid |

When you use this method, use ModelDoc2::GraphicsRedraw2 to redraw the graphics window and see your changes.
