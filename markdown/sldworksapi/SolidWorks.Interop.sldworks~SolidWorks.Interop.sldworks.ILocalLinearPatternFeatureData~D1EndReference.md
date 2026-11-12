---
title: "D1EndReference Property (ILocalLinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalLinearPatternFeatureData"
member: "D1EndReference"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1EndReference.html"
---

# D1EndReference Property (ILocalLinearPatternFeatureData)

Gets or sets the up-to reference entity in Direction 1 for this linear component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D1EndReference As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalLinearPatternFeatureData
Dim value As System.Object

instance.D1EndReference = value

value = instance.D1EndReference
```

### C#

```csharp
System.object D1EndReference {get; set;}
```

### C++/CLI

```cpp
property System.Object^ D1EndReference {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pattern's up-to reference ([vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html), [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html), [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html), or [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html)) in Direction 1

## VBA Syntax

See [LocalLinearPatternFeatureData::D1EndReference](ms-its:sldworksapivb6.chm::/sldworks~LocalLinearPatternFeatureData~D1EndReference.html).

## Remarks

This property is valid only if [ILocalLinearPatternFeatureData::D1EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1EndCondition.html) is set to [swPatternEndCondition_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternEndCondition_e.html).swPatternEndCondition_UpToReference.

To pre-select, use selection Mark = 256.

During edit of this property, if you specify an invalid entity [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.html) returns false and the feature does not roll back. To roll back the feature, call [IModelDoc2::ForceRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceRebuild3.html) or move the rollback bar in the user interface to before and after the feature.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

For more information, see the **Linear Component Pattern PropertyManager** topic in the SOLIDWORKS Design user-interface help.

## See Also

[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.html)
[ILocalLinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.html)
[ILocalLinearPatternFeatureData::D1EndReferenceType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1EndReferenceType.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
