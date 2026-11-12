---
title: "FeatureScope Property (IMirrorPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorPatternFeatureData"
member: "FeatureScope"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~FeatureScope.html"
---

# FeatureScope Property (IMirrorPatternFeatureData)

Gets or sets whether to use scope for the mirror pattern feature in a multibody part.

## Syntax

### Visual Basic (Declaration)

```vb
Property FeatureScope As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorPatternFeatureData
Dim value As System.Integer

instance.FeatureScope = value

value = instance.FeatureScope
```

### C#

```csharp
System.int FeatureScope {get; set;}
```

### C++/CLI

```cpp
property System.int FeatureScope {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Feature scope option as defined in [swFeatureScope_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureScope_e.html)

## VBA Syntax

See [MirrorPatternFeatureData::FeatureScope](ms-its:sldworksapivb6.chm::/Sldworks~MirrorPatternFeatureData~FeatureScope.html).

## Remarks

This property is valid only if [IMirrorPatternFeatureData::GeometryPattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~GeometryPattern.html) is true.

If this property is set to either swFeatureScope_SelectedBodiesWithAutoSelect or swFeatureScope_SelectedBodiesWithOutAutoSelect, you can use [IMirrorPatternFeatureData::FeatureScopeBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~FeatureScopeBodies.html) to specify affected bodies.

For more information, see the **Mirror Feature PropertyManager** topic in the SOLIDWORKS Design user-interface help.

## See Also

[IMirrorPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData.html)
[IMirrorPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData_members.html)
[IMirrorPatternFeatureData::GetFeatureScopeBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~GetFeatureScopeBodiesCount.html)
[IMirrorPatternFeatureData::IGetFeatureScopeBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~IGetFeatureScopeBodies.html)
[IMirrorPatternFeatureData::ISetFeatureScopeBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~ISetFeatureScopeBodies.html)
[IMirrorPatternFeatureData::FeatureScopeBodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~FeatureScopeBodies.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
