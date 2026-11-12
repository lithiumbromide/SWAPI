---
title: "SetBondingFormulation Method (ICWMultipleComponentContactsEditManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMultipleComponentContactsEditManager"
member: "SetBondingFormulation"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~SetBondingFormulation.html"
---

# SetBondingFormulation Method (ICWMultipleComponentContactsEditManager)

Sets the specified bonding formulation for all component contacts.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetBondingFormulation( _
   ByVal NType As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMultipleComponentContactsEditManager
Dim NType As System.Integer
Dim value As System.Integer

value = instance.SetBondingFormulation(NType)
```

### C#

```csharp
System.int SetBondingFormulation(
   System.int NType
)
```

### C++/CLI

```cpp
System.int SetBondingFormulation(
   System.int NType
)
```

### Parameters

- `NType`: Option for

  - no penetration ([static](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWStaticStudyOptions.html) and [nonlinear](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWNonLinearStudyOptions.html) studies only) advanced options as defined in [swsNoPenetrationOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsNoPenetrationOption_e.html) (except swsNoPenetrationOptionNodeToNode)
  - thermal resistance ([thermal](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions.html) studies only) advanced options as defined in [swsNoPenetrationOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsNoPenetrationOption_e.html) (except swsNoPenetrationOptionNodeToNode)
  - shrink fit (static and nonlinear studies only) advanced options as defined in [swsShrinkFitOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsShrinkFitOption_e.html)

### Return Value

Error code as defined in [swsMultipleContactsEditErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMultipleContactsEditErrorCode_e.html)

## VBA Syntax

See [CWMultipleComponentContactsEditManager::SetBondingFormulation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMultipleComponentContactsEditManager~SetBondingFormulation.html).

## Remarks

This method is valid only for selected components that behave during simulation as if they were welded.

For more information, see **SOLIDWORKS user-interface Help > Simulation > Interaction Options >**:

- **Component Interaction PropertyManager**

- and -

- **Types of Interactions > Bonded Interaction**

## See Also

[ICWMultipleComponentContactsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager.html)
[ICWMultipleComponentContactsEditManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager_members.html)

## Availability

SOLIDWORKS Simulation API 2022 SP1
