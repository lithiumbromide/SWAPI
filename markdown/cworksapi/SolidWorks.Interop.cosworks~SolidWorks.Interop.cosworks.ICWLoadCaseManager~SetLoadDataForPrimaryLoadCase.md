---
title: "SetLoadDataForPrimaryLoadCase Method (ICWLoadCaseManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadCaseManager"
member: "SetLoadDataForPrimaryLoadCase"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~SetLoadDataForPrimaryLoadCase.html"
---

# SetLoadDataForPrimaryLoadCase Method (ICWLoadCaseManager)

Sets the load data for the specified primary load case and load.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetLoadDataForPrimaryLoadCase( _
   ByVal SLoadCaseName As System.String, _
   ByVal SLoadName As System.String, _
   ByVal ArrayInputSuppressComps As System.Object, _
   ByVal DataArrayInputVals As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadCaseManager
Dim SLoadCaseName As System.String
Dim SLoadName As System.String
Dim ArrayInputSuppressComps As System.Object
Dim DataArrayInputVals As System.Object
Dim value As System.Integer

value = instance.SetLoadDataForPrimaryLoadCase(SLoadCaseName, SLoadName, ArrayInputSuppressComps, DataArrayInputVals)
```

### C#

```csharp
System.int SetLoadDataForPrimaryLoadCase(
   System.string SLoadCaseName,
   System.string SLoadName,
   System.object ArrayInputSuppressComps,
   System.object DataArrayInputVals
)
```

### C++/CLI

```cpp
System.int SetLoadDataForPrimaryLoadCase(
   System.String^ SLoadCaseName,
   System.String^ SLoadName,
   System.Object^ ArrayInputSuppressComps,
   System.Object^ DataArrayInputVals
)
```

### Parameters

- `SLoadCaseName`: Name of primary load case
- `SLoadName`: Name of load
- `ArrayInputSuppressComps`: Array of booleans indicating which of the values in DataArrayInputVals to suppress; true to suppress, false to not
- `DataArrayInputVals`: Array of values for SLoadName

### Return Value

Error as defined in [swsLoadCaseManagerError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsLoadCaseManagerError_e.html)

## VBA Syntax

See [CWLoadCaseManager::SetLoadDataForPrimaryLoadCase](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadCaseManager~SetLoadDataForPrimaryLoadCase.html).

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
[ICWLoadCaseManager::SuppressOrUnSuppressPrimaryLoadCase Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager~SuppressOrUnSuppressPrimaryLoadCase.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
