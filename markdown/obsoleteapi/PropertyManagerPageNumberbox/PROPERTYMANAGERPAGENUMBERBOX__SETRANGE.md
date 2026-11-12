---
title: "PropertyManagerPageNumberbox::SetRange"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPageNumberbox/PROPERTYMANAGERPAGENUMBERBOX__SETRANGE.HTM"
---

# PropertyManagerPageNumberbox::SetRange

This method is obsolete and has been superseded by [PropertyManagerPageNumberbox::SetRange2](sldworksAPI.chm::/PropertyManagerPageNumberBox/PropertyManagerPageNumberbox__SetRange2.htm).

Description

This method sets the range and increment for this number box.

Syntax (OLE Automation)

PropertyManagerPageNumberbox.SetRange ( Units, Minimum, Maximum, Increment )

| Input: | (long) Units | Number box units as defined in swNumberboxUnitType_e |
| --- | --- | --- |
| Input: | (double) Minimum | Number box minimum value |
| Input: | (double) Maximum | Number box maximum value |
| Input: | (double) Increment | Number box increment |
| Input: | (VARIANT_BOOL) Inclusive | TRUE sets the range as inclusive, FALSE sets it as exclusive |

Syntax (COM)

status = PropertyManagerPageNumberbox->SetRange ( Units, Minimum, Maximum, Increment )

| Input: | (long) Units | Number box units as defined in swNumberboxUnitType_e |
| --- | --- | --- |
| Input: | (double) Minimum | Number box minimum value |
| Input: | (double) Maximum | Number box maximum value |
| Input: | (double) Increment | Number box increment |
| Input: | (VARIANT_BOOL) Inclusive | TRUE sets the range as inclusive, FALSE sets it as exclusive |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You can only use this method to set properties on the PropertyManager page before it is displayed or while it is closed. See PropertyManagerPage2::Show2 and ProperytManagerPage2::Close.
