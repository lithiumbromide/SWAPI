---
title: "ICreateSplinesByEqnParams Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "ICreateSplinesByEqnParams"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ICreateSplinesByEqnParams.html"
---

# ICreateSplinesByEqnParams Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::ICreateSplinesByEqnParams](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ICreateSplinesByEqnParams.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateSplinesByEqnParams( _
   ByRef PropArray As System.Integer, _
   ByRef KnotsArray As System.Double, _
   ByRef CntrlPntCoordArray As System.Double _
) As EnumSketchSegments
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim PropArray As System.Integer
Dim KnotsArray As System.Double
Dim CntrlPntCoordArray As System.Double
Dim value As EnumSketchSegments

value = instance.ICreateSplinesByEqnParams(PropArray, KnotsArray, CntrlPntCoordArray)
```

### C#

```csharp
EnumSketchSegments ICreateSplinesByEqnParams(
   ref System.int PropArray,
   ref System.double KnotsArray,
   ref System.double CntrlPntCoordArray
)
```

### C++/CLI

```cpp
EnumSketchSegments^ ICreateSplinesByEqnParams(
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

See [ModelDoc::ICreateSplinesByEqnParams](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~ICreateSplinesByEqnParams.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
