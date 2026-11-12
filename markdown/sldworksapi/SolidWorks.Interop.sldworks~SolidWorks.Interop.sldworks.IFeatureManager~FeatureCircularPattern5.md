---
title: "FeatureCircularPattern5 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "FeatureCircularPattern5"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureCircularPattern5.html"
---

# FeatureCircularPattern5 Method (IFeatureManager)

Obsolete. See [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.html) and the Remarks in [ICircularPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.html) and [ILocalCircularPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function FeatureCircularPattern5( _
   ByVal Number As System.Integer, _
   ByVal Spacing As System.Double, _
   ByVal FlipDirection As System.Boolean, _
   ByVal DName As System.String, _
   ByVal GeometryPattern As System.Boolean, _
   ByVal EqualSpacing As System.Boolean, _
   ByVal VaryInstance As System.Boolean, _
   ByVal SyncSubAssemblies As System.Boolean, _
   ByVal BDir2 As System.Boolean, _
   ByVal BSymmetric As System.Boolean, _
   ByVal Number2 As System.Integer, _
   ByVal Spacing2 As System.Double, _
   ByVal DName2 As System.String, _
   ByVal EqualSpacing2 As System.Boolean _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Number As System.Integer
Dim Spacing As System.Double
Dim FlipDirection As System.Boolean
Dim DName As System.String
Dim GeometryPattern As System.Boolean
Dim EqualSpacing As System.Boolean
Dim VaryInstance As System.Boolean
Dim SyncSubAssemblies As System.Boolean
Dim BDir2 As System.Boolean
Dim BSymmetric As System.Boolean
Dim Number2 As System.Integer
Dim Spacing2 As System.Double
Dim DName2 As System.String
Dim EqualSpacing2 As System.Boolean
Dim value As Feature

value = instance.FeatureCircularPattern5(Number, Spacing, FlipDirection, DName, GeometryPattern, EqualSpacing, VaryInstance, SyncSubAssemblies, BDir2, BSymmetric, Number2, Spacing2, DName2, EqualSpacing2)
```

### C#

```csharp
Feature FeatureCircularPattern5(
   System.int Number,
   System.double Spacing,
   System.bool FlipDirection,
   System.string DName,
   System.bool GeometryPattern,
   System.bool EqualSpacing,
   System.bool VaryInstance,
   System.bool SyncSubAssemblies,
   System.bool BDir2,
   System.bool BSymmetric,
   System.int Number2,
   System.double Spacing2,
   System.string DName2,
   System.bool EqualSpacing2
)
```

### C++/CLI

```cpp
Feature^ FeatureCircularPattern5(
   System.int Number,
   System.double Spacing,
   System.bool FlipDirection,
   System.String^ DName,
   System.bool GeometryPattern,
   System.bool EqualSpacing,
   System.bool VaryInstance,
   System.bool SyncSubAssemblies,
   System.bool BDir2,
   System.bool BSymmetric,
   System.int Number2,
   System.double Spacing2,
   System.String^ DName2,
   System.bool EqualSpacing2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Number`: Number of instances of the circular pattern to insert in Direction 1, including the original instance
- `Spacing`: Spacing between each instance in Direction 1 of the circular pattern or, if EqualSpacing is true, then the total angle in radians
- `FlipDirection`: True to flip the direction of the circular pattern in Direction 1, false to not
- `DName`: Name of the angular dimension defining Direction 1 of the pattern
- `GeometryPattern`: True to use geometry pattern, false to not
- `EqualSpacing`: True to use equal spacing in Direction 1, false to not
- `VaryInstance`: True to vary the dimensions or spacing of individual pattern instances, false to not; valid only if GeometryPattern = false (see **Remarks**)
- `SyncSubAssemblies`: True to move components in the patterned instances when components are moved in the seed flexible subassembly, false to not
- `BDir2`: True to create a bidirectional circular pattern feature, false to not
- `BSymmetric`: True to create a symmetric circular pattern feature in Direction 2, false to create an asymmetrical circular pattern feature in Direction 2; valid only if BDir2 is true
- `Number2`: Number of instances to insert in Direction 2; valid only if BDir2 is true
- `Spacing2`: Distance between pattern instances in Direction 2; valid only if BDir2 is true
- `DName2`: Name of the angular dimension defining Direction 2 of the pattern; valid only if BDir2 is true
- `EqualSpacing2`: True to use equal spacing in Direction 2, false to not; valid only if BDir2 is true and BSymmetric is false

### Return Value

Circular pattern [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::FeatureCircularPattern5](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~FeatureCircularPattern5.html).

## Remarks

| If... | To select a feature, use... | To select a component, use... |
| --- | --- | --- |
| Using IModelDocExtension::SelectByID2 to select features and components, ordered selection of the features and components is required | 1 to mark the direction axis 4 to mark the features to pattern | 1 to mark the components to pattern 2 to mark the direction axis |
| Directly selecting a feature or axis using IFeature::Select2 | 1 to mark the direction axis 4 to mark the features to pattern | ISelectData::Mark and Component2::Select3 1 to mark the components to pattern 2 to mark the direction axis |

If VaryInstance = true, then to indicate how to vary the individual pattern instances, decide on the type of pattern and call its corresponding method before calling this method:

| Type | Method |
| --- | --- |
| Increment | IFeatureManager::InsertVaryInstanceIncrement |
| Override | IFeatureManager::InsertVaryInstanceOverride |

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
