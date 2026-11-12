---
title: "PropagateVisualProperty Property (ITablePatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ITablePatternFeatureData"
member: "PropagateVisualProperty"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~PropagateVisualProperty.html"
---

# PropagateVisualProperty Property (ITablePatternFeatureData)

Gets or sets whether to propagate visual properties (e.g., colors, textures, etc.) in the table-driven pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PropagateVisualProperty As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITablePatternFeatureData
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

True to propagate visual properties, false to not

## VBA Syntax

See [TablePatternFeatureData::PropagateVisualProperty](ms-its:sldworksapivb6.chm::/sldworks~TablePatternFeatureData~PropagateVisualProperty.html).

## Examples

See the [ITablePatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.html) example.

## See Also

[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.html)
[ITablePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
