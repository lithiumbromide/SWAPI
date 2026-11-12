---
title: "AddNewLoadCaseCombination Method (ICWLoadCaseManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadCaseManager"
member: "AddNewLoadCaseCombination"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~AddNewLoadCaseCombination.html"
---

# AddNewLoadCaseCombination Method (ICWLoadCaseManager)

Adds the specified linear combination of primary load cases.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddNewLoadCaseCombination( _
   ByVal SCombinationName As System.String, _
   ByVal SCombinationEquation As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadCaseManager
Dim SCombinationName As System.String
Dim SCombinationEquation As System.String
Dim value As System.Integer

value = instance.AddNewLoadCaseCombination(SCombinationName, SCombinationEquation)
```

### C#

```csharp
System.int AddNewLoadCaseCombination(
   System.string SCombinationName,
   System.string SCombinationEquation
)
```

### C++/CLI

```cpp
System.int AddNewLoadCaseCombination(
   System.String^ SCombinationName,
   System.String^ SCombinationEquation
)
```

### Parameters

- `SCombinationName`: Name of load case combination
- `SCombinationEquation`: Equation; linear combination of primary load cases

### Return Value

Error as defined in [swsLoadCaseManagerError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsLoadCaseManagerError_e.html)

## VBA Syntax

See [CWLoadCaseManager::AddNewLoadCaseCombination](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadCaseManager~AddNewLoadCaseCombination.html).

## Examples

See the [ICWLoadCaseManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager.html) examples.

## See Also

[ICWLoadCaseManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager.html)
[ICWLoadCaseManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager_members.html)
[ICWLoadCaseManager::DeleteLoadCaseCombination Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~DeleteLoadCaseCombination.html)
[ICWLoadCaseManager::GetAllLoadCaseCombinationNames Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~GetAllLoadCaseCombinationNames.html)
[ICWLoadCaseManager::GetEquationForLoadCaseCombination Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~GetEquationForLoadCaseCombination.html)
[ICWLoadCaseManager::GetSensorResultValueForLoadCaseCombination Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~GetSensorResultValueForLoadCaseCombination.html)
[ICWLoadCaseManager::LoadResultsOfLoadCaseCombination Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~LoadResultsOfLoadCaseCombination.html)
[ICWLoadCaseManager::RenameLoadCaseCombination Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~RenameLoadCaseCombination.html)
[ICWLoadCaseManager::SetEquationForLoadCaseCombination Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~SetEquationForLoadCaseCombination.html)
[ICWLoadCaseManager::SuppressOrUnSuppressLoadCaseCombination Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~SuppressOrUnSuppressLoadCaseCombination.html)
[ICWLoadCaseManager::RunLoadCases Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~RunLoadCases.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
