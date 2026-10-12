---
title: "GetParentsCount Method (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "GetParentsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetParentsCount.html"
---

# GetParentsCount Method (IMacroFeatureData)

Gets the number of parent features for this macro feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetParentsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim value As System.Integer

value = instance.GetParentsCount()
```

### C#

```csharp
System.int GetParentsCount()
```

### C++/CLI

```cpp
System.int GetParentsCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of parent features for this macro feature

## VBA Syntax

See [MacroFeatureData::GetParentsCount](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData~GetParentsCount.html).

## Remarks

Call this method before using [IMacroFeatureData::IGetParents](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~IGetParents.html) to determine the size of the array for that method.

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
[IMacroFeatureData::IGetParents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetParents.html)
[IMacroFeatureData::ISetParents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ISetParents.html)
[IMacroFeatureData::Parents Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~Parents.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
