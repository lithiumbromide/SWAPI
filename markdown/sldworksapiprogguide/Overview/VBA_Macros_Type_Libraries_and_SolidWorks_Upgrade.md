---
title: "VBA Macros, Type Libraries, and SOLIDWORKS Upgrade"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/VBA_Macros_Type_Libraries_and_SolidWorks_Upgrade.htm"
---

# VBA Macros, Type Libraries, and SOLIDWORKS Upgrade

When upgrading to a newer version of SOLIDWORKS, an existing VBA macro might fail on this line of code:

```vb
Set swApp = Application.SldWorks
```

with this message:

```vb
Compile error:
Object library feature not supported
```

#### To resolve compile error:

1. Click Tools, References in the IDE.
2. Select the SOLIDWORKS type libraries referenced by the VBA macro.
3. Use the up- and down-arrow buttons to change the priority of the selected SOLIDWORKS type libraries.
4. Click OK.

The type libraries should be reread by VBA. However, if the previous procedure fails:

1. Click Tools, References again.
2. Select a type library that is not used in the macro.
3. Click OK.

The type libraries should be reread by VBA. Once the macro runs, you can deselect the type library just selected.
