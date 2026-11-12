---
title: "System Options > Import > IDF"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/FileOpenOptionsIDF.htm"
---

# System Options > Import > IDF

To display the dialog:

Click **Tools > Options > System Options > Import > IDF** in **File Format**.

- or -

1. Click **File > Open**.
2. In **Files of type**, select **IDF**.
3. Click **Options**.

| Setting | Get/Set Methods | Return Value or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Add board drilled holes | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swImportIDFAddDrilledHoles) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swImportIDFAddDrilledHoles. < OnFlag >) | Boolean value | Specifies whether to add drilled holes from the circuit board; for Intermediate Data Format (IDF) circuit boards files only |
| Reverse underside components | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swImportIDFReverseUndersideComponents) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swImportIDFReverseUndersideComponents. < OnFlag >) | Boolean value | Specifies whether to compensate for incorrectly rotated components by allowing proper location of the component features; for Intermediate Data Format (IDF) circuit board files only |
