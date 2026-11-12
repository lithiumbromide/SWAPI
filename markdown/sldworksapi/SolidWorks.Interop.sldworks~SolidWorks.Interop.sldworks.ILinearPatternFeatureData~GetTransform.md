---
title: "GetTransform Method (ILinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearPatternFeatureData"
member: "GetTransform"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~GetTransform.html"
---

# GetTransform Method (ILinearPatternFeatureData)

Gets the transform for the specified instance of this linear pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTransform( _
   ByVal Instance As System.Integer _
) As MathTransform
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearPatternFeatureData
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

See [LinearPatternFeatureData::GetTransform](ms-its:sldworksapivb6.chm::/sldworks~LinearPatternFeatureData~GetTransform.html).

## Remarks

1 <= `Instance` <= ([ILinearPatternFeatureData::D1TotalInstances](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILinearPatternFeatureData~D1TotalInstances.html) + [ILinearPatternFeatureData::D2TotalInstances](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILinearPatternFeatureData~D2TotalInstances.html))

## See Also

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html)
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.html)
[ILinearPatternFeatureData::SkippedItemArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~SkippedItemArray.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
