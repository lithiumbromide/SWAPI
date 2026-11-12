---
title: "ICreateSpline Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "ICreateSpline"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ICreateSpline.html"
---

# ICreateSpline Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::ICreateSpline](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ICreateSpline.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateSpline( _
   ByVal PointCount As System.Integer, _
   ByRef PointData As System.Double _
) As SketchSegment
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim PointCount As System.Integer
Dim PointData As System.Double
Dim value As SketchSegment

value = instance.ICreateSpline(PointCount, PointData)
```

### C#

```csharp
SketchSegment ICreateSpline(
   System.int PointCount,
   ref System.double PointData
)
```

### C++/CLI

```cpp
SketchSegment^ ICreateSpline(
   System.int PointCount,
   System.double% PointData
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PointCount`:
- `PointData`:

## VBA Syntax

See [ModelDoc::ICreateSpline](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~ICreateSpline.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
