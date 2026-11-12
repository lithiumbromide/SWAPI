---
title: "GetClosestPointOn Method (IFace)"
project: "SOLIDWORKS API Help"
interface: "IFace"
member: "GetClosestPointOn"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace~GetClosestPointOn.html"
---

# GetClosestPointOn Method (IFace)

Obsolete. Superseded by [IFace2:: GetClosestPointOn](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetClosestPointOn.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetClosestPointOn( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFace
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Object

value = instance.GetClosestPointOn(X, Y, Z)
```

### C#

```csharp
System.object GetClosestPointOn(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
System.Object^ GetClosestPointOn(
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

See [Face::GetClosestPointOn](ms-its:sldworksapivb6.chm::/sldworks~Face~GetClosestPointOn.html).

## See Also

[IFace Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace.html)
[IFace Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace_members.html)
