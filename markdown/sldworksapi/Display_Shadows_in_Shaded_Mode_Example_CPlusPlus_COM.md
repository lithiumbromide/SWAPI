---
title: "Display Shadows in Shaded Mode Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Display_Shadows_in_Shaded_Mode_Example_CPlusPlus_COM.htm"
---

# Display Shadows in Shaded Mode Example (C++ COM)

## Display Shadow Example

This example shows how to turn on shadows using swDisplayShadowsInShadedMode, which is a system setting.

```vb
iSldWorks->SetUserPreferenceToggle(swDisplayShadowsInShadedMode, TRUE);
pInputDoc->GraphicsRedraw2();
```
