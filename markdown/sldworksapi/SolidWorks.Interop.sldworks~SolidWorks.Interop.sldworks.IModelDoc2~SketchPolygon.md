---
title: "SketchPolygon Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SketchPolygon"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchPolygon.html"
---

# SketchPolygon Method (IModelDoc2)

Obsolete. Superseded by [ISketchManager::CreatePolygon](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~CreatePolygon.html).

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
Dim instance As IModelDoc2
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

- `XCenter`: X component of the polygon's center
- `YCenter`: Y component of the polygon's center
- `XEdge`: X component of the first vertex on the polygon
- `YEdge`: Y component of the first vertex on the polygon
- `NSides`: Number of sides for the polygon
- `BInscribed`: True to show an inscribed construction circle, false to show a circumscribed construction circle

### Return Value

True if polygon created, false if not

## VBA Syntax

See [ModelDoc2::SketchPolygon](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SketchPolygon.html).

## Remarks

After using this method, the PropertyManager page is in edit mode for the polygon. To exit this PropertyManager page and complete the operation, use [IModelDoc2::SetPickMode](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetPickMode.html), [IModelDoc2::ClearSelection2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ClearSelection2.html), or exit the sketch.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
