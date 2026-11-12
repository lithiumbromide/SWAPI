---
title: "PropagateVisualProperties Property (IDimPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDimPatternFeatureData"
member: "PropagateVisualProperties"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~PropagateVisualProperties.html"
---

# PropagateVisualProperties Property (IDimPatternFeatureData)

Gets or sets whether to propagate visual properties (e.g., colors, textures, etc.) to all variable pattern instances.

## Syntax

### Visual Basic (Declaration)

```vb
Property PropagateVisualProperties As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimPatternFeatureData
Dim value As System.Boolean

instance.PropagateVisualProperties = value

value = instance.PropagateVisualProperties
```

### C#

```csharp
System.bool PropagateVisualProperties {get; set;}
```

### C++/CLI

```cpp
property System.bool PropagateVisualProperties {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to propagate visual properties, false to not

## VBA Syntax

See [DimPatternFeatureData::PropagateVisualProperties](ms-its:sldworksapivb6.chm::/sldworks~DimPatternFeatureData~PropagateVisualProperties.html).

## Examples

[Delete Instances and Dimensions in Variable Pattern Feature (C#)](Delete_Instances_and_Dimensions_in_Variable_Pattern_Feature_Example_CSharp.htm)
[Delete Instances and Dimensions in Variable Pattern Feature (VB.NET)](Delete_Instances_and_Dimensions_in_Variable_Pattern_Feature_Example_VBNET.htm)
[Delete Instances and Dimensions in Variable Pattern Feature (VBA)](Delete_Instances_and_Dimensions_in_Variable_Pattern_Feature_Example_VB.htm)

## See Also

[IDimPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData.html)
[IDimPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
