---
title: "Display Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "Display"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Display.html"
---

# Display Method (IBody2)

Obsolete. Superseded by [IBody2::Display3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~Display3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub Display( _
   ByVal Part As System.Object, _
   ByVal Color As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim Part As System.Object
Dim Color As System.Integer

instance.Display(Part, Color)
```

### C#

```csharp
void Display(
   System.object Part,
   System.int Color
)
```

### C++/CLI

```cpp
void Display(
   System.Object^ Part,
   System.int Color
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Part`:
- `Color`:

## VBA Syntax

See [Body2::Display](ms-its:sldworksapivb6.chm::/sldworks~Body2~Display.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
