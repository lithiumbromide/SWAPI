---
title: "GetComponentAt Method (ICWSolidManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSolidManager"
member: "GetComponentAt"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidManager~GetComponentAt.html"
---

# GetComponentAt Method (ICWSolidManager)

Gets the solid component at the specified index.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetComponentAt( _
   ByVal NIndex As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As CWSolidComponent
```

### Visual Basic (Usage)

```vb
Dim instance As ICWSolidManager
Dim NIndex As System.Integer
Dim ErrorCode As System.Integer
Dim value As CWSolidComponent

value = instance.GetComponentAt(NIndex, ErrorCode)
```

### C#

```csharp
CWSolidComponent GetComponentAt(
   System.int NIndex,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWSolidComponent^ GetComponentAt(
   System.int NIndex,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NIndex`: 0-based index of the solid component to get
- `ErrorCode`: 0 if successful, 1 if no solid component at NIndex

### Return Value

[Solid component](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWSolidComponent.html) or NULL if no solid component at NIndex

## VBA Syntax

See [CWSolidManager::GetComponentAt](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWSolidManager~GetComponentAt.html).

## Examples

See the [ICWSolidManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidManager.html) examples.

## Remarks

Before calling this method, call [ICWSolidManager::ComponentCount](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWSolidManager~ComponentCount.html) to get NIndex. Index starts at 0.

## See Also

[ICWSolidManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidManager.html)
[ICWSolidManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidManager_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
