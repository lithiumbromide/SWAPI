---
title: "GetExtremePoint Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "GetExtremePoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~GetExtremePoint.html"
---

# GetExtremePoint Method (IBody)

Obsolete. Superseded by [IBody2::GetExtremePoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~GetExtremePoint.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetExtremePoint( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByRef Outx As System.Double, _
   ByRef Outy As System.Double, _
   ByRef Outz As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim Outx As System.Double
Dim Outy As System.Double
Dim Outz As System.Double
Dim value As System.Boolean

value = instance.GetExtremePoint(X, Y, Z, Outx, Outy, Outz)
```

### C#

```csharp
System.bool GetExtremePoint(
   System.double X,
   System.double Y,
   System.double Z,
   out System.double Outx,
   out System.double Outy,
   out System.double Outz
)
```

### C++/CLI

```cpp
System.bool GetExtremePoint(
   System.double X,
   System.double Y,
   System.double Z,
   [Out] System.double Outx,
   [Out] System.double Outy,
   [Out] System.double Outz
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`:
- `Y`:
- `Z`:
- `Outx`:
- `Outy`:
- `Outz`:

## VBA Syntax

See [Body::GetExtremePoint](ms-its:sldworksapivb6.chm::/sldworks~Body~GetExtremePoint.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
