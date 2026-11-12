---
title: "InsertVaryInstanceOverride Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertVaryInstanceOverride"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertVaryInstanceOverride.html"
---

# InsertVaryInstanceOverride Method (IFeatureManager)

Obsolete. Superseded by [IInstanceToVaryOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertVaryInstanceOverride( _
   ByVal DName As System.String, _
   ByVal PatternType As System.Integer, _
   ByVal OverrideType As System.Integer, _
   ByVal Direction As System.Integer, _
   ByVal InstanceRowIndex As System.Integer, _
   ByVal InstanceColumnIndex As System.Integer, _
   ByVal OverrideValue As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim DName As System.String
Dim PatternType As System.Integer
Dim OverrideType As System.Integer
Dim Direction As System.Integer
Dim InstanceRowIndex As System.Integer
Dim InstanceColumnIndex As System.Integer
Dim OverrideValue As System.Double
Dim value As System.Boolean

value = instance.InsertVaryInstanceOverride(DName, PatternType, OverrideType, Direction, InstanceRowIndex, InstanceColumnIndex, OverrideValue)
```

### C#

```csharp
System.bool InsertVaryInstanceOverride(
   System.string DName,
   System.int PatternType,
   System.int OverrideType,
   System.int Direction,
   System.int InstanceRowIndex,
   System.int InstanceColumnIndex,
   System.double OverrideValue
)
```

### C++/CLI

```cpp
System.bool InsertVaryInstanceOverride(
   System.String^ DName,
   System.int PatternType,
   System.int OverrideType,
   System.int Direction,
   System.int InstanceRowIndex,
   System.int InstanceColumnIndex,
   System.double OverrideValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DName`:

  | If OverrideType is... | Then set DName to... |
  | --- | --- |
  | 1 | Name of the pattern instance dimension to override |
  | 2 | "Spacing Increment" |
- `PatternType`: Type of pattern (see **Remarks**):

  - 2 = linear
  - 4 = circular
  - 256 = variable
- `OverrideType`: Type of increment override:

  - 1 = dimension
  - 2 = spacing
- `Direction`: Direction in which to apply the spacing override.

  | If OverrideType is ... | Then set Direction to ... |
  | --- | --- |
  | 2 | 0 = direction 1 1 = direction 2 |
  | 1 | -1 |
- `InstanceRowIndex`: 0 < row index of the instance to modify < number of instances per row
- `InstanceColumnIndex`: 0 < column index of the instance to modify < number of instances per column; valid only for PatternType = 2
- `OverrideValue`: Value to override the current value of the dimension or spacing of the specified instance

### Return Value

True if the override is applied successfully, false if not

## VBA Syntax

See [FeatureManager::InsertVaryInstanceIncrement](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertVaryInstanceIncrement.html).

## Remarks

To vary the dimensions or spacings of pattern instances:

1. Call this method multiple times to override multiple dimensions or spacings of pattern instances.
2. Call [IFeatureManager::InsertVaryInstanceIncrement](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertVaryInstanceIncrement.html) multiple times to increment multiple dimensions or spacings of pattern instances.

| If PatternType is... | Call IFeatureManager::CreateFeature(...) |
| --- | --- |
| 2 | LinearPatternFeatureData object |
| 4 | CircularPatternFeatureData object |
| 256 | DimPatternFeatureData object |

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
