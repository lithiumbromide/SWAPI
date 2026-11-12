---
title: "UnabsorbedSketches Property (IMirrorPartFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorPartFeatureData"
member: "UnabsorbedSketches"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData~UnabsorbedSketches.html"
---

# UnabsorbedSketches Property (IMirrorPartFeatureData)

Gets or sets whether to import unabsorbed sketches.

## Syntax

### Visual Basic (Declaration)

```vb
Property UnabsorbedSketches As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorPartFeatureData
Dim value As System.Boolean

instance.UnabsorbedSketches = value

value = instance.UnabsorbedSketches
```

### C#

```csharp
System.bool UnabsorbedSketches {get; set;}
```

### C++/CLI

```cpp
property System.bool UnabsorbedSketches {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to import unabsorbed sketches, false to not

## VBA Syntax

See [MirrorPartFeatureData::UnabsorbedSketches](ms-its:sldworksapivb6.chm::/sldworks~MirrorPartFeatureData~UnabsorbedSketches.html).

## See Also

[IMirrorPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData.html)
[IMirrorPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData_members.html)
[IMirrorPartFeatureData::AbsorbedSketches Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData~AbsorbedSketches.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
