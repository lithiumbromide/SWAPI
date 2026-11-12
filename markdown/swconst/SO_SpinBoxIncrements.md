---
title: "System Options > Spin Box Increments"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/SO_SpinBoxIncrements.htm"
---

# System Options > Spin Box Increments

| Setting | Get/Set Methods | Return Value or < Value > | Comment |
| --- | --- | --- | --- |
| Length increments - English units | ISldWorks::GetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swSpinBoxEnglishLengthIncrement) ISldWorks::SetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swSpinBoxEnglishLengthIncrement, < Value >) | Double value in inches | Specifies number of inches added or subtracted when spin box arrow is clicked to change a linear dimension value; see Units to learn how to set length units using the SOLIDWORKS API |
| Length increments - Metric units | ISldWorks::GetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swSpinBoxMetricLengthIncrement) ISldWorks::SetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swSpinBoxMetricLengthIncrement, < Value >) | Double value in metric units | Specifies number of units added or subtracted when a spin box arrow is clicked to change a linear dimension value; see Units to learn how to set length units using the SOLIDWORKS API |
| Angle increments | ISldWorks::GetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swSpinBoxAngleIncrement) ISldWorks::SetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swSpinBoxAngleIncrement, < Value >) | Double value in angular units | Specifies number of angular units added or subtracted when a spin box arrow is clicked to change an angular dimension value; see Units to learn how to set angular units using the SOLIDWORKS API |
| Time increments | ISldWorks::GetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swSpinBoxTimeIncrement) ISldWorks::SetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swSpinBoxTimeIncrement, < Value >) | Double value in time units | Specifies number of units added or subtracted when a spin box arrow is clicked to change a time value; see Units to learn how to set time units using the SOLIDWORKS API |
