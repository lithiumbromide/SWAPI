---
title: "IGetClosestPointOn Method (IFace)"
project: "SOLIDWORKS API Help"
interface: "IFace"
member: "IGetClosestPointOn"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace~IGetClosestPointOn.html"
---

# IGetClosestPointOn Method (IFace)

Obsolete. Superseded by [IFace2::IGetClosestPointOn](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IGetClosestPointOn.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetClosestPointOn( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IFace
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Double

value = instance.IGetClosestPointOn(X, Y, Z)
```

### C#

```csharp
System.double IGetClosestPointOn(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
System.double IGetClosestPointOn(
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`:
- `Y`:
- `Z`:

## VBA Syntax

See [Face::IGetClosestPointOn](ms-its:sldworksapivb6.chm::/sldworks~Face~IGetClosestPointOn.html).

## See Also

[IFace Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace.html)
[IFace Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace_members.html)
