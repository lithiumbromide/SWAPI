---
title: "FeatureCircularPattern3 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "FeatureCircularPattern3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureCircularPattern3.html"
---

# FeatureCircularPattern3 Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::FeatureCircularPattern4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureCircularPattern4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function FeatureCircularPattern3( _
   ByVal Number As System.Integer, _
   ByVal Spacing As System.Double, _
   ByVal FlipDirection As System.Boolean, _
   ByVal DName As System.String, _
   ByVal GeometryPattern As System.Boolean, _
   ByVal EqualSpacing As System.Boolean _
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
Dim value As Feature

value = instance.FeatureCircularPattern3(Number, Spacing, FlipDirection, DName, GeometryPattern, EqualSpacing)
```

### C#

```csharp
Feature FeatureCircularPattern3(
   System.int Number,
   System.double Spacing,
   System.bool FlipDirection,
   System.string DName,
   System.bool GeometryPattern,
   System.bool EqualSpacing
)
```

### C++/CLI

```cpp
Feature^ FeatureCircularPattern3(
   System.int Number,
   System.double Spacing,
   System.bool FlipDirection,
   System.String^ DName,
   System.bool GeometryPattern,
   System.bool EqualSpacing
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Number`: Number of instances of the circular pattern to insert, including the original instance
- `Spacing`: Spacing between each instance of the circular pattern or total angle if EqualSpacing is true (in radians)
- `FlipDirection`: True to flip the direction of the circular pattern, false to not
- `DName`: Name of the angular dimension defining the direction of the pattern
- `GeometryPattern`: True to use geometry pattern, false to not
- `EqualSpacing`: True to use equal spacing, false to not

### Return Value

Circular pattern [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::FeatureCircularPattern3](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~FeatureCircularPattern3.html).

## Remarks

This method requires ordered selection of the features and components.

- Features and axis: Use [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) with a Mark of 4 for the features to pattern and a Mark of 1 for the axis. You can also use [IFeature::Select2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~Select2.html) to select the features and the axis.
- Components and axis: Use IModelDocExtension::SelectByID2 with a Mark of 1 for the components to pattern and a Mark of 2 for the axis.

You must select the features or components before selecting the axis.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
