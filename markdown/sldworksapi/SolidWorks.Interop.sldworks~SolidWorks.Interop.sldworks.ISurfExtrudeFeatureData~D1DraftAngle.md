---
title: "D1DraftAngle Property (ISurfExtrudeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfExtrudeFeatureData"
member: "D1DraftAngle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~D1DraftAngle.html"
---

# D1DraftAngle Property (ISurfExtrudeFeatureData)

Gets or sets the angle of the draft of this extruded surface in Direction 1.

## Syntax

### Visual Basic (Declaration)

```vb
Property D1DraftAngle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfExtrudeFeatureData
Dim value As System.Double

instance.D1DraftAngle = value

value = instance.D1DraftAngle
```

### C#

```csharp
System.double D1DraftAngle {get; set;}
```

### C++/CLI

```cpp
property System.double D1DraftAngle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Draft angle in Direction 1 (see **Remarks**)

## VBA Syntax

See [SurfExtrudeFeatureData::D1DraftAngle](ms-its:sldworksapivb6.chm::/sldworks~SurfExtrudeFeatureData~D1DraftAngle.html).

## Examples

See the [ISurfExtrudeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.html) examples.

## Remarks

This property is only available if [ISurfExtrudeFeatureData::D1DraftOn](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~D1DraftOn.html) = true.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.html)
[ISurfExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData_members.html)
[ISurfExtrudeFeatureData::D1DraftOutward Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~D1DraftOutward.html)
[ISurfExtrudeFeatureData::BothDirections Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~BothDirections.html)
[ISurfExtrudeFeatureData::D1CapEnd Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~D1CapEnd.html)
[ISurfExtrudeFeatureData::D2DraftAngle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~D2DraftAngle.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
