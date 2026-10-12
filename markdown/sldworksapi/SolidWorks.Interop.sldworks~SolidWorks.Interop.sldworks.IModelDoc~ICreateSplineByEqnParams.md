---
title: "ICreateSplineByEqnParams Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "ICreateSplineByEqnParams"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ICreateSplineByEqnParams.html"
---

# ICreateSplineByEqnParams Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::ICreateSplineByEqnParams](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ICreateSplineByEqnParams.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateSplineByEqnParams( _
   ByRef PropArray As System.Integer, _
   ByRef KnotsArray As System.Double, _
   ByRef CntrlPntCoordArray As System.Double _
) As SketchSegment
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim PropArray As System.Integer
Dim KnotsArray As System.Double
Dim CntrlPntCoordArray As System.Double
Dim value As SketchSegment

value = instance.ICreateSplineByEqnParams(PropArray, KnotsArray, CntrlPntCoordArray)
```

### C#

```csharp
SketchSegment ICreateSplineByEqnParams(
   ref System.int PropArray,
   ref System.double KnotsArray,
   ref System.double CntrlPntCoordArray
)
```

### C++/CLI

```cpp
SketchSegment^ ICreateSplineByEqnParams(
   System.int% PropArray,
   System.double% KnotsArray,
   System.double% CntrlPntCoordArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PropArray`:
- `KnotsArray`:
- `CntrlPntCoordArray`:

## VBA Syntax

See [ModelDoc::ICreateSplineByEqnParams](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~ICreateSplineByEqnParams.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
