---
title: "FrameThickness Property (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "FrameThickness"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~FrameThickness.html"
---

# FrameThickness Property (IAnnotation)

Gets or sets the frame's line thickness for this annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Property FrameThickness As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim value As System.Integer

instance.FrameThickness = value

value = instance.FrameThickness
```

### C#

```csharp
System.int FrameThickness {get; set;}
```

### C++/CLI

```cpp
property System.int FrameThickness {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Frame's line thickness as defined by [swLineWeights_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html)

## VBA Syntax

See [Annotation::FrameThickness](ms-its:sldworksapivb6.chm::/sldworks~Annotation~FrameThickness.html).

## Remarks

[IAnnotation::UseDocDispFrame](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~UseDocDispFrame.html) must be false for this property to have any effect.

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[IAnnotation::FrameLineStyle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~FrameLineStyle.html)
[IAnnotation::FrameThicknessCustom Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~FrameThicknessCustom.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
