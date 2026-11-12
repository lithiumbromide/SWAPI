---
title: "IInsertSketchForEdgeFlange Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IInsertSketchForEdgeFlange"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IInsertSketchForEdgeFlange.html"
---

# IInsertSketchForEdgeFlange Method (IModelDoc2)

Inserts a sketch for [IFeatureManager::InsertSheetMetalEdgeFlange2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertSheetMetalEdgeFlange2.html) in this sheet metal part.

## Syntax

### Visual Basic (Declaration)

```vb
Function IInsertSketchForEdgeFlange( _
   ByVal FlangeEdge As Edge, _
   ByVal DAngle As System.Double, _
   ByVal FlipDir As System.Boolean _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim FlangeEdge As Edge
Dim DAngle As System.Double
Dim FlipDir As System.Boolean
Dim value As Feature

value = instance.IInsertSketchForEdgeFlange(FlangeEdge, DAngle, FlipDir)
```

### C#

```csharp
Feature IInsertSketchForEdgeFlange(
   Edge FlangeEdge,
   System.double DAngle,
   System.bool FlipDir
)
```

### C++/CLI

```cpp
Feature^ IInsertSketchForEdgeFlange(
   Edge^ FlangeEdge,
   System.double DAngle,
   System.bool FlipDir
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FlangeEdge`: Edge to which to apply flange
- `DAngle`: Angle of flange
- `FlipDir`: True reverses the offset direction of the flange, false does not

### Return Value

Sketch for the edge flagne, returned as a [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [ModelDoc2::IInsertSketchForEdgeFlange](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~IInsertSketchForEdgeFlange.html).

## Remarks

After calling this method, you must create the profile for the flange on the appropriate plane. After creating the profile, call [IFeatureManager::InsertSheetMetalEdgeFlange2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertSheetMetalEdgeFlange2.html) to create the flange.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::InsertSheetMetalMiterFlange Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSheetMetalMiterFlange.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
