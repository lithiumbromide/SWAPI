---
title: "EqualSpacing Property (ILocalCircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalCircularPatternFeatureData"
member: "EqualSpacing"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~EqualSpacing.html"
---

# EqualSpacing Property (ILocalCircularPatternFeatureData)

Gets or sets whether to equally space the pattern instances in Direction 1 in this circular component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property EqualSpacing As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalCircularPatternFeatureData
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

True to equally space the pattern instances in Direction 1, false to not

## VBA Syntax

See [LocalCircularPatternFeatureData::EqualSpacing](ms-its:sldworksapivb6.chm::/sldworks~LocalCircularPatternFeatureData~EqualSpacing.html).

## Examples

See the [ILocalCircularPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.html) example.

## Remarks

If this property is set to true, then [ILocalCircularPatternFeatureData::Spacing](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~Spacing.html) is automatically set to 360 degrees.

## See Also

[ILocalCircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.html)
[ILocalCircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData_members.html)
[ILocalCircularPatternFeatureData::EqualSpacing2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~EqualSpacing2.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
