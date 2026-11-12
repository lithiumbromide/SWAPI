---
title: "GetSelectionCount Method (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "GetSelectionCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetSelectionCount.html"
---

# GetSelectionCount Method (IMacroFeatureData)

Gets the number of selected objects for the macro feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSelectionCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim value As System.Integer

value = instance.GetSelectionCount()
```

### C#

```csharp
System.int GetSelectionCount()
```

### C++/CLI

```cpp
System.int GetSelectionCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of selected objects

## VBA Syntax

See [MacroFeatureData::GetSelectionCount](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData~GetSelectionCount.html).

## Remarks

Call ths method before calling [IMacroFeatureData::IGetSelections3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~IGetSelections3.html) to determine the size of the array for that method.

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
[IMacroFeatureData::ISetSelections2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ISetSelections2.html)
[IMacroFeatureData::SetSelections2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetSelections2.html)
[IMacroFeatureData::GetSelections3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetSelections3.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
