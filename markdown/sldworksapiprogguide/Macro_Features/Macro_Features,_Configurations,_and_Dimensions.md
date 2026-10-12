---
title: "Macro Features, Configurations, and Dimensions"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Macro_Features/Macro_Features,_Configurations,_and_Dimensions.htm"
---

# Macro Features, Configurations, and Dimensions

## Macro Features and Configurations

When working with configurable dimensions and a macro feature, only your [edit definition function](Edit_Definition_Function.htm) should take into consideration configurations. In your edit definition function, you can use [IDimension::SetSystemValue3](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IDimension~SetSystemValue3.html) or [IDimension::ISetSystemValue3](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IDimension~ISetSystemValue3.html) to modify dimensions values as per the user’s changes. This is similar to how it works in the SOLIDWORKS Design user-interface when modifying feature dimensions across configurations.

Your [rebuild function](Rebuild_Function.htm) should not attempt to modify dimensions across configurations.
