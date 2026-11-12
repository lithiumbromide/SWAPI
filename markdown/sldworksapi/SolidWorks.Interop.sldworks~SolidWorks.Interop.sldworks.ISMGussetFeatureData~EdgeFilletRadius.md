---
title: "EdgeFilletRadius Property (ISMGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISMGussetFeatureData"
member: "EdgeFilletRadius"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~EdgeFilletRadius.html"
---

# EdgeFilletRadius Property (ISMGussetFeatureData)

Gets or sets the fillet radius of edges in this flat-back gusset.

## Syntax

### Visual Basic (Declaration)

```vb
Property EdgeFilletRadius As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISMGussetFeatureData
Dim value As System.Double

instance.EdgeFilletRadius = value

value = instance.EdgeFilletRadius
```

### C#

```csharp
System.double EdgeFilletRadius {get; set;}
```

### C++/CLI

```cpp
property System.double EdgeFilletRadius {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Gusset edge fillet radius

## VBA Syntax

See [SMGussetFeatureData::EdgeFilletRadius](ms-its:sldworksapivb6.chm::/sldworks~SMGussetFeatureData~EdgeFilletRadius.html).

## Remarks

This property is valid only if [ISMGussetFeatureData::FilletGussetEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData~FilletGussetEdges.html) is true and [ISMGussetFeatureData::GussetType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData~GussetType.html) is set to 1.

## See Also

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html)
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
