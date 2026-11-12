---
title: "FeatureScopeBodies Property (ISketchPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISketchPatternFeatureData"
member: "FeatureScopeBodies"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~FeatureScopeBodies.html"
---

# FeatureScopeBodies Property (ISketchPatternFeatureData)

Gets the bodies in this multibody part to be affected by this sketch-driven pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FeatureScopeBodies As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPatternFeatureData
Dim value As System.Object

value = instance.FeatureScopeBodies
```

### C#

```csharp
System.object FeatureScopeBodies {get;}
```

### C++/CLI

```cpp
property System.Object^ FeatureScopeBodies {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html) to be affected

## VBA Syntax

See [SketchPatternFeatureData::FeatureScopeBodies](ms-its:sldworksapivb6.chm::/sldworks~SketchPatternFeatureData~FeatureScopeBodies.html).

## Remarks

This property is valid only if [ISketchPatternFeatureData::GeometryPattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~GeometryPattern.html) is true.

Call [ISketchPatternFeatureData::SetFeatureScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~SetFeatureScope.html) to set this property.

For more information, see the **Sketch Driven Patterns PropertyManager** topic in the SOLIDWORKS Design user-interface help.

## See Also

[ISketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData.html)
[ISketchPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
