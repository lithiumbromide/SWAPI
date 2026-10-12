---
title: "IDisplayWireFrameXOR Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "IDisplayWireFrameXOR"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~IDisplayWireFrameXOR.html"
---

# IDisplayWireFrameXOR Method (IBody)

Obsolete. Superseded by [IBody2::IDisplayWireFromXOR](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IDisplayWireFrameXOR.html).

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
Dim instance As IBody
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

- `Part`:
- `Color`:

## VBA Syntax

See [Body::IDisplayWireFrameXOR](ms-its:sldworksapivb6.chm::/sldworks~Body~IDisplayWireFrameXOR.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
