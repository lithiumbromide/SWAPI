---
title: "GetTransform Method (ICircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICircularPatternFeatureData"
member: "GetTransform"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~GetTransform.html"
---

# GetTransform Method (ICircularPatternFeatureData)

Gets the transform for the specified instance of this circular-pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTransform( _
   ByVal Instance As System.Integer _
) As MathTransform
```

### Visual Basic (Usage)

```vb
Dim instance As ICircularPatternFeatureData
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

See [CircularPatternFeatureData::GetTransform](ms-its:sldworksapivb6.chm::/sldworks~CircularPatternFeatureData~GetTransform.html).

## Examples

[Get Transform for Each Circular Pattern Instance (C#)](Get_Transform_for_Each_Circular_Pattern_Instance_Example_CSharp.htm)
[Get Transform for Each Circular Pattern Instance (VB.NET)](Get_Transform_for_Each_Circular_Pattern_Instance_Example_VBNET.htm)
[Get Transform for Each Circular Pattern Instance (VBA)](Get_Transform_for_Each_Circular_Pattern_Instance_Example_VB.htm)

## Remarks

1 <= `Instance` <= [ICircularPatternFeatureData::TotalInstances](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICircularPatternFeatureData~TotalInstances.html)

## See Also

[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.html)
[ICircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
