---
title: "SetResistanceUnitSystem Method (ICWMultipleContactSetsEditManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMultipleContactSetsEditManager"
member: "SetResistanceUnitSystem"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetResistanceUnitSystem.html"
---

# SetResistanceUnitSystem Method (ICWMultipleContactSetsEditManager)

Sets the units of thermal resistance for the contact sets to edit.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetResistanceUnitSystem( _
   ByVal NUnitSystem As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMultipleContactSetsEditManager
Dim NUnitSystem As System.Integer
Dim value As System.Integer

value = instance.SetResistanceUnitSystem(NUnitSystem)
```

### C#

```csharp
System.int SetResistanceUnitSystem(
   System.int NUnitSystem
)
```

### C++/CLI

```cpp
System.int SetResistanceUnitSystem(
   System.int NUnitSystem
)
```

### Parameters

- `NUnitSystem`: Unit system as defined in [swsUnitSystem_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsUnitSystem_e.html)

### Return Value

Error code as defined in [swsMultipleContactsEditErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMultipleContactsEditErrorCode_e.html)

## VBA Syntax

See [CWMultipleContactSetsEditManager::SetResistanceUnitSystem](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMultipleContactSetsEditManager~SetResistanceUnitSystem.html).

## Remarks

This property is valid only for thermal studies and if [ICWMultipleContactSetsEditManager::SetContactType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetContactType.html) sets [swsContactSetTypeThermal_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactSetTypeThermal_e.html).swsContactSetTypeThermalResistance.

## See Also

[ICWMultipleContactSetsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager.html)
[ICWMultipleContactSetsEditManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager_members.html)
[ICWMultipleContactSetsEditManager::SetResistanceType Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetResistanceType.html)
[ICWMultipleContactSetsEditManager::SetResistanceValue Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetResistanceValue.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
