---
title: "GetTransform Method (ILocalSketchPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalSketchPatternFeatureData"
member: "GetTransform"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData~GetTransform.html"
---

# GetTransform Method (ILocalSketchPatternFeatureData)

Gets the transform for the specified instance in this sketch-driven component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTransform( _
   ByVal Instance As System.Integer _
) As MathTransform
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalSketchPatternFeatureData
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

- `Instance`: Index of one repeating element in this local sketch-driven pattern feature (see **Remarks**)

### Return Value

[Transform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html)

## VBA Syntax

See [LocalSketchPatternFeatureData::GetTransform](ms-its:sldworksapivb6.chm::/sldworks~LocalSketchPatternFeatureData~GetTransform.html).

## Remarks

Valid values for Instance are 1 <= Instance <= [ILocalSketchPatternFeatureData::GetPatternComponentCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILocalSketchPatternFeatureData~GetPatternComponentCount.html)

## See Also

[ILocalSketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData.html)
[ILocalSketchPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
