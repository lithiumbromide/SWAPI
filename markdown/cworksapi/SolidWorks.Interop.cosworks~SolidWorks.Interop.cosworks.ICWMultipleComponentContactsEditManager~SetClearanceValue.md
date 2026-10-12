---
title: "SetClearanceValue Method (ICWMultipleComponentContactsEditManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMultipleComponentContactsEditManager"
member: "SetClearanceValue"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~SetClearanceValue.html"
---

# SetClearanceValue Method (ICWMultipleComponentContactsEditManager)

Sets the maximum clearance between non-touching faces or shell edges.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetClearanceValue( _
   ByVal DMaxGap As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMultipleComponentContactsEditManager
Dim DMaxGap As System.Double
Dim value As System.Integer

value = instance.SetClearanceValue(DMaxGap)
```

### C#

```csharp
System.int SetClearanceValue(
   System.double DMaxGap
)
```

### C++/CLI

```cpp
System.int SetClearanceValue(
   System.double DMaxGap
)
```

### Parameters

- `DMaxGap`: Maximum clearance

### Return Value

Error code as defined in [swsMultipleContactsEditErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMultipleContactsEditErrorCode_e.html)

## VBA Syntax

See [CWMultipleComponentContactsEditManager::SetClearanceValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMultipleComponentContactsEditManager~SetClearanceValue.html).

## Remarks

This method is valid only if:

- [ICWMultipleComponentContactsEditManager::IncludeClearance](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~IncludeClearance.html)'s BNonTouching is set to 1,

- and -

- [ICWMultipleComponentContactsEditManager::SetContactType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~SetContactType.html)'s NType is set to [swsContactType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactType_e.html).swsContactTypeBonded.

## See Also

[ICWMultipleComponentContactsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager.html)
[ICWMultipleComponentContactsEditManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager_members.html)
[ICWMultipleComponentContactsEditManager::IncludeShellEdgeSolidOrShellFace Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~IncludeShellEdgeSolidOrShellFace.html)
[ICWMultipleComponentContactsEditManager::SetClearanceUnit Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~SetClearanceUnit.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
