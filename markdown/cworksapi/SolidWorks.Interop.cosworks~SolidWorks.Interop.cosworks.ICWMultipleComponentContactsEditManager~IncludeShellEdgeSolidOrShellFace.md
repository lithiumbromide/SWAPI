---
title: "IncludeShellEdgeSolidOrShellFace Method (ICWMultipleComponentContactsEditManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMultipleComponentContactsEditManager"
member: "IncludeShellEdgeSolidOrShellFace"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~IncludeShellEdgeSolidOrShellFace.html"
---

# IncludeShellEdgeSolidOrShellFace Method (ICWMultipleComponentContactsEditManager)

Obsolete. Superseded by [ICWMultipleComponentContactsEditManager::IncludeShellEdgeSolidOrShellFace2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~IncludeShellEdgeSolidOrShellFace2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IncludeShellEdgeSolidOrShellFace( _
   ByVal BNonTouchingShell As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMultipleComponentContactsEditManager
Dim BNonTouchingShell As System.Integer
Dim value As System.Integer

value = instance.IncludeShellEdgeSolidOrShellFace(BNonTouchingShell)
```

### C#

```csharp
System.int IncludeShellEdgeSolidOrShellFace(
   System.int BNonTouchingShell
)
```

### C++/CLI

```cpp
System.int IncludeShellEdgeSolidOrShellFace(
   System.int BNonTouchingShell
)
```

### Parameters

- `BNonTouchingShell`: 1 to create edge-to-edge bonded contact sets, 0 to not

### Return Value

Error code as defined in [swsMultipleContactsEditErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMultipleContactsEditErrorCode_e.html)

## VBA Syntax

See [CWMultipleComponentContactsEditManager::IncludeShellEdgeSolidOrShellFace](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMultipleComponentContactsEditManager~IncludeShellEdgeSolidOrShellFace.html).

## Remarks

This method is valid only if:

- [ICWMultipleComponentContactsEditManager::IncludeClearance](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~IncludeClearance.html)'s BNonTouching is set to 1,

- and -

- [ICWMultipleComponentContactsEditManager::SetContactType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~SetContactType.html)'s NType is set to [swsContactType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactType_e.html).swsContactTypeBonded.

If BNonTouchingShell is set to true, then this method creates edge-to-edge bonded contact sets for pairs of:

- shell edges-to-shell edges,
- shell edges-to-shell faces, and
- shell edges-to-solid faces

that are within clearance as specified by [ICWMultipleComponentContactsEditManager::SetClearanceValue](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~SetClearanceValue.html).

## See Also

[ICWMultipleComponentContactsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager.html)
[ICWMultipleComponentContactsEditManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager_members.html)
**ICWMultipleComponentContactsEditManager::GetIncludeShellEdgeSolidOrShellFace Method ()**

## Availability

SOLIDWORKS Simulation API 2017 SP0
