---
title: "ICreateClippedSplines Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "ICreateClippedSplines"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ICreateClippedSplines.html"
---

# ICreateClippedSplines Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::ICreateClippedSplines](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ICreateClippedSplines.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateClippedSplines( _
   ByRef PropArray As System.Integer, _
   ByRef KnotsArray As System.Double, _
   ByRef CntrlPntCoordArray As System.Double, _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal X2 As System.Double, _
   ByVal Y2 As System.Double _
) As EnumSketchSegments
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim PropArray As System.Integer
Dim KnotsArray As System.Double
Dim CntrlPntCoordArray As System.Double
Dim X1 As System.Double
Dim Y1 As System.Double
Dim X2 As System.Double
Dim Y2 As System.Double
Dim value As EnumSketchSegments

value = instance.ICreateClippedSplines(PropArray, KnotsArray, CntrlPntCoordArray, X1, Y1, X2, Y2)
```

### C#

```csharp
EnumSketchSegments ICreateClippedSplines(
   ref System.int PropArray,
   ref System.double KnotsArray,
   ref System.double CntrlPntCoordArray,
   System.double X1,
   System.double Y1,
   System.double X2,
   System.double Y2
)
```

### C++/CLI

```cpp
EnumSketchSegments^ ICreateClippedSplines(
   System.int% PropArray,
   System.double% KnotsArray,
   System.double% CntrlPntCoordArray,
   System.double X1,
   System.double Y1,
   System.double X2,
   System.double Y2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PropArray`:
- `KnotsArray`:
- `CntrlPntCoordArray`:
- `X1`:
- `Y1`:
- `X2`:
- `Y2`:

## VBA Syntax

See [ModelDoc::ICreateClippedSplines](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~ICreateClippedSplines.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
