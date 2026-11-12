---
title: "Display Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "Display"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~Display.html"
---

# Display Method (IBody)

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
Dim instance As IBody
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

See [Body::Display](ms-its:sldworksapivb6.chm::/sldworks~Body~Display.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
