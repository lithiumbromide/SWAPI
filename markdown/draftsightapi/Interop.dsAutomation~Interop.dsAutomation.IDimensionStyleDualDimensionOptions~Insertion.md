---
title: "Insertion Property (IDimensionStyleDualDimensionOptions)"
project: ""
interface: "IDimensionStyleDualDimensionOptions"
member: "Insertion"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleDualDimensionOptions~Insertion.html"
---

# Insertion Property (IDimensionStyleDualDimensionOptions)

Gets or sets whether to place dual Dimensions before or after the primary Dimensions.

## Syntax

### Visual Basic

```vb
Property Insertion As dsDualDimensionInsertPlacement_e
```

### C#

```csharp
dsDualDimensionInsertPlacement_e Insertion {get; set;}
```

### JScript

```
function get,set Insertion : dsDualDimensionInsertPlacement_e
```

### Managed Extensions for C++

```
__property dsDualDimensionInsertPlacement_e get_Insertion();
__property void set_Insertion(
   dsDualDimensionInsertPlacement_e value
);
```

### C++/CLI

```cpp
property dsDualDimensionInsertPlacement_e Insertion {
   dsDualDimensionInsertPlacement_e get();
   void set (    dsDualDimensionInsertPlacement_e value);
}
```

### Property Value

True to place dual Dimensions after primary Dimensions, false to place them before

## See Also

[IDimensionStyleDualDimensionOptions Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleDualDimensionOptions.html)
[IDimensionStyleDualDimensionOptions Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleDualDimensionOptions_members.html)

## Availability

DraftSight V1R1.2
