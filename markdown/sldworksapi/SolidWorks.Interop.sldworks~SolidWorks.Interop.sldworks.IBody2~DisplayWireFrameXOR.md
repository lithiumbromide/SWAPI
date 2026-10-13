---
title: "DisplayWireFrameXOR Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "DisplayWireFrameXOR"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DisplayWireFrameXOR.html"
---

# DisplayWireFrameXOR Method (IBody2)

Displays a temporary body in the given part's context in XOR mode.

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
Dim instance As IBody2
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

- `Part`: Part
- `Color`: Color of part

## VBA Syntax

See [Body2::DisplayWireFrameXOR](ms-its:sldworksapivb6.chm::/sldworks~Body2~DisplayWireFrameXOR.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::IDisplayWireFrameXOR Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDisplayWireFrameXOR.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
