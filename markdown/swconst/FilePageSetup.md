---
title: "File > Page Setup"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/FilePageSetup.htm"
---

# File > Page Setup

This topic contains two tables. The information in the table:

- appearing immediately after the screen capture of the Page Setup dialog corresponds to the settings on that dialog.
- titled [Obsolete Enumerators](#Obsolete) contains enumerators that previously appeared on the Page Setup dialog, but are now obsolete and no longer appear on that dialog.

| Setting | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Use system settings | See Comment | See Comment | Not currently available in SOLIDWORKS API |
| Use this document settings | See Comment | See Comment | Not currently available in SOLIDWORKS API |
| Set each drawing sheet individually | See Comment | See Comment | Not currently available in SOLIDWORKS API |
| Settings for | See Comment | See Comment | Not currently available in SOLIDWORKS API |
| Scale and Resolution - Scale to fit | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swPageSetupDrawingScaleToFit) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swPageSetupDrawingScaleToFit, < OnFlag >) | Boolean value | Specifies whether to print drawing sheet to fit paper size; for drawings only; Use system settings on Page Setup dialog must be selected when changing this setting. |
| Scale and Resolution - Scale | See Comment | See Comment | Not currently available in SOLIDWORKS API |
| Scale and Resolution - < n > | See Comment | See Comment | Not currently available in SOLIDWORKS API |
| Scale and Resolution - High Quality | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swPageSetupHighQuality) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swPageSetupHighQuality, < OnFlag >) | Boolean value | Specifies whether to load all model information into memory; for drawings only |
| Scale and Resolution - Scale draft edges | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swPageSetupScaleDraftEdges) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swPageSetupScaleDraftEdges, < OnFlag >) | Boolean value | Specifies whether to scale draft edges; for drawings only |
| Drawing Color - Automatic | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swPageSetupDrawingColor) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swPageSetupDrawingColor, swPageSetupDrawingColor_e.swPageSetup_AutomaticDrawingColor) | swPageSetupDrawingColor_e.swPageSetup_AutomaticDrawingColor | See swPageSetupDrawingColor_e for all valid options |
| Drawing Color - Color / Gray scale | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swPageSetupDrawingColor) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swPageSetupDrawingColor, swPageSetupDrawingColor_e.swPageSetup_ColorGrey) | swPageSetupDrawingColor_e.swPageSetup_ColorGrey) | See swPageSetupDrawingColor_e for all valid options |
| Drawing Color - Black and white | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swPageSetupDrawingColor) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swPageSetupDrawingColor, swPageSetupDrawingColor_e.swPageSetup_BlackAndWhite) | swPageSetupDrawingColor_e.swPageSetup_BlackAndWhite) | See swPageSetupDrawingColor_e for all valid options |
| Paper - Size | See Comment | See Comment | Defined by the operating system or by a specific printer device; there is no SOLIDWORKS API enumeration for these values |
| Paper - Source | See Comment | See Comment | Defined by the operating system or by a specific printer device; there is no SOLIDWORKS API enumeration for these values |
| Orientation - Portrait | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swPageSetupPrinterOrientation) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swPageSetupPrinterOrientation, swPageSetupOrientation_e.swPageSetupOrient_Portrait) | swPageSetupOrientation_e.swPageSetupOrient_Portrait | See swPageSetupOrientation_e for all valid options |
| Orientation - Landscape | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swPageSetupPrinterOrientation) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swPageSetupPrinterOrientation, swPageSetupOrientation_e.swPageSetupOrient_Landscape) | swPageSetupOrientation_e.swPageSetupOrient_Landsacpe | See swPageSetupOrientation_e for all valid options |

Obsolete Enumerators

| Enumerator | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| swPageSetupPrinterPartAsmPrintWindow | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swPageSetupPrinterPartAsmPrintWindow) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swPageSetupPrinterPartAsmPrintWindow, < OnFlag >) | Boolean value | Obsolete ; for parts and assemblies only; specified whether to print current view of the graphics area; Use system settings on Page Setup dialog must be selected when changing this setting |
| swPageSetupDrawingScale | ISldWorks::GetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e, swPageSetupDrawingScale) ISldWorks::SetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e, swPageSetupDrawingScale, < Value >) | Double value | Obsolete |
| swPageSetupPrinterPartAsmScale | ISldWorks::GetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e, swPageSetupPrinterPartAsmScale) ISldWorks::SetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e, swPageSetupPrinterPartAsmScale, < Value >) | Double value | Obsolete |
