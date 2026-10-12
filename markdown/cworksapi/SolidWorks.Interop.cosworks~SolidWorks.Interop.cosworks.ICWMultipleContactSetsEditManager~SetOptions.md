---
title: "SetOptions Method (ICWMultipleContactSetsEditManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMultipleContactSetsEditManager"
member: "SetOptions"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetOptions.html"
---

# SetOptions Method (ICWMultipleContactSetsEditManager)

Sets the advanced options for the contact sets to edit.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetOptions( _
   ByVal NOptions As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMultipleContactSetsEditManager
Dim NOptions As System.Integer
Dim value As System.Integer

value = instance.SetOptions(NOptions)
```

### C#

```csharp
System.int SetOptions(
   System.int NOptions
)
```

### C++/CLI

```cpp
System.int SetOptions(
   System.int NOptions
)
```

### Parameters

- `NOptions`: Option for

  - no penetration ([static](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWStaticStudyOptions.html) and [nonlinear](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWNonLinearStudyOptions.html) studies only) advanced options as defined in [swsNoPenetrationOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsNoPenetrationOption_e.html)
  - thermal resistance ([thermal](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions.html) studies only) advanced options as defined in [swsNoPenetrationOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsNoPenetrationOption_e.html) (except swsNoPenetrationOptionNodeToNode)
  - shrink fit (static and nonlinear studies only) advanced options as defined in [swsShrinkFitOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsShrinkFitOption_e.html)

### Return Value

Error code as defined in [swsMultipleContactsEditErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMultipleContactsEditErrorCode_e.html)

## VBA Syntax

See [CWMultipleContactSetsEditManager::SetOptions](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMultipleContactSetsEditManager~SetOptions.html).

## See Also

[ICWMultipleContactSetsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager.html)
[ICWMultipleContactSetsEditManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
