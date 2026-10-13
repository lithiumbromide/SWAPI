---
title: "GussetType Property (ISMGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISMGussetFeatureData"
member: "GussetType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~GussetType.html"
---

# GussetType Property (ISMGussetFeatureData)

Gets or sets the type of this gusset.

## Syntax

### Visual Basic (Declaration)

```vb
Property GussetType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISMGussetFeatureData
Dim value As System.Integer

instance.GussetType = value

value = instance.GussetType
```

### C#

```csharp
System.int GussetType {get; set;}
```

### C++/CLI

```cpp
property System.int GussetType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of gusset as defined in [swSheetMetalRibGussetType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalRibGussetType_e.html)

## VBA Syntax

See [SMGussetFeatureData::GussetType](ms-its:sldworksapivb6.chm::/sldworks~SMGussetFeatureData~GussetType.html).

## Examples

See the examples for [ISMGussetFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData.html).

## See Also

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html)
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.html)
[ISMGussetFeatureData::EdgeFilletRadius Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~EdgeFilletRadius.html)
[ISMGussetFeatureData::FilletGussetEdges Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~FilletGussetEdges.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
