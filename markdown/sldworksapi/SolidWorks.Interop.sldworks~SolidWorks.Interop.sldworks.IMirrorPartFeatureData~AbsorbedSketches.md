---
title: "AbsorbedSketches Property (IMirrorPartFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorPartFeatureData"
member: "AbsorbedSketches"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData~AbsorbedSketches.html"
---

# AbsorbedSketches Property (IMirrorPartFeatureData)

Gets or sets whether to import absorbed sketches.

## Syntax

### Visual Basic (Declaration)

```vb
Property AbsorbedSketches As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorPartFeatureData
Dim value As System.Boolean

instance.AbsorbedSketches = value

value = instance.AbsorbedSketches
```

### C#

```csharp
System.bool AbsorbedSketches {get; set;}
```

### C++/CLI

```cpp
property System.bool AbsorbedSketches {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to import absorbed sketches, false to not

## VBA Syntax

See [MirrorPartFeatureData::AbsorbedSketches](ms-its:sldworksapivb6.chm::/sldworks~MirrorPartFeatureData~AbsorbedSketches.html).

## See Also

[IMirrorPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData.html)
[IMirrorPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData_members.html)
[IMirrorPartFeatureData::UnabsorbedSketches Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData~UnabsorbedSketches.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
