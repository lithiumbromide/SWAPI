---
title: "D1DraftOutward Property (ISurfExtrudeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfExtrudeFeatureData"
member: "D1DraftOutward"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~D1DraftOutward.html"
---

# D1DraftOutward Property (ISurfExtrudeFeatureData)

Gets or sets whether to draft the extruded surface outward or inward in Direction 1.

## Syntax

### Visual Basic (Declaration)

```vb
Property D1DraftOutward As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfExtrudeFeatureData
Dim value As System.Boolean

instance.D1DraftOutward = value

value = instance.D1DraftOutward
```

### C#

```csharp
System.bool D1DraftOutward {get; set;}
```

### C++/CLI

```cpp
property System.bool D1DraftOutward {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to draft the extruded surface outward in Direction 1, false to draft the extruded surface inward in Direction 1 (see **Remarks**)

## VBA Syntax

See [SurfExtrudeFeatureData::D1DraftOutward](ms-its:sldworksapivb6.chm::/sldworks~SurfExtrudeFeatureData~D1DraftOutward.html).

## Examples

See the [ISurfExtrudeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.html) examples.

## Remarks

This property is only available if [ISurfExtrudeFeatureData::D1DraftOn](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~D1DraftOn.html) = true.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.html)
[ISurfExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData_members.html)
[ISurfExtrudeFeatureData::D1DraftAngle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~D1DraftAngle.html)
[ISurfExtrudeFeatureData::D1CapEnd Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~D1CapEnd.html)
[ISurfExtrudeFeatureData::BothDirections Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~BothDirections.html)
[ISurfExtrudeFeatureData::D1CapEnd Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~D1CapEnd.html)
[ISurfExtrudeFeatureData::D2DraftOutward Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~D2DraftOutward.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
