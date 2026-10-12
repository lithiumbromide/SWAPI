---
title: "CreateArc2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "CreateArc2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~CreateArc2.html"
---

# CreateArc2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::CreateArc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateArc2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateArc2( _
   ByVal XC As System.Double, _
   ByVal YC As System.Double, _
   ByVal Zc As System.Double, _
   ByVal Xp1 As System.Double, _
   ByVal Yp1 As System.Double, _
   ByVal Zp1 As System.Double, _
   ByVal Xp2 As System.Double, _
   ByVal Yp2 As System.Double, _
   ByVal Zp2 As System.Double, _
   ByVal Direction As System.Short _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim XC As System.Double
Dim YC As System.Double
Dim Zc As System.Double
Dim Xp1 As System.Double
Dim Yp1 As System.Double
Dim Zp1 As System.Double
Dim Xp2 As System.Double
Dim Yp2 As System.Double
Dim Zp2 As System.Double
Dim Direction As System.Short
Dim value As System.Object

value = instance.CreateArc2(XC, YC, Zc, Xp1, Yp1, Zp1, Xp2, Yp2, Zp2, Direction)
```

### C#

```csharp
System.object CreateArc2(
   System.double XC,
   System.double YC,
   System.double Zc,
   System.double Xp1,
   System.double Yp1,
   System.double Zp1,
   System.double Xp2,
   System.double Yp2,
   System.double Zp2,
   System.short Direction
)
```

### C++/CLI

```cpp
System.Object^ CreateArc2(
   System.double XC,
   System.double YC,
   System.double Zc,
   System.double Xp1,
   System.double Yp1,
   System.double Zp1,
   System.double Xp2,
   System.double Yp2,
   System.double Zp2,
   System.short Direction
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `XC`:
- `YC`:
- `Zc`:
- `Xp1`:
- `Yp1`:
- `Zp1`:
- `Xp2`:
- `Yp2`:
- `Zp2`:
- `Direction`:

## VBA Syntax

See [ModelDoc::CreateArc2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~CreateArc2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
