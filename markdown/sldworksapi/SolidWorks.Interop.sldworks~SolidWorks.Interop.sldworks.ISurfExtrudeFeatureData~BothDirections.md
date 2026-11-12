---
title: "BothDirections Property (ISurfExtrudeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfExtrudeFeatureData"
member: "BothDirections"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~BothDirections.html"
---

# BothDirections Property (ISurfExtrudeFeatureData)

Gets or sets whether this surface is extruded in both directions.

## Syntax

### Visual Basic (Declaration)

```vb
Property BothDirections As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfExtrudeFeatureData
Dim value As System.Boolean

instance.BothDirections = value

value = instance.BothDirections
```

### C#

```csharp
System.bool BothDirections {get; set;}
```

### C++/CLI

```cpp
property System.bool BothDirections {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True extrudes the surface in both directions, false does not

## VBA Syntax

See [SurfExtrudeFeatureData::BothDirections](ms-its:sldworksapivb6.chm::/sldworks~SurfExtrudeFeatureData~BothDirections.html).

## Examples

See the [ISurfExtrudeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.html)
[ISurfExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData_members.html)
[ISurfExtrudeFeatureData::D1CapEnd Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~D1CapEnd.html)
[ISurfExtrudeFeatureData::D1DraftAngle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~D1DraftAngle.html)
[ISurfExtrudeFeatureData::D1DraftOn Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~D1DraftOn.html)
[ISurfExtrudeFeatureData::D1DraftOutward Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~D1DraftOutward.html)
[ISurfExtrudeFeatureData::D2CapEnd Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~D2CapEnd.html)
[ISurfExtrudeFeatureData::D2DraftAngle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~D2DraftAngle.html)
[ISurfExtrudeFeatureData::D2DraftOn Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~D2DraftOn.html)
[ISurfExtrudeFeatureData::D2DraftOutward Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~D2DraftOutward.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
