---
title: "System Options > Drawings > AreaHatch/Fill"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/SO_Drawings-AreaHatchFill.htm"
---

# System Options > Drawings > AreaHatch/Fill

## System Options > Drawings > Area Hatch/Fill

| Setting | Get/Set Methods | Return Value or < Value > | Comment |
| --- | --- | --- | --- |
| None | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swDrawingAreaHatchFillStyle) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swDrawingAreaHatchFillStyle, swAreaHatchFillStyle_e.swAreaHatchFillStyle_None) | See swAreaHatchFillStyle_e for valid options |  |
| Solid | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swDrawingAreaHatchFillStyle) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swDrawingAreaHatchFillStyle, swAreaHatchFillStyle_e.swAreaHatchFillStyle_Solid) | See swAreaHatchFillStyle_e for valid options |  |
| Hatch | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swDrawingAreaHatchFillStyle) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swDrawingAreaHatchFillStyle, swAreaHatchFillStyle_e.swAreaHatchFillStyle_Pattern) | See swAreaHatchFillStyle_e for valid options |  |
| Pattern | ISldWorks::GetUserPreferenceStringValue (swUserPreferenceStringValue_e.swDrawingAreaHatchPattern) ISldWorks::SetUserPreferenceStringValue (swUserPreferenceStringValue_e.swDrawingAreaHatchPattern, < Value >) | String value |  |
| Scale | ISldWorks::GetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swDrawingAreaHatchScale) ISldWorks::SetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swDrawingAreaHatchScale, < Value >) | Double value | Specifies value to scale crosshatch |
| Angle | ISldWorks::GetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swDrawingAreaHatchAngle) ISldWorks::SetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swDrawingAreaHatchAngle, < Value >) | Double value | Specifies angle for crosshatch |
