---
title: "SetInstanceToVaryOptions Method (ILinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearPatternFeatureData"
member: "SetInstanceToVaryOptions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~SetInstanceToVaryOptions.html"
---

# SetInstanceToVaryOptions Method (ILinearPatternFeatureData)

Sets the options for varying the spacing of pattern instances in this circular pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetInstanceToVaryOptions( _
   ByVal InstancesToVaryObj As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearPatternFeatureData
Dim InstancesToVaryObj As System.Object
Dim value As System.Boolean

value = instance.SetInstanceToVaryOptions(InstancesToVaryObj)
```

### C#

```csharp
System.bool SetInstanceToVaryOptions(
   System.object InstancesToVaryObj
)
```

### C++/CLI

```cpp
System.bool SetInstanceToVaryOptions(
   System.Object^ InstancesToVaryObj
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `InstancesToVaryObj`: [IInstanceToVaryOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions.html)

### Return Value

True if options successfully set, false if not

## VBA Syntax

See [LinearPatternFeatureData::SetInstanceToVaryOptions](ms-its:sldworksapivb6.chm::/sldworks~LinearPatternFeatureData~SetInstanceToVaryOptions.html).

## Examples

See the [IInstanceToVaryOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions.html) examples.

## Remarks

This method is valid only if [ILinearPatternFeatureData::InstancesToVary](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~InstancesToVary.html) is true.

## See Also

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html)
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.html)
[ILinearPatternFeatureData::GetInstanceToVaryOptions Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~GetInstanceToVaryOptions.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
