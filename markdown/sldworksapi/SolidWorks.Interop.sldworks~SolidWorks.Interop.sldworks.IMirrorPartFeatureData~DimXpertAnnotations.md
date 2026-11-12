---
title: "DimXpertAnnotations Property (IMirrorPartFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorPartFeatureData"
member: "DimXpertAnnotations"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData~DimXpertAnnotations.html"
---

# DimXpertAnnotations Property (IMirrorPartFeatureData)

Gets or sets whether to import DimXpert annotations.

## Syntax

### Visual Basic (Declaration)

```vb
Property DimXpertAnnotations As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorPartFeatureData
Dim value As System.Boolean

instance.DimXpertAnnotations = value

value = instance.DimXpertAnnotations
```

### C#

```csharp
System.bool DimXpertAnnotations {get; set;}
```

### C++/CLI

```cpp
property System.bool DimXpertAnnotations {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to import DimXpert annotations, false to not

## VBA Syntax

See [MirrorPartFeatureData::DimXpertAnnotations](ms-its:sldworksapivb6.chm::/sldworks~MirrorPartFeatureData~DimXpertAnnotations.html).

## See Also

[IMirrorPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData.html)
[IMirrorPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
