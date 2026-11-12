---
title: "YoungsModulus Property (ICWLinkageRod)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLinkageRod"
member: "YoungsModulus"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod~YoungsModulus.html"
---

# YoungsModulus Property (ICWLinkageRod)

Sets Young's Modulus for the custom material of this linkage rod connector.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property YoungsModulus As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLinkageRod

instance.YoungsModulus = value
```

### C#

```csharp
System.double YoungsModulus {set;}
```

### C++/CLI

```cpp
property System.double YoungsModulus {
   void set (    System.double value);
}
```

### Property Value

0.0 <= Young's Modulus in N/m^2 <= 1000000000000000042420637374017961984.0

## VBA Syntax

See [CWLinkageRod::YoungsModulus](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLinkageRod~YoungsModulus.html).

## Remarks

This property is valid only if [ICWLinkageRod::MaterialSource](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod~MaterialSource.html) is set to [swsMaterialSourceType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMaterialSourceType_e.html).swsMaterial_Custom.

## See Also

[ICWLinkageRod Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod.html)
[ICWLinkageRod Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod_members.html)

## Availability

SOLIDWORKS Simulation API 2022 SP0
