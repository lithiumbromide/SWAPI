---
title: "SetEquationForLoadCaseCombination Method (ICWLoadCaseManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadCaseManager"
member: "SetEquationForLoadCaseCombination"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~SetEquationForLoadCaseCombination.html"
---

# SetEquationForLoadCaseCombination Method (ICWLoadCaseManager)

Sets the linear combination of primary load cases for the specified load case combination.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetEquationForLoadCaseCombination( _
   ByVal SCombinationName As System.String, _
   ByVal SNewCombinationEquation As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadCaseManager
Dim SCombinationName As System.String
Dim SNewCombinationEquation As System.String
Dim value As System.Integer

value = instance.SetEquationForLoadCaseCombination(SCombinationName, SNewCombinationEquation)
```

### C#

```csharp
System.int SetEquationForLoadCaseCombination(
   System.string SCombinationName,
   System.string SNewCombinationEquation
)
```

### C++/CLI

```cpp
System.int SetEquationForLoadCaseCombination(
   System.String^ SCombinationName,
   System.String^ SNewCombinationEquation
)
```

### Parameters

- `SCombinationName`: Name of load case combination
- `SNewCombinationEquation`: Equation; linear combination of primary load cases

### Return Value

Error as defined in [swsLoadCaseManagerError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsLoadCaseManagerError_e.html)

## VBA Syntax

See [CWLoadCaseManager::SetEquationForLoadCaseCombination](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadCaseManager~SetEquationForLoadCaseCombination.html).

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
[ICWLoadCaseManager::SuppressOrUnSuppressLoadCaseCombination Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~SuppressOrUnSuppressLoadCaseCombination.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
