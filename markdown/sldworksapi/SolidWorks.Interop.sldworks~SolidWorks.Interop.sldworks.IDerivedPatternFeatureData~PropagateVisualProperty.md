---
title: "PropagateVisualProperty Property (IDerivedPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDerivedPatternFeatureData"
member: "PropagateVisualProperty"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData~PropagateVisualProperty.html"
---

# PropagateVisualProperty Property (IDerivedPatternFeatureData)

Gets or sets whether to propagate visual properties (e.g., colors, textures, etc.) in this derived pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PropagateVisualProperty As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDerivedPatternFeatureData
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

See [DerivedPatternFeatureData::PropagateVisualProperty](ms-its:sldworksapivb6.chm::/sldworks~DerivedPatternFeatureData~PropagateVisualProperty.html).

## Examples

[Get Number of Instances Skipped in Driving Feature (C#)](Get_Number_of_Instances_Skipped_in_Driving_Feature_Example_CSharp.htm)
[Get Number of Instances Skipped in Driving Feature (VB.NET)](Get_Number_of_Instances_Skipped_in_Driving_Feature_Example_VBNET.htm)
[Get Number of Instances Skipped in Driving Feature (VBA)](Get_Number_of_Instances_Skipped_in_Driving_Feature_Example_VB.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IDerivedPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData.html)
[IDerivedPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
