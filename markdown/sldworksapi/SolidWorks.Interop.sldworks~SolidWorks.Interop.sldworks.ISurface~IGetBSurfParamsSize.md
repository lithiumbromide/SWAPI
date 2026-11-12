---
title: "IGetBSurfParamsSize Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "IGetBSurfParamsSize"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetBSurfParamsSize.html"
---

# IGetBSurfParamsSize Method (ISurface)

Obsolete. Superseded by [ISurface::IGetBSurfParamsSize3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~IGetBSurfParamsSize3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetBSurfParamsSize( _
   ByVal WantCubicRational As System.Boolean, _
   ByRef Range As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim WantCubicRational As System.Boolean
Dim Range As System.Double
Dim value As System.Integer

value = instance.IGetBSurfParamsSize(WantCubicRational, Range)
```

### C#

```csharp
System.int IGetBSurfParamsSize(
   System.bool WantCubicRational,
   ref System.double Range
)
```

### C++/CLI

```cpp
System.int IGetBSurfParamsSize(
   System.bool WantCubicRational,
   System.double% Range
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WantCubicRational`:
- `Range`:

## VBA Syntax

See [Surface::IGetBSurfParamsSize](ms-its:sldworksapivb6.chm::/sldworks~Surface~IGetBSurfParamsSize.html).

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
