---
title: "CreateCircleByRadius2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "CreateCircleByRadius2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~CreateCircleByRadius2.html"
---

# CreateCircleByRadius2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::CreateCircleByRadius2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateCircleByRadius2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateCircleByRadius2( _
   ByVal XC As System.Double, _
   ByVal YC As System.Double, _
   ByVal Zc As System.Double, _
   ByVal Radius As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim XC As System.Double
Dim YC As System.Double
Dim Zc As System.Double
Dim Radius As System.Double
Dim value As System.Object

value = instance.CreateCircleByRadius2(XC, YC, Zc, Radius)
```

### C#

```csharp
System.object CreateCircleByRadius2(
   System.double XC,
   System.double YC,
   System.double Zc,
   System.double Radius
)
```

### C++/CLI

```cpp
System.Object^ CreateCircleByRadius2(
   System.double XC,
   System.double YC,
   System.double Zc,
   System.double Radius
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `XC`:
- `YC`:
- `Zc`:
- `Radius`:

## VBA Syntax

See [ModelDoc::CreateCircleByRadius2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~CreateCircleByRadius2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
