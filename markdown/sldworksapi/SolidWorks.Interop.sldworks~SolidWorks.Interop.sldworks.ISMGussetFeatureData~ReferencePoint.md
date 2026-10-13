---
title: "ReferencePoint Property (ISMGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISMGussetFeatureData"
member: "ReferencePoint"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ReferencePoint.html"
---

# ReferencePoint Property (ISMGussetFeatureData)

Gets or sets a position reference for this gusset.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReferencePoint As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISMGussetFeatureData
Dim value As System.Object

instance.ReferencePoint = value

value = instance.ReferencePoint
```

### C#

```csharp
System.object ReferencePoint {get; set;}
```

### C++/CLI

```cpp
property System.Object^ ReferencePoint {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Point (e.g., [vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html), [sketch point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html), or [reference point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPoint.html)) where to position this gusset

## VBA Syntax

See [SMGussetFeatureData::ReferencePoint](ms-its:sldworksapivb6.chm::/sldworks~SMGussetFeatureData~ReferencePoint.html).

## Examples

See the [IFeatureManager::InsertSheetMetalGussetFeature3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalGussetFeature3.html) examples.

## Remarks

If you do not set this property, you must set [ISMGussetFeatureData::UseOffset](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData~UseOffset.html) and [ISMGussetFeatureData::OffsetDistance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData~OffsetDistance.html) to offset the gusset from an assumed reference point. For insertion of the first gusset, the assumed reference point is on the end of the sheet metal bend. For second and subsequent gusset insertions, the assumed reference point is on the edge of the gusset last inserted.

See the [ISMGussetFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html) Remarks.

## See Also

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html)
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.html)
[ISMGussetFeatureData::ReferenceLine Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ReferenceLine.html)
[ISMGussetFeatureData::SupportingFaces Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~SupportingFaces.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
