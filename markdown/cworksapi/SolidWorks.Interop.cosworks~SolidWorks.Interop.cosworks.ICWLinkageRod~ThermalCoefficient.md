---
title: "ThermalCoefficient Property (ICWLinkageRod)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLinkageRod"
member: "ThermalCoefficient"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod~ThermalCoefficient.html"
---

# ThermalCoefficient Property (ICWLinkageRod)

Sets the thermal expansion coefficient for the custom material of this linkage rod connector.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property ThermalCoefficient As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLinkageRod

instance.ThermalCoefficient = value
```

### C#

```csharp
System.double ThermalCoefficient {set;}
```

### C++/CLI

```cpp
property System.double ThermalCoefficient {
   void set (    System.double value);
}
```

### Property Value

0.0 <= Thermal expansion coefficient /Kelvin <= 1000000000000000042420637374017961984.0

## VBA Syntax

See [CWLinkageRod::ThermalCoefficient](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLinkageRod~ThermalCoefficient.html).

## Remarks

This property is valid only if [ICWLinkageRod::MaterialSource](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod~MaterialSource.html) is set to [swsMaterialSourceType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMaterialSourceType_e.html).swsMaterial_Custom.

## See Also

[ICWLinkageRod Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod.html)
[ICWLinkageRod Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod_members.html)

## Availability

SOLIDWORKS Simulation API 2022 SP0
