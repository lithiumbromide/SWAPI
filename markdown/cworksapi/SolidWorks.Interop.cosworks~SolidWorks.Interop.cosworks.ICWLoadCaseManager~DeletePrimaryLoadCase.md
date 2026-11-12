---
title: "DeletePrimaryLoadCase Method (ICWLoadCaseManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadCaseManager"
member: "DeletePrimaryLoadCase"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~DeletePrimaryLoadCase.html"
---

# DeletePrimaryLoadCase Method (ICWLoadCaseManager)

Deletes the specified primary load case.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeletePrimaryLoadCase( _
   ByVal SLoadCaseName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadCaseManager
Dim SLoadCaseName As System.String
Dim value As System.Boolean

value = instance.DeletePrimaryLoadCase(SLoadCaseName)
```

### C#

```csharp
System.bool DeletePrimaryLoadCase(
   System.string SLoadCaseName
)
```

### C++/CLI

```cpp
System.bool DeletePrimaryLoadCase(
   System.String^ SLoadCaseName
)
```

### Parameters

- `SLoadCaseName`: Name of primary load case to delete

### Return Value

True if deletion is successful, false if not

## VBA Syntax

See [CWLoadCaseManager::DeletePrimaryLoadCase](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadCaseManager~DeletePrimaryLoadCase.html).

## Examples

See the [ICWLoadCaseManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager.html) examples.

## Remarks

Call [ICWLoadCaseManager::GetAllPrimaryLoadCaseNames](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~GetAllPrimaryLoadCaseNames.html) to set SLoadCaseName.

## See Also

[ICWLoadCaseManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager.html)
[ICWLoadCaseManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager_members.html)
[ICWLoadCaseManager::AddNewPrimaryLoadCase Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~AddNewPrimaryLoadCase.html)
[ICWLoadCaseManager::GetLoadDataForPrimaryLoadCase Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~GetLoadDataForPrimaryLoadCase.html)
[ICWLoadCaseManager::GetSensorResultValueForPrimaryLoadCase Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~GetSensorResultValueForPrimaryLoadCase.html)
[ICWLoadCaseManager::LoadResultsOfPrimaryLoadCase Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~LoadResultsOfPrimaryLoadCase.html)
[ICWLoadCaseManager::RenamePrimaryLoadCase Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~RenamePrimaryLoadCase.html)
[ICWLoadCaseManager::SetLoadDataForPrimaryLoadCase Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~SetLoadDataForPrimaryLoadCase.html)
[ICWLoadCaseManager::SuppressOrUnSuppressPrimaryLoadCase Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~SuppressOrUnSuppressPrimaryLoadCase.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
