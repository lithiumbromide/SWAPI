---
title: "CreateCircle2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "CreateCircle2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~CreateCircle2.html"
---

# CreateCircle2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::CreateCircle2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateCircle2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateCircle2( _
   ByVal XC As System.Double, _
   ByVal YC As System.Double, _
   ByVal Zc As System.Double, _
   ByVal Xp As System.Double, _
   ByVal Yp As System.Double, _
   ByVal Zp As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim XC As System.Double
Dim YC As System.Double
Dim Zc As System.Double
Dim Xp As System.Double
Dim Yp As System.Double
Dim Zp As System.Double
Dim value As System.Object

value = instance.CreateCircle2(XC, YC, Zc, Xp, Yp, Zp)
```

### C#

```csharp
System.object CreateCircle2(
   System.double XC,
   System.double YC,
   System.double Zc,
   System.double Xp,
   System.double Yp,
   System.double Zp
)
```

### C++/CLI

```cpp
System.Object^ CreateCircle2(
   System.double XC,
   System.double YC,
   System.double Zc,
   System.double Xp,
   System.double Yp,
   System.double Zp
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `XC`:
- `YC`:
- `Zc`:
- `Xp`:
- `Yp`:
- `Zp`:

## VBA Syntax

See [ModelDoc::CreateCircle2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~CreateCircle2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
