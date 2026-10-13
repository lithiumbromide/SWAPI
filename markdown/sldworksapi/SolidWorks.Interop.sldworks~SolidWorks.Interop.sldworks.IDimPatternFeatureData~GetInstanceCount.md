---
title: "GetInstanceCount Method (IDimPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDimPatternFeatureData"
member: "GetInstanceCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceCount.html"
---

# GetInstanceCount Method (IDimPatternFeatureData)

Gets the number of pattern instances in this variable pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetInstanceCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDimPatternFeatureData
Dim value As System.Integer

value = instance.GetInstanceCount()
```

### C#

```csharp
System.int GetInstanceCount()
```

### C++/CLI

```cpp
System.int GetInstanceCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of pattern instances

## VBA Syntax

See [DimPatternFeatureData::GetInstanceCount](ms-its:sldworksapivb6.chm::/sldworks~DimPatternFeatureData~GetInstanceCount.html).

## Examples

[Insert Variable Pattern Feature (C#)](Insert_Advanced_Variable_Pattern_Feature_Example_CSharp.htm)
[Insert Variable Pattern Feature (VB.NET)](Insert_Advanced_Variable_Pattern_Feature_Example_VBNET.htm)
[Insert Variable Pattern Feature (VBA)](Insert_Advanced_Variable_Pattern_Feature_Example_VB.htm)

## See Also

[IDimPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData.html)
[IDimPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
