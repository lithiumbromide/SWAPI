---
title: "SetResistanceValue Method (ICWMultipleContactSetsEditManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMultipleContactSetsEditManager"
member: "SetResistanceValue"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetResistanceValue.html"
---

# SetResistanceValue Method (ICWMultipleContactSetsEditManager)

Sets the thermal resistance value for the contact sets to edit.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetResistanceValue( _
   ByVal DResistanceValue As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMultipleContactSetsEditManager
Dim DResistanceValue As System.Double
Dim value As System.Integer

value = instance.SetResistanceValue(DResistanceValue)
```

### C#

```csharp
System.int SetResistanceValue(
   System.double DResistanceValue
)
```

### C++/CLI

```cpp
System.int SetResistanceValue(
   System.double DResistanceValue
)
```

### Parameters

- `DResistanceValue`: Thermal resistance value

### Return Value

Error code as defined in [swsMultipleContactsEditErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMultipleContactsEditErrorCode_e.html)

## VBA Syntax

See [CWMultipleContactSetsEditManager::SetResistanceValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMultipleContactSetsEditManager~SetResistanceValue.html).

## Remarks

This property is valid only for thermal studies and if [ICWMultipleContactSetsEditManager::SetContactType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetContactType.html) sets [swsContactSetTypeThermal_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactSetTypeThermal_e.html).swsContactSetTypeThermalResistance.

## See Also

[ICWMultipleContactSetsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager.html)
[ICWMultipleContactSetsEditManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager_members.html)
[ICWMultipleContactSetsEditManager::SetResistanceType Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetResistanceType.html)
[ICWMultipleContactSetsEditManager::SetResistanceUnitSystem Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetResistanceUnitSystem.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
