---
title: "IDisplayWireFrameXOR Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IDisplayWireFrameXOR"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDisplayWireFrameXOR.html"
---

# IDisplayWireFrameXOR Method (IBody2)

Displays a temporary body in the given part's context in XOR mode.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IDisplayWireFrameXOR( _
   ByVal Part As PartDoc, _
   ByVal Color As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim Part As PartDoc
Dim Color As System.Integer

instance.IDisplayWireFrameXOR(Part, Color)
```

### C#

```csharp
void IDisplayWireFrameXOR(
   PartDoc Part,
   System.int Color
)
```

### C++/CLI

```cpp
void IDisplayWireFrameXOR(
   PartDoc^ Part,
   System.int Color
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Part`: Pointer to the [part](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc.html)
- `Color`: Color of part

## VBA Syntax

See [Body2::IDisplayWireFrameXOR](ms-its:sldworksapivb6.chm::/sldworks~Body2~IDisplayWireFrameXOR.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::DisplayWireFrameXOR Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DisplayWireFrameXOR.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
