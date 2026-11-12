---
title: "SketchPolygon Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SketchPolygon"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SketchPolygon.html"
---

# SketchPolygon Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SketchPolygon](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SketchPolygon.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SketchPolygon( _
   ByVal XCenter As System.Double, _
   ByVal YCenter As System.Double, _
   ByVal XEdge As System.Double, _
   ByVal YEdge As System.Double, _
   ByVal NSides As System.Integer, _
   ByVal BInscribed As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim XCenter As System.Double
Dim YCenter As System.Double
Dim XEdge As System.Double
Dim YEdge As System.Double
Dim NSides As System.Integer
Dim BInscribed As System.Boolean
Dim value As System.Boolean

value = instance.SketchPolygon(XCenter, YCenter, XEdge, YEdge, NSides, BInscribed)
```

### C#

```csharp
System.bool SketchPolygon(
   System.double XCenter,
   System.double YCenter,
   System.double XEdge,
   System.double YEdge,
   System.int NSides,
   System.bool BInscribed
)
```

### C++/CLI

```cpp
System.bool SketchPolygon(
   System.double XCenter,
   System.double YCenter,
   System.double XEdge,
   System.double YEdge,
   System.int NSides,
   System.bool BInscribed
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `XCenter`:
- `YCenter`:
- `XEdge`:
- `YEdge`:
- `NSides`:
- `BInscribed`:

## VBA Syntax

See [ModelDoc::SketchPolygon](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SketchPolygon.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
