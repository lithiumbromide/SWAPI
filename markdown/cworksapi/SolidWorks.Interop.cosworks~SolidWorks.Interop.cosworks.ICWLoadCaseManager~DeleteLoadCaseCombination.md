---
title: "DeleteLoadCaseCombination Method (ICWLoadCaseManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadCaseManager"
member: "DeleteLoadCaseCombination"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~DeleteLoadCaseCombination.html"
---

# DeleteLoadCaseCombination Method (ICWLoadCaseManager)

Deletes the specified load case combination.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteLoadCaseCombination( _
   ByVal SCombinationName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadCaseManager
Dim SCombinationName As System.String
Dim value As System.Boolean

value = instance.DeleteLoadCaseCombination(SCombinationName)
```

### C#

```csharp
System.bool DeleteLoadCaseCombination(
   System.string SCombinationName
)
```

### C++/CLI

```cpp
System.bool DeleteLoadCaseCombination(
   System.String^ SCombinationName
)
```

### Parameters

- `SCombinationName`: Name of load case combination to delete

### Return Value

True if deletion is successful, false if not

## VBA Syntax

See [CWLoadCaseManager::DeleteLoadCaseCombination](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadCaseManager~DeleteLoadCaseCombination.html).

## Examples

See the [ICWLoadCaseManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager.html) examples.

## Remarks

Call [ICWLoadCaseManager::GetAllLoadCaseCombinationNames](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~GetAllLoadCaseCombinationNames.html) to set SCombinationName.

## See Also

[ICWLoadCaseManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager.html)
[ICWLoadCaseManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager_members.html)
[ICWLoadCaseManager::AddNewLoadCaseCombination Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~AddNewLoadCaseCombination.html)
[ICWLoadCaseManager::GetAllLoadCaseCombinationNames Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~GetAllLoadCaseCombinationNames.html)
[ICWLoadCaseManager::GetEquationForLoadCaseCombination Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~GetEquationForLoadCaseCombination.html)
[ICWLoadCaseManager::GetSensorResultValueForLoadCaseCombination Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~GetSensorResultValueForLoadCaseCombination.html)
[ICWLoadCaseManager::LoadResultsOfLoadCaseCombination Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~LoadResultsOfLoadCaseCombination.html)
[ICWLoadCaseManager::RenameLoadCaseCombination Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~RenameLoadCaseCombination.html)
[ICWLoadCaseManager::SetEquationForLoadCaseCombination Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~SetEquationForLoadCaseCombination.html)
[ICWLoadCaseManager::SuppressOrUnSuppressLoadCaseCombination Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~SuppressOrUnSuppressLoadCaseCombination.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
