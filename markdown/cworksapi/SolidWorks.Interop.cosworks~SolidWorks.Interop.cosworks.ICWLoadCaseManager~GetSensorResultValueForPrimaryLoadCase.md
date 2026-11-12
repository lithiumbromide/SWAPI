---
title: "GetSensorResultValueForPrimaryLoadCase Method (ICWLoadCaseManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadCaseManager"
member: "GetSensorResultValueForPrimaryLoadCase"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~GetSensorResultValueForPrimaryLoadCase.html"
---

# GetSensorResultValueForPrimaryLoadCase Method (ICWLoadCaseManager)

Gets the result data for the specified data sensor and primary load case.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSensorResultValueForPrimaryLoadCase( _
   ByVal SSensorName As System.String, _
   ByVal SLoadCaseName As System.String, _
   ByRef DResultValue As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadCaseManager
Dim SSensorName As System.String
Dim SLoadCaseName As System.String
Dim DResultValue As System.Double
Dim value As System.Boolean

value = instance.GetSensorResultValueForPrimaryLoadCase(SSensorName, SLoadCaseName, DResultValue)
```

### C#

```csharp
System.bool GetSensorResultValueForPrimaryLoadCase(
   System.string SSensorName,
   System.string SLoadCaseName,
   out System.double DResultValue
)
```

### C++/CLI

```cpp
System.bool GetSensorResultValueForPrimaryLoadCase(
   System.String^ SSensorName,
   System.String^ SLoadCaseName,
   [Out] System.double DResultValue
)
```

### Parameters

- `SSensorName`: Name of data sensor
- `SLoadCaseName`: Name of primary load case
- `DResultValue`: Result value from SSensorName

### Return Value

True if successful, false if not

## VBA Syntax

See [CWLoadCaseManager::GetSensorResultValueForPrimaryLoadCase](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadCaseManager~GetSensorResultValueForPrimaryLoadCase.html).

## Remarks

- Call [ICWLoadCaseManager::GetAllTrackResultsSensorNames](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~GetAllTrackResultsSensorNames.html) to set SSensorName.
- Call [ICWLoadCaseManager::GetAllPrimaryLoadCaseNames](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~GetAllPrimaryLoadCaseNames.html) to set SLoadCaseName.

## See Also

[ICWLoadCaseManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager.html)
[ICWLoadCaseManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager_members.html)
[ICWLoadCaseManager::AddNewPrimaryLoadCase Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~AddNewPrimaryLoadCase.html)
[ICWLoadCaseManager::DeletePrimaryLoadCase Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~DeletePrimaryLoadCase.html)
[ICWLoadCaseManager::GetLoadDataForPrimaryLoadCase Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~GetLoadDataForPrimaryLoadCase.html)
[ICWLoadCaseManager::LoadResultsOfPrimaryLoadCase Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~LoadResultsOfPrimaryLoadCase.html)
[ICWLoadCaseManager::RenamePrimaryLoadCase Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~RenamePrimaryLoadCase.html)
[ICWLoadCaseManager::SetLoadDataForPrimaryLoadCase Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~SetLoadDataForPrimaryLoadCase.html)
[ICWLoadCaseManager::SuppressOrUnSuppressPrimaryLoadCase Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~SuppressOrUnSuppressPrimaryLoadCase.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
