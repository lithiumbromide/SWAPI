---
title: "SetContactType Method (ICWMultipleContactSetsEditManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMultipleContactSetsEditManager"
member: "SetContactType"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetContactType.html"
---

# SetContactType Method (ICWMultipleContactSetsEditManager)

Sets the type of the contact sets to edit.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetContactType( _
   ByVal NType As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMultipleContactSetsEditManager
Dim NType As System.Integer
Dim value As System.Integer

value = instance.SetContactType(NType)
```

### C#

```csharp
System.int SetContactType(
   System.int NType
)
```

### C++/CLI

```cpp
System.int SetContactType(
   System.int NType
)
```

### Parameters

- `NType`: Type of contact set for:

  - [static](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWStaticStudyOptions.html) and [nonlinear](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWNonLinearStudyOptions.html) studies as defined in [swsContactSetTypeStaticNonLinear_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsContactSetTypeStaticNonLinear_e.html)
  - [thermal](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWThermalStudyOptions.html) studies as defined in [swsContactSetTypeThermal_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsContactSetTypeThermal_e.html)
  - [buckling](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBucklingStudyOptions.html) and [frequency](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWFrequencyStudyOptions.html) studies as defined [swsContactType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsContactType_e.html), excluding swsContactTypeStaticNoPenetration

### Return Value

Error code as defined in [swsMultipleContactsEditErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMultipleContactsEditErrorCode_e.html)

## VBA Syntax

See [CWMultipleContactSetsEditManager::SetContactType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMultipleContactSetsEditManager~SetContactType.html).

## Examples

See the [ICWMultipleContactSetsEditManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager.html) examples.

## Remarks

See the SOLIDWORKS Simulation Help for guidelines about studies with contact conditions.

## See Also

[ICWMultipleContactSetsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager.html)
[ICWMultipleContactSetsEditManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
