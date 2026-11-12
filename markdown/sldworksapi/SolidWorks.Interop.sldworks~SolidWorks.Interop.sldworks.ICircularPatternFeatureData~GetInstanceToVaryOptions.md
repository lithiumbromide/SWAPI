---
title: "GetInstanceToVaryOptions Method (ICircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICircularPatternFeatureData"
member: "GetInstanceToVaryOptions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~GetInstanceToVaryOptions.html"
---

# GetInstanceToVaryOptions Method (ICircularPatternFeatureData)

Gets the options for varying the spacing of pattern instances in this circular pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetInstanceToVaryOptions() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICircularPatternFeatureData
Dim value As System.Object

value = instance.GetInstanceToVaryOptions()
```

### C#

```csharp
System.object GetInstanceToVaryOptions()
```

### C++/CLI

```cpp
System.Object^ GetInstanceToVaryOptions();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IInstanceToVaryOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions.html)

## VBA Syntax

See [CircularPatternFeatureData::GetInstanceToVaryOptions](ms-its:sldworksapivb6.chm::/sldworks~CircularPatternFeatureData~GetInstanceToVaryOptions.html).

## Remarks

This method is valid only if [ICircularPatternFeatureData::InstancesToVary](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~InstancesToVary.html) is true.

## See Also

[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.html)
[ICircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.html)
[ICircularPatternFeatureData::SetInstanceToVaryOptions Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~SetInstanceToVaryOptions.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
