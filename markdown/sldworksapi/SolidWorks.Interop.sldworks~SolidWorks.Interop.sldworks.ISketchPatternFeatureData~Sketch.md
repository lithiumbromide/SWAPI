---
title: "Sketch Property (ISketchPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISketchPatternFeatureData"
member: "Sketch"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~Sketch.html"
---

# Sketch Property (ISketchPatternFeatureData)

Gets or sets the sketch from which that this sketch pattern feature is created.

## Syntax

### Visual Basic (Declaration)

```vb
Property Sketch As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPatternFeatureData
Dim value As System.Object

instance.Sketch = value

value = instance.Sketch
```

### C#

```csharp
System.object Sketch {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Sketch {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Sketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html) for this pattern

## VBA Syntax

See [SketchPatternFeatureData::Sketch](ms-its:sldworksapivb6.chm::/sldworks~SketchPatternFeatureData~Sketch.html).

## Examples

See the [ISketchPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData.html)
[ISketchPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
