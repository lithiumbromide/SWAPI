---
title: "RotationAngle Property (ILocalLinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalLinearPatternFeatureData"
member: "RotationAngle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~RotationAngle.html"
---

# RotationAngle Property (ILocalLinearPatternFeatureData)

Gets or sets the angle of rotation of instances in this linear component pattern.

## Syntax

### Visual Basic (Declaration)

```vb
Property RotationAngle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalLinearPatternFeatureData
Dim value As System.Double

instance.RotationAngle = value

value = instance.RotationAngle
```

### C#

```csharp
System.double RotationAngle {get; set;}
```

### C++/CLI

```cpp
property System.double RotationAngle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Angle of rotation in radians of pattern instances

## VBA Syntax

See [LocalLinearPatternFeatureData::RotationAngle](ms-its:sldworksapivb6.chm::/sldworks~LocalLinearPatternFeatureData~RotationAngle.html).

## Remarks

This property is valid only if [ILocalLinearPatternFeatureData::RotateInstances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~RotateInstances.html) is true.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

For more information, see the **Linear Component Pattern PropertyManager** topic in the SOLIDWORKS Design user-interface help.

## See Also

[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.html)
[ILocalLinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
