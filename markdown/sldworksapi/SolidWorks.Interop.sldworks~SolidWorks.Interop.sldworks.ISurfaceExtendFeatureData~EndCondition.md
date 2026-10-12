---
title: "EndCondition Property (ISurfaceExtendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceExtendFeatureData"
member: "EndCondition"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData~EndCondition.html"
---

# EndCondition Property (ISurfaceExtendFeatureData)

Gets or sets the end condition for this surface-extend feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property EndCondition As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceExtendFeatureData
Dim value As System.Integer

instance.EndCondition = value

value = instance.EndCondition
```

### C#

```csharp
System.int EndCondition {get; set;}
```

### C++/CLI

```cpp
property System.int EndCondition {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

End condition as defined in [swSurfaceExtendEndCond_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSurfaceExtendEndCond_e.html)

## VBA Syntax

See [SurfaceExtendFeatureData::EndCondition](ms-its:sldworksapivb6.chm::/sldworks~SurfaceExtendFeatureData~EndCondition.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfaceExtendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData.html)
[ISurfaceExtendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
