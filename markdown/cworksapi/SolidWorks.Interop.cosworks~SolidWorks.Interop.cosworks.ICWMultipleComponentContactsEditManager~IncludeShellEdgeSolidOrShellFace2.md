---
title: "IncludeShellEdgeSolidOrShellFace2 Method (ICWMultipleComponentContactsEditManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMultipleComponentContactsEditManager"
member: "IncludeShellEdgeSolidOrShellFace2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~IncludeShellEdgeSolidOrShellFace2.html"
---

# IncludeShellEdgeSolidOrShellFace2 Method (ICWMultipleComponentContactsEditManager)

Sets whether to create edge-to-edge bonded contact sets.

## Syntax

### Visual Basic (Declaration)

```vb
Function IncludeShellEdgeSolidOrShellFace2( _
   ByVal BNonTouchingShell As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMultipleComponentContactsEditManager
Dim BNonTouchingShell As System.Boolean
Dim value As System.Integer

value = instance.IncludeShellEdgeSolidOrShellFace2(BNonTouchingShell)
```

### C#

```csharp
System.int IncludeShellEdgeSolidOrShellFace2(
   System.bool BNonTouchingShell
)
```

### C++/CLI

```cpp
System.int IncludeShellEdgeSolidOrShellFace2(
   System.bool BNonTouchingShell
)
```

### Parameters

- `BNonTouchingShell`: -1 or true to create edge-to-edge bonded contact sets, 0 or false to not

### Return Value

Error code as defined in [swsMultipleContactsEditErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMultipleContactsEditErrorCode_e.html)

## VBA Syntax

See [CWMultipleComponentContactsEditManager::IncludeShellEdgeSolidOrShellFace2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMultipleComponentContactsEditManager~IncludeShellEdgeSolidOrShellFace2.html).

## See Also

[ICWMultipleComponentContactsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager.html)
[ICWMultipleComponentContactsEditManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager_members.html)

## Availability

SOLIDWORKS Simulation API 2022 SP0
