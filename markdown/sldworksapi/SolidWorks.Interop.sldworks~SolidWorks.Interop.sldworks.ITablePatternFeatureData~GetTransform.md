---
title: "GetTransform Method (ITablePatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ITablePatternFeatureData"
member: "GetTransform"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~GetTransform.html"
---

# GetTransform Method (ITablePatternFeatureData)

Gets the transform for the specified repeating element in this table-driven pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTransform( _
   ByVal Instance As System.Integer _
) As MathTransform
```

### Visual Basic (Usage)

```vb
Dim instance As ITablePatternFeatureData
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

- `Instance`: Index of one repeating element in the pattern (see **Remarks**)

### Return Value

[Transform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html)

## VBA Syntax

See [TablePatternFeatureData::GetTransform](ms-its:sldworksapivb6.chm::/sldworks~TablePatternFeatureData~GetTransform.html).

## Remarks

1 <= `Instance` <= [ITablePatternFeatureData::GetPointCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITablePatternFeatureData~GetPointCount.html)

## See Also

[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.html)
[ITablePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
