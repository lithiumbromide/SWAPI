---
title: "PropagateVisualProperty Property (ICurveDrivenPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICurveDrivenPatternFeatureData"
member: "PropagateVisualProperty"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~PropagateVisualProperty.html"
---

# PropagateVisualProperty Property (ICurveDrivenPatternFeatureData)

Gets or sets whether to propagate visual properties (e.g., colors, textures, etc.) to all curve-driven pattern instances.

## Syntax

### Visual Basic (Declaration)

```vb
Property PropagateVisualProperty As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICurveDrivenPatternFeatureData
Dim value As System.Boolean

instance.PropagateVisualProperty = value

value = instance.PropagateVisualProperty
```

### C#

```csharp
System.bool PropagateVisualProperty {get; set;}
```

### C++/CLI

```cpp
property System.bool PropagateVisualProperty {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to propagate all visual properties, false to not

## VBA Syntax

See [CurveDrivenPatternFeatureData::PropagateVisualProperty](ms-its:sldworksapivb6.chm::/sldworks~CurveDrivenPatternFeatureData~PropagateVisualProperty.html).

## See Also

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.html)
[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
