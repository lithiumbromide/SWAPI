---
title: "PropagateVisualProperty Property (ICircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICircularPatternFeatureData"
member: "PropagateVisualProperty"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~PropagateVisualProperty.html"
---

# PropagateVisualProperty Property (ICircularPatternFeatureData)

Gets or sets whether to propagate visual properties (e.g., colors, textures, cosmetic thread data, etc.) to all pattern instances in this circular pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PropagateVisualProperty As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICircularPatternFeatureData
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

See [CircularPatternFeatureData::PropagateVisualProperty](ms-its:sldworksapivb6.chm::/sldworks~CircularPatternFeatureData~PropagateVisualProperty.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.html)
[ICircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
