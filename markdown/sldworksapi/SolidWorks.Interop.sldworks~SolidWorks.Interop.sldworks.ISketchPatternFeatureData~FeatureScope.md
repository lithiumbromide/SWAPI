---
title: "FeatureScope Property (ISketchPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISketchPatternFeatureData"
member: "FeatureScope"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~FeatureScope.html"
---

# FeatureScope Property (ISketchPatternFeatureData)

Gets which bodies in this multibody part are affected by this sketch-driven pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FeatureScope As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPatternFeatureData
Dim value As System.Boolean

value = instance.FeatureScope
```

### C#

```csharp
System.bool FeatureScope {get;}
```

### C++/CLI

```cpp
property System.bool FeatureScope {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to specify affected bodies, false to apply the pattern to all bodies every time the feature regenerates

## VBA Syntax

See [SketchPatternFeatureData::FeatureScope](ms-its:sldworksapivb6.chm::/sldworks~SketchPatternFeatureData~FeatureScope.html).

## Remarks

This property is valid only if [ISketchPatternFeatureData::GeometryPattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~GeometryPattern.html) is true.

Call [ISketchPatternFeatureData::SetFeatureScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~SetFeatureScope.html) to set this property.

For more information, see the **Sketch Driven Patterns PropertyManager** topic in the SOLIDWORKS Design user-interface help.

## See Also

[ISketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData.html)
[ISketchPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
