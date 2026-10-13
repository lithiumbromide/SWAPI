---
title: "DeleteTrackResultsSensor Method (ICWLoadCaseManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadCaseManager"
member: "DeleteTrackResultsSensor"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~DeleteTrackResultsSensor.html"
---

# DeleteTrackResultsSensor Method (ICWLoadCaseManager)

Deletes the specified data sensor.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteTrackResultsSensor( _
   ByVal SSensorName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadCaseManager
Dim SSensorName As System.String
Dim value As System.Boolean

value = instance.DeleteTrackResultsSensor(SSensorName)
```

### C#

```csharp
System.bool DeleteTrackResultsSensor(
   System.string SSensorName
)
```

### C++/CLI

```cpp
System.bool DeleteTrackResultsSensor(
   System.String^ SSensorName
)
```

### Parameters

- `SSensorName`: Name of data sensor to delete

### Return Value

True if deletion is successful, false if not

## VBA Syntax

See [CWLoadCaseManager::DeleteTrackResultsSensor](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadCaseManager~DeleteTrackResultsSensor.html).

## Remarks

Call [ICWLoadCaseManager::GetAllTrackResultsSensorNames](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~GetAllTrackResultsSensorNames.html) to set SSensorName.

## See Also

[ICWLoadCaseManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager.html)
[ICWLoadCaseManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager_members.html)
[ICWLoadCaseManager::AddTrackResultsSensor Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~AddTrackResultsSensor.html)
[ICWLoadCaseManager::GetAllTrackResultsSensorNames Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~GetAllTrackResultsSensorNames.html)
[ICWLoadCaseManager::GetSensorResultValueForLoadCaseCombination Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~GetSensorResultValueForLoadCaseCombination.html)
[ICWLoadCaseManager::GetSensorResultValueForPrimaryLoadCase Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~GetSensorResultValueForPrimaryLoadCase.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
