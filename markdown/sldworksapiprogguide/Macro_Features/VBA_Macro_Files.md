---
title: "VBA Macro Files"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Macro_Features/VBA_Macro_Files.htm"
---

# VBA Macro Files

## VBA Macro Files and Macro Features

Macro features that use VBA macros to define the [macro feature functions](Overview_of_Macro_Features.htm) must reside in SOLIDWORKS VBA macro files (*.swp).

Each function:

- Must accept these three arguments, which must be declared as type VARIANT:

For example:

```vb
Function swmRegen(app As Variant, part As Variant, feature As Variant) As Variant
```

- Can exist in the same or different file or module.
