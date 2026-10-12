---
title: "SetInstanceToVaryOptions Method (ICircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICircularPatternFeatureData"
member: "SetInstanceToVaryOptions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~SetInstanceToVaryOptions.html"
---

# SetInstanceToVaryOptions Method (ICircularPatternFeatureData)

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
Dim instance As ICircularPatternFeatureData
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

See [CircularPatternFeatureData::SetInstanceToVaryOptions](ms-its:sldworksapivb6.chm::/sldworks~CircularPatternFeatureData~SetInstanceToVaryOptions.html).

## Remarks

This method is valid only if [ICircularPatternFeatureData::InstancesToVary](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~InstancesToVary.html) is true.

## See Also

[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.html)
[ICircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.html)
[ICircularPatternFeatureData::GetInstanceToVaryOptions Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~GetInstanceToVaryOptions.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
