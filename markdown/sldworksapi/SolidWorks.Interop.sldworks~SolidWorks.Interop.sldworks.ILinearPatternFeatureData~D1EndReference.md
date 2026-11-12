---
title: "D1EndReference Property (ILinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearPatternFeatureData"
member: "D1EndReference"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndReference.html"
---

# D1EndReference Property (ILinearPatternFeatureData)

Gets or sets the up-to reference geometry in Direction 1 for this linear pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D1EndReference As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearPatternFeatureData
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

Pattern's up-to reference geometry ([vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html), [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html), [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html), or [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html)) in Direction 1

## VBA Syntax

See [LinearPatternFeatureData::D1EndReference](ms-its:sldworksapivb6.chm::/sldworks~LinearPatternFeatureData~D1EndReference.html).

## Remarks

This property is valid only if [ILinearPatternFeatureData::D1EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndCondition.html) is set to [swPatternEndCondition_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternEndCondition_e.html).swPatternEndCondition_UpToReference.

To control the pattern in Direction 1, also set:

- ILinearPatternFeatureData::D1Axis
- ILinearPatternFeatureData::D1EndRefOffset
- ILinearPatternFeatureData::D1EndRefReverseOffset
- ILinearPatternFeatureData::D1EndUseSeedReference

  - ILinearPatternFeatureData::D1EndSeedReference (if D1EndUseSeedReference is true)
- ILinearPatternFeatureData::D1EndUseSpacing

  - ILinearPatternFeatureData::D1Spacing (if D1EndUseSpacing is true)
  - ILinearPatternFeatureData::D1TotalInstances (if D1EndUseSpacing is false)

For more information, see the **Linear Patterns and the Linear Pattern PropertyManager** topic in the SOLIDWORKS Design user-interface help.

## See Also

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html)
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
