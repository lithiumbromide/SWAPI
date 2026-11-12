---
title: "SuppressOrUnSuppressPrimaryLoadCase Method (ICWLoadCaseManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadCaseManager"
member: "SuppressOrUnSuppressPrimaryLoadCase"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~SuppressOrUnSuppressPrimaryLoadCase.html"
---

# SuppressOrUnSuppressPrimaryLoadCase Method (ICWLoadCaseManager)

Displays or hides the specified primary load case.

## Syntax

### Visual Basic (Declaration)

```vb
Function SuppressOrUnSuppressPrimaryLoadCase( _
   ByVal SLoadCaseName As System.String, _
   ByVal BSuppress As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadCaseManager
Dim SLoadCaseName As System.String
Dim BSuppress As System.Boolean
Dim value As System.Boolean

value = instance.SuppressOrUnSuppressPrimaryLoadCase(SLoadCaseName, BSuppress)
```

### C#

```csharp
System.bool SuppressOrUnSuppressPrimaryLoadCase(
   System.string SLoadCaseName,
   System.bool BSuppress
)
```

### C++/CLI

```cpp
System.bool SuppressOrUnSuppressPrimaryLoadCase(
   System.String^ SLoadCaseName,
   System.bool BSuppress
)
```

### Parameters

- `SLoadCaseName`: Name of primary load case
- `BSuppress`: True to hide SLoadCaseName, false to display it

### Return Value

True if successful, false if not

## VBA Syntax

See [CWLoadCaseManager::SuppressOrUnSuppressPrimaryLoadCase](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadCaseManager~SuppressOrUnSuppressPrimaryLoadCase.html).

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
[ICWLoadCaseManager::RenamePrimaryLoadCase Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~RenamePrimaryLoadCase.html)
[ICWLoadCaseManager::SetLoadDataForPrimaryLoadCase Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~SetLoadDataForPrimaryLoadCase.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
