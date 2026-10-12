---
title: "InsertSketchForEdgeFlange Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertSketchForEdgeFlange"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSketchForEdgeFlange.html"
---

# InsertSketchForEdgeFlange Method (IModelDoc2)

Inserts a profile sketch of an edge flange in this sheet metal part.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertSketchForEdgeFlange( _
   ByVal FlangeEdge As System.Object, _
   ByVal DAngle As System.Double, _
   ByVal FlipDir As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim FlangeEdge As System.Object
Dim DAngle As System.Double
Dim FlipDir As System.Boolean
Dim value As System.Object

value = instance.InsertSketchForEdgeFlange(FlangeEdge, DAngle, FlipDir)
```

### C#

```csharp
System.object InsertSketchForEdgeFlange(
   System.object FlangeEdge,
   System.double DAngle,
   System.bool FlipDir
)
```

### C++/CLI

```cpp
System.Object^ InsertSketchForEdgeFlange(
   System.Object^ FlangeEdge,
   System.double DAngle,
   System.bool FlipDir
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FlangeEdge`: Edge with which to create an edge flange
- `DAngle`: Angle of flange
- `FlipDir`: True reverses the offset direction of the flange, false does not

### Return Value

Sketch for the edge flange, returned as a [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [ModelDoc2::InsertSketchForEdgeFlange](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertSketchForEdgeFlange.html).

## Examples

See the [IEdgeFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html) examples.

## Remarks

After calling this method, you must create the profile for the flange on the appropriate plane. Then use [IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.html), [IEdgeFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html), and [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.html) to create the edge flange.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
