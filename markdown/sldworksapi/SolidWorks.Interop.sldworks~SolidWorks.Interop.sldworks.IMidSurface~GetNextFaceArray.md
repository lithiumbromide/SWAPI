---
title: "GetNextFaceArray Method (IMidSurface)"
project: "SOLIDWORKS API Help"
interface: "IMidSurface"
member: "GetNextFaceArray"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface~GetNextFaceArray.html"
---

# GetNextFaceArray Method (IMidSurface)

Obsolete. Superseded by [IMidSurface2::GetNextFaceArray](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface2~GetNextFaceArray.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNextFaceArray( _
   ByRef Thickness As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMidSurface
Dim Thickness As System.Double
Dim value As System.Object

value = instance.GetNextFaceArray(Thickness)
```

### C#

```csharp
System.object GetNextFaceArray(
   out System.double Thickness
)
```

### C++/CLI

```cpp
System.Object^ GetNextFaceArray(
   [Out] System.double Thickness
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Thickness`:

## VBA Syntax

See [MidSurface::GetNextFaceArray](ms-its:sldworksapivb6.chm::/sldworks~MidSurface~GetNextFaceArray.html).

## See Also

[IMidSurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface.html)
[IMidSurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface_members.html)
