---
title: "GetLoadDataForPrimaryLoadCase Method (ICWLoadCaseManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadCaseManager"
member: "GetLoadDataForPrimaryLoadCase"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~GetLoadDataForPrimaryLoadCase.html"
---

# GetLoadDataForPrimaryLoadCase Method (ICWLoadCaseManager)

Gets the load data for the specified primary load case and load.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLoadDataForPrimaryLoadCase( _
   ByVal SLoadCaseName As System.String, _
   ByVal SLoadName As System.String, _
   ByRef ArraySuppressComps As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadCaseManager
Dim SLoadCaseName As System.String
Dim SLoadName As System.String
Dim ArraySuppressComps As System.Object
Dim value As System.Object

value = instance.GetLoadDataForPrimaryLoadCase(SLoadCaseName, SLoadName, ArraySuppressComps)
```

### C#

```csharp
System.object GetLoadDataForPrimaryLoadCase(
   System.string SLoadCaseName,
   System.string SLoadName,
   out System.object ArraySuppressComps
)
```

### C++/CLI

```cpp
System.Object^ GetLoadDataForPrimaryLoadCase(
   System.String^ SLoadCaseName,
   System.String^ SLoadName,
   [Out] System.Object^ ArraySuppressComps
)
```

### Parameters

- `SLoadCaseName`: Name of primary load case
- `SLoadName`: Name of load
- `ArraySuppressComps`: Array of booleans indicating which of the returned values for SLoadName are suppressed; true if suppressed, false if not

### Return Value

Array of load data for SLoadName

## VBA Syntax

See [CWLoadCaseManager::GetLoadDataForPrimaryLoadCase](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadCaseManager~GetLoadDataForPrimaryLoadCase.html).

## Examples

See the [ICWLoadCaseManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager.html) examples.

## Remarks

Call [ICWLoadCaseManager::GetAllPrimaryLoadCaseNames](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~GetAllPrimaryLoadCaseNames.html) to set SLoadCaseName.

## See Also

[ICWLoadCaseManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager.html)
[ICWLoadCaseManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager_members.html)
[ICWLoadCaseManager::AddNewPrimaryLoadCase Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~AddNewPrimaryLoadCase.html)
[ICWLoadCaseManager::DeletePrimaryLoadCase Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~DeletePrimaryLoadCase.html)
[ICWLoadCaseManager::GetSensorResultValueForPrimaryLoadCase Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~GetSensorResultValueForPrimaryLoadCase.html)
[ICWLoadCaseManager::LoadResultsOfPrimaryLoadCase Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~LoadResultsOfPrimaryLoadCase.html)
[ICWLoadCaseManager::RenamePrimaryLoadCase Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~RenamePrimaryLoadCase.html)
[ICWLoadCaseManager::SetLoadDataForPrimaryLoadCase Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~SetLoadDataForPrimaryLoadCase.html)
[ICWLoadCaseManager::SuppressOrUnSuppressPrimaryLoadCase Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~SuppressOrUnSuppressPrimaryLoadCase.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
