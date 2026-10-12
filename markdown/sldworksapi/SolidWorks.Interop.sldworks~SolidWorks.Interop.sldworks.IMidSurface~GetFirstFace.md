---
title: "GetFirstFace Method (IMidSurface)"
project: "SOLIDWORKS API Help"
interface: "IMidSurface"
member: "GetFirstFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface~GetFirstFace.html"
---

# GetFirstFace Method (IMidSurface)

Obsolete. Superseded by [IMidSurface2::GetFirstFace](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface2~GetFirstFace.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstFace( _
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

value = instance.GetFirstFace(FromFace1Disp, FromFace2Disp, Thickness)
```

### C#

```csharp
System.object GetFirstFace(
   out System.object FromFace1Disp,
   out System.object FromFace2Disp,
   out System.double Thickness
)
```

### C++/CLI

```cpp
System.Object^ GetFirstFace(
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

See [MidSurface::GetFirstFace](ms-its:sldworksapivb6.chm::/sldworks~MidSurface~GetFirstFace.html).

## See Also

[IMidSurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface.html)
[IMidSurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface_members.html)
