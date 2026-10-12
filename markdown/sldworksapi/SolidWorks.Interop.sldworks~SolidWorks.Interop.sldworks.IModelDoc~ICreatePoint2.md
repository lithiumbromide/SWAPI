---
title: "ICreatePoint2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "ICreatePoint2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ICreatePoint2.html"
---

# ICreatePoint2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::ICreatePoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ICreatePoint2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreatePoint2( _
   ByVal PointX As System.Double, _
   ByVal PointY As System.Double, _
   ByVal PointZ As System.Double _
) As SketchPoint
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim PointX As System.Double
Dim PointY As System.Double
Dim PointZ As System.Double
Dim value As SketchPoint

value = instance.ICreatePoint2(PointX, PointY, PointZ)
```

### C#

```csharp
SketchPoint ICreatePoint2(
   System.double PointX,
   System.double PointY,
   System.double PointZ
)
```

### C++/CLI

```cpp
SketchPoint^ ICreatePoint2(
   System.double PointX,
   System.double PointY,
   System.double PointZ
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PointX`:
- `PointY`:
- `PointZ`:

## VBA Syntax

See [ModelDoc::ICreatePoint2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~ICreatePoint2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
