---
title: "IDisplay Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IDisplay"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDisplay.html"
---

# IDisplay Method (IBody2)

Obsolete. Superseded by [IBody2::Display3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~Display3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub IDisplay( _
   ByVal Part As PartDoc, _
   ByVal Color As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim Part As PartDoc
Dim Color As System.Integer

instance.IDisplay(Part, Color)
```

### C#

```csharp
void IDisplay(
   PartDoc Part,
   System.int Color
)
```

### C++/CLI

```cpp
void IDisplay(
   PartDoc^ Part,
   System.int Color
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Part`:
- `Color`:

## VBA Syntax

See [Body2::IDisplay](ms-its:sldworksapivb6.chm::/sldworks~Body2~IDisplay.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
