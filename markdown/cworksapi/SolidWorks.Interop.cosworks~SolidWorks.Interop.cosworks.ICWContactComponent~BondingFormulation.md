---
title: "BondingFormulation Property (ICWContactComponent)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactComponent"
member: "BondingFormulation"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~BondingFormulation.html"
---

# BondingFormulation Property (ICWContactComponent)

Sets the bonding formulation for this contact.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property BondingFormulation As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactComponent

instance.BondingFormulation = value
```

### C#

```csharp
System.int BondingFormulation {set;}
```

### C++/CLI

```cpp
property System.int BondingFormulation {
   void set (    System.int value);
}
```

### Property Value

Option for

- no penetration ([static](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWStaticStudyOptions.html) and [nonlinear](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWNonLinearStudyOptions.html) studies only) advanced options as defined in [swsNoPenetrationOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsNoPenetrationOption_e.html) (except swsNoPenetrationOptionNodeToNode)
- thermal resistance ([thermal](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions.html) studies only) advanced options as defined in [swsNoPenetrationOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsNoPenetrationOption_e.html) (except swsNoPenetrationOptionNodeToNode)
- shrink fit (static and nonlinear studies only) advanced options as defined in [swsShrinkFitOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsShrinkFitOption_e.html)

## VBA Syntax

See [CWContactComponent::BondingFormulation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactComponent~BondingFormulation.html).

## Remarks

This property is valid only for selected components that behave during simulation as if they were welded.

For more information, see **SOLIDWORKS user-interface Help > Simulation > Interaction Options >**:

- **Component Interaction PropertyManager**

- and -

- **Types of Interactions > Bonded Interaction**

## See Also

[ICWContactComponent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent.html)
[ICWContactComponent Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent_members.html)

## Availability

SOLIDWORKS Simulation API 2022 SP1
