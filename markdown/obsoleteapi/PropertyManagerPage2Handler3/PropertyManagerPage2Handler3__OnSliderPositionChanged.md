---
title: "PropertyManagerPage2Handler3::OnSliderPositionChanged"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler3/PropertyManagerPage2Handler3__OnSliderPositionChanged.htm"
---

# PropertyManagerPage2Handler3::OnSliderPositionChanged

This method is obsolete and has been superseded by [PropertyManagerPage2Handler4::OnSliderPositionChanged](../PropertyManagerPage2Handler4/PropertyManagerPage2Handler4__OnSliderPositionChanged.htm).

Description

This method is called when a user changes the position of a slider control on this PropertyManager.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler3.OnSliderPositionChanged ( Id, Value)

| Input: | (long) Id | ID of slider control |
| --- | --- | --- |
| Input: | (double) Value | Value indicating the new position of the slider |

Syntax (COM)

status = PropertyManagerPage2Handler3->OnSliderPositionChanged ( Id, Value)

| Input: | (long) Id | ID of slider control |
| --- | --- | --- |
| Input: | (double) Value | Value indicating the new position of the slider |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Although Value is declared as a double, the value of a slider is always a long. When this method is called, Value can be cast to a long.

PropertyManagerPageSlider::Style set to swPropMgrPageSliderStyule_NotifyWhileTracking affects when and how often PropertyManagerPage2Handler3::OnSliderPositionChanged is called.
