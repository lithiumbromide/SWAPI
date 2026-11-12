---
title: "GetTransform Method (ILocalLinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalLinearPatternFeatureData"
member: "GetTransform"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~GetTransform.html"
---

# GetTransform Method (ILocalLinearPatternFeatureData)

Gets the transform for the specified instance of this linear component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTransform( _
   ByVal Instance As System.Integer _
) As MathTransform
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalLinearPatternFeatureData
Dim Instance As System.Integer
Dim value As MathTransform

value = instance.GetTransform(Instance)
```

### C#

```csharp
MathTransform GetTransform(
   System.int Instance
)
```

### C++/CLI

```cpp
MathTransform^ GetTransform(
   System.int Instance
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Instance`: Index of one repeating element in this pattern (see **Remarks**)

### Return Value

[Transform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html)

## VBA Syntax

See [LocalLinearPatternFeatureData::GetTransform](ms-its:sldworksapivb6.chm::/sldworks~LocalLinearPatternFeatureData~GetTransform.html).

## Remarks

1 <= `Instance` <= ([ILocalLinearPatternFeatureData::D1TotalInstances](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILocalLinearPatternFeatureData~D1TotalInstances.html) + [ILocalLinearPatternFeatureData::D2TotalInstances](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILocalLinearPatternFeatureData~D2TotalInstances.html))

## See Also

[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.html)
[ILocalLinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.html)
[ILocalLinearPatternFeatureData::SkippedItemArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~SkippedItemArray.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
