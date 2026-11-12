---
title: "RayIntersections Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "RayIntersections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~RayIntersections.html"
---

# RayIntersections Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::RayIntersections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~RayIntersections.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function RayIntersections( _
   ByVal BodiesIn As System.Object, _
   ByVal BasePointsIn As System.Object, _
   ByVal VectorsIn As System.Object, _
   ByVal Options As System.Integer, _
   ByVal HitRadius As System.Double, _
   ByVal Offset As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim BodiesIn As System.Object
Dim BasePointsIn As System.Object
Dim VectorsIn As System.Object
Dim Options As System.Integer
Dim HitRadius As System.Double
Dim Offset As System.Double
Dim value As System.Integer

value = instance.RayIntersections(BodiesIn, BasePointsIn, VectorsIn, Options, HitRadius, Offset)
```

### C#

```csharp
System.int RayIntersections(
   System.object BodiesIn,
   System.object BasePointsIn,
   System.object VectorsIn,
   System.int Options,
   System.double HitRadius,
   System.double Offset
)
```

### C++/CLI

```cpp
System.int RayIntersections(
   System.Object^ BodiesIn,
   System.Object^ BasePointsIn,
   System.Object^ VectorsIn,
   System.int Options,
   System.double HitRadius,
   System.double Offset
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BodiesIn`:
- `BasePointsIn`:
- `VectorsIn`:
- `Options`:
- `HitRadius`:
- `Offset`:

## VBA Syntax

See [ModelDoc::RayIntersections](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~RayIntersections.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
