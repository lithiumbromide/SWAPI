---
title: "PropagateToTangentFaces Property (ISurfaceRadiateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceRadiateFeatureData"
member: "PropagateToTangentFaces"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData~PropagateToTangentFaces.html"
---

# PropagateToTangentFaces Property (ISurfaceRadiateFeatureData)

Gets or sets whether to propagate the tangent faces of this surface radiate feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PropagateToTangentFaces As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceRadiateFeatureData
Dim value As System.Boolean

instance.PropagateToTangentFaces = value

value = instance.PropagateToTangentFaces
```

### C#

```csharp
System.bool PropagateToTangentFaces {get; set;}
```

### C++/CLI

```cpp
property System.bool PropagateToTangentFaces {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True continues the surface to tangent faces, false does not continue the surface

## VBA Syntax

See [SurfaceRadiateFeatureData::PropagateToTangentFaces](ms-its:sldworksapivb6.chm::/sldworks~SurfaceRadiateFeatureData~PropagateToTangentFaces.html).

## Examples

See the [ISurfaceRadiateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfaceRadiateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData.html)
[ISurfaceRadiateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus SP2, Revision Number 10.2
