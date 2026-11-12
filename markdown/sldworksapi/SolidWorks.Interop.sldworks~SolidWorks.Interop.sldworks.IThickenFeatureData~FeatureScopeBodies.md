---
title: "FeatureScopeBodies Property (IThickenFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IThickenFeatureData"
member: "FeatureScopeBodies"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData~FeatureScopeBodies.html"
---

# FeatureScopeBodies Property (IThickenFeatureData)

Gets or sets the solid bodies that the thicken feature affects in a multibody part.

## Syntax

### Visual Basic (Declaration)

```vb
Property FeatureScopeBodies As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IThickenFeatureData
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

Array of solid [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) that the feature affects

## VBA Syntax

See [ThickenFeatureData::FeatureScopeBodies](ms-its:sldworksapivb6.chm::/sldworks~ThickenFeatureData~FeatureScopeBodies.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IThickenFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData.html)
[IThickenFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData_members.html)
[IThickenFeatureData::GetFeatureScopeBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData~GetFeatureScopeBodiesCount.html)
[IThickenFeatureData::IGetFeatureScopeBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData~IGetFeatureScopeBodies.html)
[IThickenFeatureData::ISetFeatureScopeBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData~ISetFeatureScopeBodies.html)
[IThickenFeatureData::AutoSelect Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData~AutoSelect.html)
[IThickenFeatureData::FeatureScope Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData~FeatureScope.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
