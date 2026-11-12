---
title: "GetControlPointsCount Method (IVariableFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData2"
member: "GetControlPointsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetControlPointsCount.html"
---

# GetControlPointsCount Method (IVariableFilletFeatureData2)

Gets the number of intermediate control points on this variable fillet feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetControlPointsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData2
Dim value As System.Integer

value = instance.GetControlPointsCount()
```

### C#

```csharp
System.int GetControlPointsCount()
```

### C++/CLI

```cpp
System.int GetControlPointsCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of intermediate control points

## VBA Syntax

See [VariableFilletFeatureData2::GetControlPointsCount](ms-its:sldworksapivb6.chm::/sldworks~VariableFilletFeatureData2~GetControlPointsCount.html).

## Remarks

Call this method before calling [IVariableFilletFeatureData2::GetControlPointRadiusAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVariableFilletFeatureData2~GetControlPointRadiusAtIndex.html).

## See Also

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
