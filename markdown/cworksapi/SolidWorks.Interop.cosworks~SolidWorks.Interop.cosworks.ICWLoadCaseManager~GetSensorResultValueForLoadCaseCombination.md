---
title: "GetSensorResultValueForLoadCaseCombination Method (ICWLoadCaseManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadCaseManager"
member: "GetSensorResultValueForLoadCaseCombination"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~GetSensorResultValueForLoadCaseCombination.html"
---

# GetSensorResultValueForLoadCaseCombination Method (ICWLoadCaseManager)

Gets the result data for the specified data sensor and load case combination.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSensorResultValueForLoadCaseCombination( _
   ByVal SSensorName As System.String, _
   ByVal SCombinationName As System.String, _
   ByRef DResultValue As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadCaseManager
Dim SSensorName As System.String
Dim SCombinationName As System.String
Dim DResultValue As System.Double
Dim value As System.Boolean

value = instance.GetSensorResultValueForLoadCaseCombination(SSensorName, SCombinationName, DResultValue)
```

### C#

```csharp
System.bool GetSensorResultValueForLoadCaseCombination(
   System.string SSensorName,
   System.string SCombinationName,
   out System.double DResultValue
)
```

### C++/CLI

```cpp
System.bool GetSensorResultValueForLoadCaseCombination(
   System.String^ SSensorName,
   System.String^ SCombinationName,
   [Out] System.double DResultValue
)
```

### Parameters

- `SSensorName`: Name of data sensor
- `SCombinationName`: Name of load case combination
- `DResultValue`: Result data from SSensorName

### Return Value

True if successful, false if not

## VBA Syntax

See [CWLoadCaseManager::GetSensorResultValueForLoadCaseCombination](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadCaseManager~GetSensorResultValueForLoadCaseCombination.html).

## Remarks

- Call [ICWLoadCaseManager::GetAllTrackResultsSensorNames](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~GetAllTrackResultsSensorNames.html) to set SSensorName.
- Call [ICWLoadCaseManager::GetAllLoadCaseCombinationNames](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~GetAllLoadCaseCombinationNames.html) to set SCombinationName.

## See Also

[ICWLoadCaseManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager.html)
[ICWLoadCaseManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager_members.html)
[ICWLoadCaseManager::AddNewLoadCaseCombination Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~AddNewLoadCaseCombination.html)
[ICWLoadCaseManager::DeleteLoadCaseCombination Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~DeleteLoadCaseCombination.html)
[ICWLoadCaseManager::GetEquationForLoadCaseCombination Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~GetEquationForLoadCaseCombination.html)
[ICWLoadCaseManager::LoadResultsOfLoadCaseCombination Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~LoadResultsOfLoadCaseCombination.html)
[ICWLoadCaseManager::RenameLoadCaseCombination Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~RenameLoadCaseCombination.html)
[ICWLoadCaseManager::SetEquationForLoadCaseCombination Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~SetEquationForLoadCaseCombination.html)
[ICWLoadCaseManager::SuppressOrUnSuppressLoadCaseCombination Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~SuppressOrUnSuppressLoadCaseCombination.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
