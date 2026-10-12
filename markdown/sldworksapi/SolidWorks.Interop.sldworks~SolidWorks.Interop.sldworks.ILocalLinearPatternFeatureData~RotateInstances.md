---
title: "RotateInstances Property (ILocalLinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalLinearPatternFeatureData"
member: "RotateInstances"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~RotateInstances.html"
---

# RotateInstances Property (ILocalLinearPatternFeatureData)

Gets or sets whether to rotate components in Direction 1 of this linear component pattern.

## Syntax

### Visual Basic (Declaration)

```vb
Property RotateInstances As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalLinearPatternFeatureData
Dim value As System.Boolean

instance.RotateInstances = value

value = instance.RotateInstances
```

### C#

```csharp
System.bool RotateInstances {get; set;}
```

### C++/CLI

```cpp
property System.bool RotateInstances {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to rotate pattern instances, false to not

## VBA Syntax

See [LocalLinearPatternFeatureData::RotateInstances](ms-its:sldworksapivb6.chm::/sldworks~LocalLinearPatternFeatureData~RotateInstances.html).

## Remarks

This property is valid only if [ILocalLinearPatternFeatureData::D1EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1EndCondition.html) is set to [swPatternEndCondition_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternEndCondition_e.html).swPatternEndCondition_SpacingAndInstances.

If you set this property to true, you can also set:

- [ILocalLinearPatternFeatureData::RotationAngle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~RotationAngle.html)
- [ILocalLinearPatternFeatureData::RotationAxis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~RotationAxis.html)
- [ILocalLinearPatternFeatureData::ReverseAxisOfRotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~ReverseAxisOfRotation.html)
- [ILocalLinearPatternFeatureData::FixedAxisOfRotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~FixedAxisOfRotation.html)

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

For more information, see the **Linear Component Pattern PropertyManager** topic in the SOLIDWORKS Design user-interface help.

## See Also

[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.html)
[ILocalLinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
