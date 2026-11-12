---
title: "SourceSketch Property (IWrapSketchFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWrapSketchFeatureData"
member: "SourceSketch"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWrapSketchFeatureData~SourceSketch.html"
---

# SourceSketch Property (IWrapSketchFeatureData)

Gets or sets the sketch for this wrap feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property SourceSketch As Sketch
```

### Visual Basic (Usage)

```vb
Dim instance As IWrapSketchFeatureData
Dim value As Sketch

instance.SourceSketch = value

value = instance.SourceSketch
```

### C#

```csharp
Sketch SourceSketch {get; set;}
```

### C++/CLI

```cpp
property Sketch^ SourceSketch {
   Sketch^ get();
   void set (    Sketch^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Sketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html)

## VBA Syntax

See [WrapSketchFeatureData::SourceSketch](ms-its:sldworksapivb6.chm::/sldworks~WrapSketchFeatureData~SourceSketch.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IWrapSketchFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWrapSketchFeatureData.html)
[IWrapSketchFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWrapSketchFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
