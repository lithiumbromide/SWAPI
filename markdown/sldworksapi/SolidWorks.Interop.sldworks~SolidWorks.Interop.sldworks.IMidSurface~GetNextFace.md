---
title: "GetNextFace Method (IMidSurface)"
project: "SOLIDWORKS API Help"
interface: "IMidSurface"
member: "GetNextFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface~GetNextFace.html"
---

# GetNextFace Method (IMidSurface)

Obsolete. Superseded by [IMidSurface2::GetNextFace](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface2~GetNextFace.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNextFace( _
   ByRef FromFace1Disp As System.Object, _
   ByRef FromFace2Disp As System.Object, _
   ByRef Thickness As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMidSurface
Dim FromFace1Disp As System.Object
Dim FromFace2Disp As System.Object
Dim Thickness As System.Double
Dim value As System.Object

value = instance.GetNextFace(FromFace1Disp, FromFace2Disp, Thickness)
```

### C#

```csharp
System.object GetNextFace(
   out System.object FromFace1Disp,
   out System.object FromFace2Disp,
   out System.double Thickness
)
```

### C++/CLI

```cpp
System.Object^ GetNextFace(
   [Out] System.Object^ FromFace1Disp,
   [Out] System.Object^ FromFace2Disp,
   [Out] System.double Thickness
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FromFace1Disp`:
- `FromFace2Disp`:
- `Thickness`:

## VBA Syntax

See [MidSurface::GetNextFace](ms-its:sldworksapivb6.chm::/sldworks~MidSurface~GetNextFace.html).

## See Also

[IMidSurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface.html)
[IMidSurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface_members.html)
