---
title: "InsertVaryInstanceIncrement Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertVaryInstanceIncrement"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertVaryInstanceIncrement.html"
---

# InsertVaryInstanceIncrement Method (IFeatureManager)

Obsolete. Superseded by [IInstanceToVaryOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertVaryInstanceIncrement( _
   ByVal DName As System.String, _
   ByVal PatternType As System.Integer, _
   ByVal IncrementType As System.Integer, _
   ByVal Direction As System.Integer, _
   ByVal IncrementValue As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim DName As System.String
Dim PatternType As System.Integer
Dim IncrementType As System.Integer
Dim Direction As System.Integer
Dim IncrementValue As System.Double
Dim value As System.Boolean

value = instance.InsertVaryInstanceIncrement(DName, PatternType, IncrementType, Direction, IncrementValue)
```

### C#

```csharp
System.bool InsertVaryInstanceIncrement(
   System.string DName,
   System.int PatternType,
   System.int IncrementType,
   System.int Direction,
   System.double IncrementValue
)
```

### C++/CLI

```cpp
System.bool InsertVaryInstanceIncrement(
   System.String^ DName,
   System.int PatternType,
   System.int IncrementType,
   System.int Direction,
   System.double IncrementValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DName`:

  | If IncrementType is... | Then set DName to... |
  | --- | --- |
  | 1 | Name of the pattern instance dimension to increment |
  | 2 | "Spacing Increment" |
- `PatternType`: Type of pattern (see **Remarks**):

  - 2 = linear
  - 4 = circular
  - 256 = table-driven
- `IncrementType`: Type of increment:

  - 1 = dimension
  - 2 = spacing
- `Direction`: Direction in which to apply the dimension or spacing increment.

  | If PatternType is... | Then set Direction to... |
  | --- | --- |
  | 2 | 0 = direction 1 1 = direction 2 |
  | 4 | 0 = direction 1 |
- `IncrementValue`: Value with which to increment the pattern instance dimension or spacing

### Return Value

True if the increment is applied successfully, false if not

## VBA Syntax

See [FeatureManager::InsertVaryInstanceIncrement](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertVaryInstanceIncrement.html).

## Remarks

To vary the spacings or dimensions of pattern instances:

1. Call this method multiple times to increment multiple dimensions or spacings of pattern instances.
2. Call [IFeatureManager::InsertVaryInstanceOverride](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertVaryInstanceOverride.html) multiple times to override multiple dimensions or spacings of pattern instances.

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
