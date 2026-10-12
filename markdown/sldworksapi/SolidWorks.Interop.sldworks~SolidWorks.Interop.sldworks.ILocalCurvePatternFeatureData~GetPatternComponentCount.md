---
title: "GetPatternComponentCount Method (ILocalCurvePatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalCurvePatternFeatureData"
member: "GetPatternComponentCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~GetPatternComponentCount.html"
---

# GetPatternComponentCount Method (ILocalCurvePatternFeatureData)

Gets the number of components in this curve-driven component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPatternComponentCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalCurvePatternFeatureData
Dim value As System.Integer

value = instance.GetPatternComponentCount()
```

### C#

```csharp
System.int GetPatternComponentCount()
```

### C++/CLI

```cpp
System.int GetPatternComponentCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of components

## VBA Syntax

See [LocalCurvePatternFeatureData::GetPatternComponentCount](ms-its:sldworksapivb6.chm::/sldworks~LocalCurvePatternFeatureData~GetPatternComponentCount.html).

## Examples

[Create Local Curve-driven Pattern (C#)](Create_Local_Curve-driven_Pattern_Example_CSharp.htm)
[Create Local Curve-driven Pattern (VB.NET)](Create_Local_Curve-driven_Pattern_Example_VBNET.htm)
[Create Local Curve-driven Pattern (VBA)](Create_Local_Curve-driven_Pattern_Example_VB.htm)

## See Also

[ILocalCurvePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData.html)
[ILocalCurvePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData_members.html)
[ILocalCurvePatternFeatureData::PatternComponentArray Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~PatternComponentArray.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
