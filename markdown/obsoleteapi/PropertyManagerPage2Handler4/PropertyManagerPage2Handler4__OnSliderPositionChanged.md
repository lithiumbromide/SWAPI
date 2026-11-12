---
title: "PropertyManagerPage2Handler4::OnSliderPositionChanged"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler4/PropertyManagerPage2Handler4__OnSliderPositionChanged.htm"
---

# PropertyManagerPage2Handler4::OnSliderPositionChanged

This method is obsolete and has been superseded by [PropertyManagerPage2Handler5::OnSliderPositionChanged](sldworksAPI.chm::/PropertyManagerPage2Handler5/PropertyManagerPage2Handler5__OnSliderPositionChanged.htm).

Description

This method is called whenever the user changes the position of a slider control on this PropertyManager.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler4.OnSliderPositionChanged ( Id, Value)

| Input: | (long) Id | ID of slider control |
| --- | --- | --- |
| Input: | (double) Value | Value indicating the new position of the slider |

Syntax (COM)

status = PropertyManagerPage2Handler4->OnSliderPositionChanged ( Id, Value)

| Input: | (long) Id | ID of slider control |
| --- | --- | --- |
| Input: | (double) Value | Value indicating the new position of the slider |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Although Value is declared as a double, the value of a slider is always a long. When this method is called, Value can be cast to a long.

If PropertyManagerPageSlider::Style is set to swPropMgrPageSliderStyle_NotifyWhileTracking, then you can use:

- PropertyManagerPage2Handler4::OnSliderPositionChanged to receive notifications every time the position of the slider changes because the slider is being dragged.

  NOTE: This might result in numerous calls to the handler, which is fine if the add-in responds quickly to each call. However, if the add-in responds slowly, then a performance bottleneck might occur.
- PropertyManagerPage2Handler4::OnSliderTrackingCompleted to receive one notification when dragging of the slider is completed.
