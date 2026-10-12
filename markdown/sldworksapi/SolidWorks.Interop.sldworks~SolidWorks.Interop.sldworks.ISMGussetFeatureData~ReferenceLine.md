---
title: "ReferenceLine Property (ISMGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISMGussetFeatureData"
member: "ReferenceLine"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ReferenceLine.html"
---

# ReferenceLine Property (ISMGussetFeatureData)

Gets or sets the orientation reference for this gusset's section plane.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReferenceLine As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISMGussetFeatureData
Dim value As System.Object

instance.ReferenceLine = value

value = instance.ReferenceLine
```

### C#

```csharp
System.object ReferenceLine {get; set;}
```

### C++/CLI

```cpp
property System.Object^ ReferenceLine {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Line (e.g., [edge,](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html) [co-Edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge.html), or [sketch segment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html)) that is perpendicular to this gusset's section plane

## VBA Syntax

See [SMGussetFeatureData::ReferenceLine](ms-its:sldworksapivb6.chm::/sldworks~SMGussetFeatureData~ReferenceLine.html).

## Examples

See the [IFeatureManager::InsertSheetMetalGussetFeature3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalGussetFeature3.html) examples.

## Remarks

If you do not set this property, the assumed reference line is the bend line adjacent to the entities in [ISMGussetFeatureData::SupportingFaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData~SupportingFaces.html).

See the [ISMGussetFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html) Remarks.

## See Also

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html)
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.html)
[ISMGussetFeatureData::ReferencePoint Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ReferencePoint.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
