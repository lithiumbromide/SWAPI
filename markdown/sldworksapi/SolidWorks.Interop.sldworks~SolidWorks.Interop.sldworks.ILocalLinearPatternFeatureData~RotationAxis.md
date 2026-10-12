---
title: "RotationAxis Property (ILocalLinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalLinearPatternFeatureData"
member: "RotationAxis"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~RotationAxis.html"
---

# RotationAxis Property (ILocalLinearPatternFeatureData)

Gets or sets the axis of rotation of components in this linear component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property RotationAxis As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalLinearPatternFeatureData
Dim value As System.Object

instance.RotationAxis = value

value = instance.RotationAxis
```

### C#

```csharp
System.object RotationAxis {get; set;}
```

### C++/CLI

```cpp
property System.Object^ RotationAxis {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.html), [line](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.html), or [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html) around which the pattern components rotate

## VBA Syntax

See [LocalLinearPatternFeatureData::RotationAxis](ms-its:sldworksapivb6.chm::/sldworks~LocalLinearPatternFeatureData~RotationAxis.html).

## Remarks

This property is valid only if [ILocalLinearPatternFeatureData::RotateInstances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~RotateInstances.html) is true.

The rotation axis must be parallel to [ILocalLinearPatternFeatureData::D1Axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1Axis.html).

Use:

- [ILocalLinearPatternFeatureData::FixedAxisOfRotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~FixedAxisOfRotation.html) to specify whether all instances of components rotate about this rotation axis.

- [ILocalLinearPatternFeatureData::ReverseAxisOfRotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~ReverseAxisOfRotation.html) to reverse the direction of this rotation axis.

You cannot edit this property to null or Nothing after the feature is first created with a rotation axis. If you try, [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.html) returns false and the feature does not roll back. To roll back the feature, call [IModelDoc2::ForceRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceRebuild3.html) or move the rollback bar in the user interface to before and after the feature.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

For more information, see the **Linear Component Pattern PropertyManager** topic in the SOLIDWORKS Design user-interface help.

## See Also

[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.html)
[ILocalLinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
