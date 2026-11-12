---
title: "FeatureScopeBodies Property (ISimpleHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleHoleFeatureData2"
member: "FeatureScopeBodies"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~FeatureScopeBodies.html"
---

# FeatureScopeBodies Property (ISimpleHoleFeatureData2)

Gets or sets the solid bodies that the simple hole feature affects in a multibody part.

## Syntax

### Visual Basic (Declaration)

```vb
Property FeatureScopeBodies As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleHoleFeatureData2
Dim value As System.Object

instance.FeatureScopeBodies = value

value = instance.FeatureScopeBodies
```

### C#

```csharp
System.object FeatureScopeBodies {get; set;}
```

### C++/CLI

```cpp
property System.Object^ FeatureScopeBodies {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of solid [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) that the simple hole feature affects

## VBA Syntax

See [SimpleHoleFeatureData2::FeatureScopeBodies](ms-its:sldworksapivb6.chm::/sldworks~SimpleHoleFeatureData2~FeatureScopeBodies.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISimpleHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2.html)
[ISimpleHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2_members.html)
[ISimpleHoleFeatureData2::GetFeatureScopeBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~GetFeatureScopeBodiesCount.html)
[ISimpleHoleFeatureData2::IGetFeatureScopeBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~IGetFeatureScopeBodies.html)
[ISimpleHoleFeatureData2::ISetFeatureScopeBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~ISetFeatureScopeBodies.html)
[ISimpleHoleFeatureData2::AutoSelect Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~AutoSelect.html)
[ISimpleHoleFeatureData2::FeatureScope Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~FeatureScope.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
