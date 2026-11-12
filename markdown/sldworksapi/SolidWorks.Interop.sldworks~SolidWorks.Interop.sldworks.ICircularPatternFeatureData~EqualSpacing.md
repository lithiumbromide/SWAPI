---
title: "EqualSpacing Property (ICircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICircularPatternFeatureData"
member: "EqualSpacing"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~EqualSpacing.html"
---

# EqualSpacing Property (ICircularPatternFeatureData)

Gets or sets whether the pattern instances in Direction 1 are equally spaced in this circular pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property EqualSpacing As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICircularPatternFeatureData
Dim value As System.Boolean

instance.EqualSpacing = value

value = instance.EqualSpacing
```

### C#

```csharp
System.bool EqualSpacing {get; set;}
```

### C++/CLI

```cpp
property System.bool EqualSpacing {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use equal spacing in Direction 1, false to not

## VBA Syntax

See [CircularPatternFeatureData::EqualSpacing](ms-its:sldworksapivb6.chm::/sldworks~CircularPatternFeatureData~EqualSpacing.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.html)
[ICircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.html)
[ICircularPatternFeatureData::TotalInstances Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~TotalInstances.html)
[ICircularPatternFeatureData::Spacing Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~Spacing.html)
[ICircularPatternFeatureData::EqualSpacing2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~EqualSpacing2.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
