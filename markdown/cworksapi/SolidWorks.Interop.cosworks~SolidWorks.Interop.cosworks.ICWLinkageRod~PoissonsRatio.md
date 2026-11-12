---
title: "PoissonsRatio Property (ICWLinkageRod)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLinkageRod"
member: "PoissonsRatio"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod~PoissonsRatio.html"
---

# PoissonsRatio Property (ICWLinkageRod)

Sets the Poisson's Ratio for the custom material of this linkage rod connector.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property PoissonsRatio As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLinkageRod

instance.PoissonsRatio = value
```

### C#

```csharp
System.double PoissonsRatio {set;}
```

### C++/CLI

```cpp
property System.double PoissonsRatio {
   void set (    System.double value);
}
```

### Property Value

0.0 <= Poisson's Ratio <= 1.0

## VBA Syntax

See [CWLinkageRod::PoissonsRatio](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLinkageRod~PoissonsRatio.html).

## Remarks

This property is valid only if [ICWLinkageRod::MaterialSource](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod~MaterialSource.html) is set to [swsMaterialSourceType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMaterialSourceType_e.html).swsMaterial_Custom.

## See Also

[ICWLinkageRod Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod.html)
[ICWLinkageRod Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod_members.html)

## Availability

SOLIDWORKS Simulation API 2022 SP0
