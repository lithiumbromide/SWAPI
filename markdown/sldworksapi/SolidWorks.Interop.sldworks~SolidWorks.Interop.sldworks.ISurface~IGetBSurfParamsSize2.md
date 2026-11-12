---
title: "IGetBSurfParamsSize2 Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "IGetBSurfParamsSize2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetBSurfParamsSize2.html"
---

# IGetBSurfParamsSize2 Method (ISurface)

Obsolete. Superseded by [ISurface::IGetBSurfParamsSize3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~IGetBSurfParamsSize3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetBSurfParamsSize2( _
   ByVal WantCubic As System.Boolean, _
   ByVal WantNonRational As System.Boolean, _
   ByRef Range As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim WantCubic As System.Boolean
Dim WantNonRational As System.Boolean
Dim Range As System.Double
Dim value As System.Integer

value = instance.IGetBSurfParamsSize2(WantCubic, WantNonRational, Range)
```

### C#

```csharp
System.int IGetBSurfParamsSize2(
   System.bool WantCubic,
   System.bool WantNonRational,
   ref System.double Range
)
```

### C++/CLI

```cpp
System.int IGetBSurfParamsSize2(
   System.bool WantCubic,
   System.bool WantNonRational,
   System.double% Range
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WantCubic`:
- `WantNonRational`:
- `Range`:

## VBA Syntax

See [Surface::IGetBSurfParamsSize2](ms-its:sldworksapivb6.chm::/sldworks~Surface~IGetBSurfParamsSize2.html).

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
