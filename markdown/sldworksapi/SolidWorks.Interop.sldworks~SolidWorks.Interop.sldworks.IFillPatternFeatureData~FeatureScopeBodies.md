---
title: "FeatureScopeBodies Property (IFillPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillPatternFeatureData"
member: "FeatureScopeBodies"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~FeatureScopeBodies.html"
---

# FeatureScopeBodies Property (IFillPatternFeatureData)

Gets or sets the solid bodies that the fill pattern feature affects in a multibody part.

## Syntax

### Visual Basic (Declaration)

```vb
Property FeatureScopeBodies As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFillPatternFeatureData
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

Array of [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) that the fill pattern feature affects

## VBA Syntax

See [FillPatternFeatureData::FeatureScopeBodies](ms-its:sldworksapivb6.chm::/sldworks~FillPatternFeatureData~FeatureScopeBodies.html).

## Remarks

This property is valid only if:

- [IFillPatternFeatureData::GeometryPattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~GeometryPattern.html) is true,
- [IFillPatternFeatureData::FeatureScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~FeatureScope.html) is true,

- and -

- [IFillPatternFeatureData::AutoSelect](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~AutoSelect.html) is false.

You cannot edit this property to null or Nothing after the feature is created with feature scope bodies. If you try, [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.html) returns true but this property does not change.

For more information, see the **Fill Pattern PropertyManager** topic in the SOLIDWORKS Design user-interface help.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html)
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
