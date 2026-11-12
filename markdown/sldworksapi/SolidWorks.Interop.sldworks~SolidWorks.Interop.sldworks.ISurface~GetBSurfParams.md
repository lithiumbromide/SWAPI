---
title: "GetBSurfParams Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "GetBSurfParams"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetBSurfParams.html"
---

# GetBSurfParams Method (ISurface)

Obsolete. Superseded by [ISurface::GetBSurfParams2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~GetBSurfParams2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBSurfParams( _
   ByVal WantCubicRational As System.Boolean, _
   ByVal VP0 As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim WantCubicRational As System.Boolean
Dim VP0 As System.Object
Dim value As System.Object

value = instance.GetBSurfParams(WantCubicRational, VP0)
```

### C#

```csharp
System.object GetBSurfParams(
   System.bool WantCubicRational,
   System.object VP0
)
```

### C++/CLI

```cpp
System.Object^ GetBSurfParams(
   System.bool WantCubicRational,
   System.Object^ VP0
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WantCubicRational`:
- `VP0`:

## VBA Syntax

See [Surface::GetBSurfParams](ms-its:sldworksapivb6.chm::/sldworks~Surface~GetBSurfParams.html).

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
