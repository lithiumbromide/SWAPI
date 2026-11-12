---
title: "IRayIntersections Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "IRayIntersections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IRayIntersections.html"
---

# IRayIntersections Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::IRayIntersections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IRayIntersections.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IRayIntersections( _
   ByRef BodiesIn As Body, _
   ByVal NumBodies As System.Integer, _
   ByRef BasePointsIn As System.Double, _
   ByRef VectorsIn As System.Double, _
   ByVal NumRays As System.Integer, _
   ByVal Options As System.Integer, _
   ByVal HitRadius As System.Double, _
   ByVal Offset As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim BodiesIn As Body
Dim NumBodies As System.Integer
Dim BasePointsIn As System.Double
Dim VectorsIn As System.Double
Dim NumRays As System.Integer
Dim Options As System.Integer
Dim HitRadius As System.Double
Dim Offset As System.Double
Dim value As System.Integer

value = instance.IRayIntersections(BodiesIn, NumBodies, BasePointsIn, VectorsIn, NumRays, Options, HitRadius, Offset)
```

### C#

```csharp
System.int IRayIntersections(
   ref Body BodiesIn,
   System.int NumBodies,
   ref System.double BasePointsIn,
   ref System.double VectorsIn,
   System.int NumRays,
   System.int Options,
   System.double HitRadius,
   System.double Offset
)
```

### C++/CLI

```cpp
System.int IRayIntersections(
   Body^% BodiesIn,
   System.int NumBodies,
   System.double% BasePointsIn,
   System.double% VectorsIn,
   System.int NumRays,
   System.int Options,
   System.double HitRadius,
   System.double Offset
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BodiesIn`:
- `NumBodies`:
- `BasePointsIn`:
- `VectorsIn`:
- `NumRays`:
- `Options`:
- `HitRadius`:
- `Offset`:

## VBA Syntax

See [ModelDoc::IRayIntersections](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~IRayIntersections.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
