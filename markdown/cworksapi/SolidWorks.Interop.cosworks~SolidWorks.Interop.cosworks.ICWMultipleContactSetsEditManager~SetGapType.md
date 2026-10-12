---
title: "SetGapType Method (ICWMultipleContactSetsEditManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMultipleContactSetsEditManager"
member: "SetGapType"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetGapType.html"
---

# SetGapType Method (ICWMultipleContactSetsEditManager)

Sets the gap type of the contact sets to edit.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetGapType( _
   ByVal NGapType As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMultipleContactSetsEditManager
Dim NGapType As System.Integer
Dim value As System.Integer

value = instance.SetGapType(NGapType)
```

### C#

```csharp
System.int SetGapType(
   System.int NGapType
)
```

### C++/CLI

```cpp
System.int SetGapType(
   System.int NGapType
)
```

### Parameters

- `NGapType`: Type of gap as defined in [swsGapType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsGapType_e.html)SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactSet~ClearanceValue.html

### Return Value

Error code as defined in [swsMultipleContactsEditErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMultipleContactsEditErrorCode_e.html)

## VBA Syntax

See [CWMultipleContactSetsEditManager::SetGapType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMultipleContactSetsEditManager~SetGapType.html).

## Remarks

This property is valid only if [ICWMultipleContactSetsEditManager::SetContactType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~SetContactType.html) is:

- [swsContactSetTypeStaticNonLinear_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactSetTypeStaticNonLinear_e.html).swsContactSetTypeStaticNonLinearVirtualWall

- or -

- swsContactSetTypeStaticNonLinear_e.swsContactSetTypeStaticNonLinearNoPenetration

## See Also

[ICWMultipleContactSetsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager.html)
[ICWMultipleContactSetsEditManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
