---
title: "GetInstanceToVaryOptions Method (ILinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearPatternFeatureData"
member: "GetInstanceToVaryOptions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~GetInstanceToVaryOptions.html"
---

# GetInstanceToVaryOptions Method (ILinearPatternFeatureData)

Gets the options for varying the spacing of pattern instances in this linear pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetInstanceToVaryOptions() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearPatternFeatureData
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

See [LinearPatternFeatureData::GetInstanceToVaryOptions](ms-its:sldworksapivb6.chm::/sldworks~LinearPatternFeatureData~GetInstanceToVaryOptions.html).

## Examples

See the [IInstanceToVaryOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions.html) examples.

## Remarks

This method is valid only if [ILinearPatternFeatureData::InstancesToVary](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~InstancesToVary.html) is true.

## See Also

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html)
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.html)
[ILinearPatternFeatureData::SetInstanceToVaryOptions Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~SetInstanceToVaryOptions.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
