---
title: "SetResistanceType Method (ICWMultipleContactSetsEditManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMultipleContactSetsEditManager"
member: "SetResistanceType"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetResistanceType.html"
---

# SetResistanceType Method (ICWMultipleContactSetsEditManager)

Sets the thermal resistance type for the contact sets to edit.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetResistanceType( _
   ByVal NResistanceType As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMultipleContactSetsEditManager
Dim NResistanceType As System.Integer
Dim value As System.Integer

value = instance.SetResistanceType(NResistanceType)
```

### C#

```csharp
System.int SetResistanceType(
   System.int NResistanceType
)
```

### C++/CLI

```cpp
System.int SetResistanceType(
   System.int NResistanceType
)
```

### Parameters

- `NResistanceType`: Thermal resistance type as defined in [swsResistanceType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResistanceType_e.html)

### Return Value

Error code as defined in [swsMultipleContactsEditErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMultipleContactsEditErrorCode_e.html)

## VBA Syntax

See [CWMultipleContactSetsEditManager::SetResistanceType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMultipleContactSetsEditManager~SetResistanceType.html).

## Remarks

This property is valid only for thermal studies and if [ICWMultipleContactSetsEditManager::SetContactType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetContactType.html) sets [swsContactSetTypeThermal_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactSetTypeThermal_e.html).swsContactSetTypeThermalResistance.

## See Also

[ICWMultipleContactSetsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager.html)
[ICWMultipleContactSetsEditManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager_members.html)
[ICWMultipleContactSetsEditManager::SetResistanceUnitSystem Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetResistanceUnitSystem.html)
[ICWMultipleContactSetsEditManager::SetResistanceValue Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetResistanceValue.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
