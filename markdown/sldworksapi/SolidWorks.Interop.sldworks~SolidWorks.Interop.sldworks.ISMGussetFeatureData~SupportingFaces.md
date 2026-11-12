---
title: "SupportingFaces Property (ISMGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISMGussetFeatureData"
member: "SupportingFaces"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~SupportingFaces.html"
---

# SupportingFaces Property (ISMGussetFeatureData)

Gets or sets the legs of this gusset.

## Syntax

### Visual Basic (Declaration)

```vb
Property SupportingFaces As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISMGussetFeatureData
Dim value As System.Object

instance.SupportingFaces = value

value = instance.SupportingFaces
```

### C#

```csharp
System.object SupportingFaces {get; set;}
```

### C++/CLI

```cpp
property System.Object^ SupportingFaces {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of one or two [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) to which this gusset is attached

## VBA Syntax

See [SMGussetFeatureData::SupportingFaces](ms-its:sldworksapivb6.chm::/sldworks~SMGussetFeatureData~SupportingFaces.html).

## Examples

See the [IFeatureManager::InsertSheetMetalGussetFeature3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalGussetFeature3.html) examples.

## Remarks

See the [ISMGussetFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html) Remarks.

## See Also

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html)
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.html)
[ISMGussetFeatureData::ReferenceLine Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ReferenceLine.html)
[ISMGussetFeatureData::ReferencePoint Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ReferencePoint.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
