---
title: "AddTrackResultsSensor Method (ICWLoadCaseManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadCaseManager"
member: "AddTrackResultsSensor"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~AddTrackResultsSensor.html"
---

# AddTrackResultsSensor Method (ICWLoadCaseManager)

Adds the specified data sensor.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddTrackResultsSensor( _
   ByVal SSensorName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadCaseManager
Dim SSensorName As System.String
Dim value As System.Boolean

value = instance.AddTrackResultsSensor(SSensorName)
```

### C#

```csharp
System.bool AddTrackResultsSensor(
   System.string SSensorName
)
```

### C++/CLI

```cpp
System.bool AddTrackResultsSensor(
   System.String^ SSensorName
)
```

### Parameters

- `SSensorName`: Name of data sensor

### Return Value

True if successfully added, false if not

## VBA Syntax

See [CWLoadCaseManager::AddTrackResultsSensor](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadCaseManager~AddTrackResultsSensor.html).

## See Also

[ICWLoadCaseManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager.html)
[ICWLoadCaseManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager_members.html)
[ICWLoadCaseManager::DeleteTrackResultsSensor Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~DeleteTrackResultsSensor.html)
[ICWLoadCaseManager::GetAllTrackResultsSensorNames Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~GetAllTrackResultsSensorNames.html)
[ICWLoadCaseManager::GetSensorResultValueForLoadCaseCombination Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~GetSensorResultValueForLoadCaseCombination.html)
[ICWLoadCaseManager::GetSensorResultValueForPrimaryLoadCase Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~GetSensorResultValueForPrimaryLoadCase.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
