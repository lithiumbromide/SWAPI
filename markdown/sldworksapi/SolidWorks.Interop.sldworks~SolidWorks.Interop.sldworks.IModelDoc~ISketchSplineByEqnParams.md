---
title: "ISketchSplineByEqnParams Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "ISketchSplineByEqnParams"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ISketchSplineByEqnParams.html"
---

# ISketchSplineByEqnParams Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::ISketchSplineByEqnParams](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ISketchSplineByEqnParams.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ISketchSplineByEqnParams( _
   ByRef PropArray As System.Integer, _
   ByRef KnotsArray As System.Double, _
   ByRef CntrlPntCoordArray As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim PropArray As System.Integer
Dim KnotsArray As System.Double
Dim CntrlPntCoordArray As System.Double
Dim value As System.Integer

value = instance.ISketchSplineByEqnParams(PropArray, KnotsArray, CntrlPntCoordArray)
```

### C#

```csharp
System.int ISketchSplineByEqnParams(
   ref System.int PropArray,
   ref System.double KnotsArray,
   ref System.double CntrlPntCoordArray
)
```

### C++/CLI

```cpp
System.int ISketchSplineByEqnParams(
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

See [ModelDoc::ISketchSplineByEqnParams](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~ISketchSplineByEqnParams.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
