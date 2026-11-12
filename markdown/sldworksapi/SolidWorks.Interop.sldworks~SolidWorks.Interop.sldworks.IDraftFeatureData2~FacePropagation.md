---
title: "FacePropagation Property (IDraftFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IDraftFeatureData2"
member: "FacePropagation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~FacePropagation.html"
---

# FacePropagation Property (IDraftFeatureData2)

Gets or sets the face propagation for this draft feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property FacePropagation As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As IDraftFeatureData2
Dim value As System.Short

instance.FacePropagation = value

value = instance.FacePropagation
```

### C#

```csharp
System.short FacePropagation {get; set;}
```

### C++/CLI

```cpp
property System.short FacePropagation {
   System.short get();
   void set (    System.short value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Face propagation type as defined in [swDraftFacePropagationType](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDraftFacePropagationType_e.html)

## VBA Syntax

See [DraftFeatureData2::FacePropagation](ms-its:sldworksapivb6.chm::/sldworks~DraftFeatureData2~FacePropagation.html).

## See Also

[IDraftFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2.html)
[IDraftFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
