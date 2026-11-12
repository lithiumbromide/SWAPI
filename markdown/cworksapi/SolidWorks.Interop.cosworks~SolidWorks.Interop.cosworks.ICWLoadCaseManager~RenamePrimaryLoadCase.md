---
title: "RenamePrimaryLoadCase Method (ICWLoadCaseManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadCaseManager"
member: "RenamePrimaryLoadCase"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~RenamePrimaryLoadCase.html"
---

# RenamePrimaryLoadCase Method (ICWLoadCaseManager)

Renames the specified primary load case.

## Syntax

### Visual Basic (Declaration)

```vb
Function RenamePrimaryLoadCase( _
   ByVal SLoadCaseName As System.String, _
   ByVal SNewLoadCaseName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadCaseManager
Dim SLoadCaseName As System.String
Dim SNewLoadCaseName As System.String
Dim value As System.Boolean

value = instance.RenamePrimaryLoadCase(SLoadCaseName, SNewLoadCaseName)
```

### C#

```csharp
System.bool RenamePrimaryLoadCase(
   System.string SLoadCaseName,
   System.string SNewLoadCaseName
)
```

### C++/CLI

```cpp
System.bool RenamePrimaryLoadCase(
   System.String^ SLoadCaseName,
   System.String^ SNewLoadCaseName
)
```

### Parameters

- `SLoadCaseName`: Current name of primary load case
- `SNewLoadCaseName`: New name of primary load case

### Return Value

True if successful, false if not

## VBA Syntax

See [CWLoadCaseManager::RenamePrimaryLoadCase](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadCaseManager~RenamePrimaryLoadCase.html).

## Examples

See the [ICWLoadCaseManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager.html) examples.

## Remarks

Call [ICWLoadCaseManager::GetAllPrimaryLoadCaseNames](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~GetAllPrimaryLoadCaseNames.html) to set SLoadCaseName.

## See Also

[ICWLoadCaseManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager.html)
[ICWLoadCaseManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager_members.html)
[ICWLoadCaseManager::AddNewPrimaryLoadCase Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~AddNewPrimaryLoadCase.html)
[ICWLoadCaseManager::DeletePrimaryLoadCase Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~DeletePrimaryLoadCase.html)
[ICWLoadCaseManager::GetLoadDataForPrimaryLoadCase Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~GetLoadDataForPrimaryLoadCase.html)
[ICWLoadCaseManager::GetSensorResultValueForPrimaryLoadCase Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~GetSensorResultValueForPrimaryLoadCase.html)
[ICWLoadCaseManager::LoadResultsOfPrimaryLoadCase Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~LoadResultsOfPrimaryLoadCase.html)
[ICWLoadCaseManager::SetLoadDataForPrimaryLoadCase Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~SetLoadDataForPrimaryLoadCase.html)
[ICWLoadCaseManager::SuppressOrUnSuppressPrimaryLoadCase Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~SuppressOrUnSuppressPrimaryLoadCase.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
