---
title: "Display2 Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "Display2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Display2.html"
---

# Display2 Method (IBody2)

Obsolete. Superseded by [IBody2::Display3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~Display3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub Display2( _
   ByVal Part As PartDoc, _
   ByVal Color As System.Integer, _
   ByVal Option As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim Part As PartDoc
Dim Color As System.Integer
Dim Option As System.Integer

instance.Display2(Part, Color, Option)
```

### C#

```csharp
void Display2(
   PartDoc Part,
   System.int Color,
   System.int Option
)
```

### C++/CLI

```cpp
void Display2(
   PartDoc^ Part,
   System.int Color,
   System.int Option
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Part`:
- `Color`:
- `Option`:

## VBA Syntax

See [Body2::Display2](ms-its:sldworksapivb6.chm::/sldworks~Body2~Display2.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
