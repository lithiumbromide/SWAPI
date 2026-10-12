---
title: "System Options > View"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/SO_View.htm"
---

# System Options > View

| Setting | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Reverse mouse wheel zoom direction | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swViewReverseWheelZoomDirection) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swViewReverseWheelZoomDirection, < OnFlag >) | Boolean value | Specifies whether to reverse a mouse's wheel zoom direction |
| Zoom to fit when changing to standard views | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swViewZoomFitAndCenter) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swViewZoomFitAndCenter, < OnFlag >) | Boolean value | Specifies whether to zoom-to-fit view when changing to standard views |
| View rotation - Arrow keys | ISldWorks::GetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swViewRotationArrowKeys) ISldWorks::SetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swViewRotationArrowKeys, < Value >) | Double value in radians | Specifies angle increment for view rotation when arrow keys are used to rotate model |
| View rotation - Mouse speed | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swViewRotationMouseSpeed) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swViewRotationMouseSpeed, < Value >) | Integer value from 1 to 100 | Specifies the speed of rotation when you use the mouse to rotate the model or assembly component |
| Transitions - View transition | ISldWorks::GetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swViewAnimationSpeed) ISldWorks::SetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swViewAnimationSpeed, < Value >) | Double value: 0 = off >0 - 3 seconds | Specifies animation-like speed when changing views |
| Transitions - Hide/show component | ISldWorks::GetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swViewTransitionHideShowComponent) ISldWorks::SetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swViewTransitionHideShowComponent, < Value >) | Double value | Specifies the animation-like speed at which to transition the view when hiding or showing components |
| Transitions - Isolate | ISldWorks::GetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swViewTransitionIsolate) ISldWorks::SetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swViewTransitionIsolate, < Value >) | Double value | Specifies the animation-like speed at which to transition the view when isolating a component in assemblies and multi-body parts |
| Transitions - View selector | ISldWorks::GetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swViewSelectorSpeed) ISldWorks::SetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swViewSelectorSpeed, < Value >) | Double value | Specifies the speed of the View selector animation; 0 indicates no animation and the current model is shown in the background; 3.0 is the maximum value |
