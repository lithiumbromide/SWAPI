---
title: "D2DraftAngle Property (ISurfExtrudeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfExtrudeFeatureData"
member: "D2DraftAngle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~D2DraftAngle.html"
---

# D2DraftAngle Property (ISurfExtrudeFeatureData)

Gets or sets the angle of the draft of this extruded surface in Direction 2.

## Syntax

### Visual Basic (Declaration)

```vb
Property D2DraftAngle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfExtrudeFeatureData
Dim value As System.Double

instance.D2DraftAngle = value

value = instance.D2DraftAngle
```

### C#

```csharp
System.double D2DraftAngle {get; set;}
```

### C++/CLI

```cpp
property System.double D2DraftAngle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Draft angle in Direction 2 (see **Remarks**)

## VBA Syntax

See [SurfExtrudeFeatureData::D2DraftAngle](ms-its:sldworksapivb6.chm::/sldworks~SurfExtrudeFeatureData~D2DraftAngle.html).

## Examples

See the [ISurfExtrudeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.html) examples.

## Remarks

This property is only available if:

- [ISurfExtrudeFeatureData::BothDirections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~BothDirections.html) = true.
- [ISurfExtrudeFeatureData::D2DraftOn](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~D2DraftOn.html) = true.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.html)
[ISurfExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData_members.html)
[ISurfExtrudeFeatureData::D2DraftOutward Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~D2DraftOutward.html)
[ISurfExtrudeFeatureData::D1DraftAngle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~D1DraftAngle.html)
[ISurfExtrudeFeatureData::D2CapEnd Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~D2CapEnd.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
