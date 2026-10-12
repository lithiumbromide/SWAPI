---
title: "AddInstanceAt Method (IDimPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDimPatternFeatureData"
member: "AddInstanceAt"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~AddInstanceAt.html"
---

# AddInstanceAt Method (IDimPatternFeatureData)

Adds a pattern instance to this variable pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddInstanceAt( _
   ByVal IsSuppressed As System.Boolean, _
   ByVal Index As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimPatternFeatureData
Dim IsSuppressed As System.Boolean
Dim Index As System.Integer
Dim value As System.Boolean

value = instance.AddInstanceAt(IsSuppressed, Index)
```

### C#

```csharp
System.bool AddInstanceAt(
   System.bool IsSuppressed,
   System.int Index
)
```

### C++/CLI

```cpp
System.bool AddInstanceAt(
   System.bool IsSuppressed,
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `IsSuppressed`: True to suppress this pattern instance, false to not
- `Index`: 0-based index indicating where to add this pattern instance in the pattern table and pattern; -1 indicates to add this pattern instance to the end of the pattern table and pattern (see **Remarks**)

### Return Value

True if the pattern instance is added, false if not

## VBA Syntax

See [DimPatternFeatureData::AddInstanceAt](ms-its:sldworksapivb6.chm::/sldworks~DimPatternFeatureData~AddInstanceAt.html).

## Examples

[Delete and Insert Instances in Variable Pattern Feature (C#)](Delete_and_Insert_Instances_in_Variable_Pattern_Feature_Example_CSharp.htm)
[Delete and Insert Instances in Variable Pattern Feature (VB.NET)](Delete_and_Insert_Instances_in_Variable_Pattern_Feature_Example_VBNET.htm)
[Delete and Insert Instances in Variable Pattern Feature (VBA)](Delete_and_Insert_Instances_in_Variable_Pattern_Feature_Example_VB.htm)

## Remarks

Use [IDimPatternFeatureData::GetInstanceCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceCount.html) to get the number of pattern instances.

By default, this pattern instance inherits the default values of the parent sketch or feature of the variable pattern feature. Use [IDimPatternFeatureData::SetInstanceDimensionValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~SetInstanceDimensionValue.html) to modify this pattern instance's values.

## See Also

[IDimPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData.html)
[IDimPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData_members.html)
[IDimPatternFeatureData::DeleteInstanceAt Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~DeleteInstanceAt.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
