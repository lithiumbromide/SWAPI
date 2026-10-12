---
title: "DisplayWireFrameXOR Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "DisplayWireFrameXOR"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~DisplayWireFrameXOR.html"
---

# DisplayWireFrameXOR Method (IBody)

Obsolete. Superseded by [IBody2::DisplayWireFrameXOR](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~DisplayWireFrameXOR.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub DisplayWireFrameXOR( _
   ByVal Part As System.Object, _
   ByVal Color As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim Part As System.Object
Dim Color As System.Integer

instance.DisplayWireFrameXOR(Part, Color)
```

### C#

```csharp
void DisplayWireFrameXOR(
   System.object Part,
   System.int Color
)
```

### C++/CLI

```cpp
void DisplayWireFrameXOR(
   System.Object^ Part,
   System.int Color
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Part`:
- `Color`:

## VBA Syntax

See [Body::DisplayWireFrameXOR](ms-its:sldworksapivb6.chm::/sldworks~Body~DisplayWireFrameXOR.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
