---
title: "GetFirstFaceArray Method (IMidSurface)"
project: "SOLIDWORKS API Help"
interface: "IMidSurface"
member: "GetFirstFaceArray"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface~GetFirstFaceArray.html"
---

# GetFirstFaceArray Method (IMidSurface)

Obsolete. Superseded by [IMidSurface2::GetFirstFaceArray](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface2~GetFirstFaceArray.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstFaceArray( _
   ByRef Thickness As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMidSurface
Dim Thickness As System.Double
Dim value As System.Object

value = instance.GetFirstFaceArray(Thickness)
```

### C#

```csharp
System.object GetFirstFaceArray(
   out System.double Thickness
)
```

### C++/CLI

```cpp
System.Object^ GetFirstFaceArray(
   [Out] System.double Thickness
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Thickness`:

## VBA Syntax

See [MidSurface::GetFirstFaceArray](ms-its:sldworksapivb6.chm::/sldworks~MidSurface~GetFirstFaceArray.html).

## See Also

[IMidSurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface.html)
[IMidSurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface_members.html)
