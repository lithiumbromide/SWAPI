---
title: "SuppressOrUnSuppressLoadCaseCombination Method (ICWLoadCaseManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadCaseManager"
member: "SuppressOrUnSuppressLoadCaseCombination"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~SuppressOrUnSuppressLoadCaseCombination.html"
---

# SuppressOrUnSuppressLoadCaseCombination Method (ICWLoadCaseManager)

Displays or hides the specified load case combination.

## Syntax

### Visual Basic (Declaration)

```vb
Function SuppressOrUnSuppressLoadCaseCombination( _
   ByVal SCombinationName As System.String, _
   ByVal BSuppress As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadCaseManager
Dim SCombinationName As System.String
Dim BSuppress As System.Boolean
Dim value As System.Boolean

value = instance.SuppressOrUnSuppressLoadCaseCombination(SCombinationName, BSuppress)
```

### C#

```csharp
System.bool SuppressOrUnSuppressLoadCaseCombination(
   System.string SCombinationName,
   System.bool BSuppress
)
```

### C++/CLI

```cpp
System.bool SuppressOrUnSuppressLoadCaseCombination(
   System.String^ SCombinationName,
   System.bool BSuppress
)
```

### Parameters

- `SCombinationName`: Name of load case combination
- `BSuppress`: True to hide SCombinationName, false to display it

### Return Value

True if successful, false if not

## VBA Syntax

See [CWLoadCaseManager::SuppressOrUnSuppressLoadCaseCombination](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadCaseManager~SuppressOrUnSuppressLoadCaseCombination.html).

## Examples

See the [ICWLoadCaseManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager.html) examples.

## Remarks

Call [ICWLoadCaseManager::GetAllLoadCaseCombinationNames](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~GetAllLoadCaseCombinationNames.html) to set SCombinationName.

## See Also

[ICWLoadCaseManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager.html)
[ICWLoadCaseManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager_members.html)
[ICWLoadCaseManager::AddNewLoadCaseCombination Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~AddNewLoadCaseCombination.html)
[ICWLoadCaseManager::DeleteLoadCaseCombination Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~DeleteLoadCaseCombination.html)
[ICWLoadCaseManager::GetEquationForLoadCaseCombination Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~GetEquationForLoadCaseCombination.html)
[ICWLoadCaseManager::GetSensorResultValueForLoadCaseCombination Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~GetSensorResultValueForLoadCaseCombination.html)
[ICWLoadCaseManager::LoadResultsOfLoadCaseCombination Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~LoadResultsOfLoadCaseCombination.html)
[ICWLoadCaseManager::RenameLoadCaseCombination Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~RenameLoadCaseCombination.html)
[ICWLoadCaseManager::SetEquationForLoadCaseCombination Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~SetEquationForLoadCaseCombination.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
