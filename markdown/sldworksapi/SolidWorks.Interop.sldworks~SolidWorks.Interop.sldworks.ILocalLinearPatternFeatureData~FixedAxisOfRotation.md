---
title: "FixedAxisOfRotation Property (ILocalLinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalLinearPatternFeatureData"
member: "FixedAxisOfRotation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~FixedAxisOfRotation.html"
---

# FixedAxisOfRotation Property (ILocalLinearPatternFeatureData)

Gets or sets whether patterned instances rotate around a common axis.

## Syntax

### Visual Basic (Declaration)

```vb
Property FixedAxisOfRotation As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalLinearPatternFeatureData
Dim value As System.Boolean

instance.FixedAxisOfRotation = value

value = instance.FixedAxisOfRotation
```

### C#

```csharp
System.bool FixedAxisOfRotation {get; set;}
```

### C++/CLI

```cpp
property System.bool FixedAxisOfRotation {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if patterned instances rotate around [ILocalLinearPatternFeatureData::RotationAxis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~RotationAxis.html), false if each instance rotates about its own axis

## VBA Syntax

See [LocalLinearPatternFeatureData::FixedAxisOfRotation](ms-its:sldworksapivb6.chm::/sldworks~LocalLinearPatternFeatureData~FixedAxisOfRotation.html).

## Remarks

This property is valid only if [ILocalLinearPatternFeatureData::RotateInstances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~RotateInstances.html) is true.

If this property is set to:

- True, then you can also specify [ILocalLinearPatternFeatureData::AlignToSeed](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~AlignToSeed.html).
- False, then the rotation axis of each instance of a component is translated along Direction 1 and then rotated following the axis of rotation for that component.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

For more information, see the **Linear Component Pattern PropertyManager** topic in the SOLIDWORKS Design user-interface help.

## See Also

[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.html)
[ILocalLinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
