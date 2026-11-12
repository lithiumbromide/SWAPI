---
title: "TrimByD1 Property (IBoundaryBossFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBoundaryBossFeatureData"
member: "TrimByD1"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~TrimByD1.html"
---

# TrimByD1 Property (IBoundaryBossFeatureData)

Gets whether to trim surfaces in Direction 1 when curves do not form a closed boundary feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property TrimByD1 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBoundaryBossFeatureData
Dim value As System.Boolean

instance.TrimByD1 = value

value = instance.TrimByD1
```

### C#

```csharp
System.bool TrimByD1 {get; set;}
```

### C++/CLI

```cpp
property System.bool TrimByD1 {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to trim surfaces in Direction 1 when curves do not form a closed boundary feature, false to not

## VBA Syntax

See [BoundaryBossFeatureData::TrimByD1](ms-its:sldworksapivb6.chm::/sldworks~BoundaryBossFeatureData~TrimByD1.html).

## Remarks

This property is only available when curves exist in both Direction 1 and Direction 2.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IBoundaryBossFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData.html)
[IBoundaryBossFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData_members.html)
[IBoundaryBossFeatureData::D1Curves Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~D1Curves.html)
[IBoundaryBossFeatureData::D2Curves Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~D2Curves.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
