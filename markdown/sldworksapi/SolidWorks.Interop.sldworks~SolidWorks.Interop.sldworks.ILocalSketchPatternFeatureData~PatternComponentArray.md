---
title: "PatternComponentArray Property (ILocalSketchPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalSketchPatternFeatureData"
member: "PatternComponentArray"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData~PatternComponentArray.html"
---

# PatternComponentArray Property (ILocalSketchPatternFeatureData)

Gets or sets the components to pattern for this sketch-driven component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PatternComponentArray As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalSketchPatternFeatureData
Dim value As System.Object

instance.PatternComponentArray = value

value = instance.PatternComponentArray
```

### C#

```csharp
System.object PatternComponentArray {get; set;}
```

### C++/CLI

```cpp
property System.Object^ PatternComponentArray {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)

## VBA Syntax

See [LocalSketchPatternFeatureData::PatternComponentArray](ms-its:sldworksapivb6.chm::/sldworks~LocalSketchPatternFeatureData~PatternComponentArray.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ILocalSketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData.html)
[ILocalSketchPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData_members.html)
[ILocalSketchPatternFeatureData::GetPatternComponentCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData~GetPatternComponentCount.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
