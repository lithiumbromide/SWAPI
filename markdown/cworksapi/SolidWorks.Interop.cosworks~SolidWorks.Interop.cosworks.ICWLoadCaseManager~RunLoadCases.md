---
title: "RunLoadCases Method (ICWLoadCaseManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadCaseManager"
member: "RunLoadCases"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~RunLoadCases.html"
---

# RunLoadCases Method (ICWLoadCaseManager)

Runs the analysis using primary load cases, primary load case combinations, or both.

## Syntax

### Visual Basic (Declaration)

```vb
Function RunLoadCases( _
   ByVal BPrimaryLoadCases As System.Boolean, _
   ByVal BLoadCaseCombinations As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadCaseManager
Dim BPrimaryLoadCases As System.Boolean
Dim BLoadCaseCombinations As System.Boolean
Dim value As System.Integer

value = instance.RunLoadCases(BPrimaryLoadCases, BLoadCaseCombinations)
```

### C#

```csharp
System.int RunLoadCases(
   System.bool BPrimaryLoadCases,
   System.bool BLoadCaseCombinations
)
```

### C++/CLI

```cpp
System.int RunLoadCases(
   System.bool BPrimaryLoadCases,
   System.bool BLoadCaseCombinations
)
```

### Parameters

- `BPrimaryLoadCases`: True to use primary load cases, false to not
- `BLoadCaseCombinations`: True to use load case combinations, false to not

### Return Value

Error as defined in [swsLoadCaseManagerError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsLoadCaseManagerError_e.html)

## VBA Syntax

See [CWLoadCaseManager::RunLoadCases](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadCaseManager~RunLoadCases.html).

## Examples

See the [ICWLoadCaseManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager.html) examples.

## See Also

[ICWLoadCaseManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager.html)
[ICWLoadCaseManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager_members.html)
[ICWLoadCaseManager::CloseLoadCaseManager Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~CloseLoadCaseManager.html)
[ICWLoadCaseManager::OpenLoadCaseManager Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~OpenLoadCaseManager.html)
[ICWLoadCaseManager::DeleteAllDataAndClose Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~DeleteAllDataAndClose.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
