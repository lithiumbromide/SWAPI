---
title: "FrameLineStyle Property (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "FrameLineStyle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~FrameLineStyle.html"
---

# FrameLineStyle Property (IAnnotation)

Gets or sets the frame's line style for this annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Property FrameLineStyle As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim value As System.Integer

instance.FrameLineStyle = value

value = instance.FrameLineStyle
```

### C#

```csharp
System.int FrameLineStyle {get; set;}
```

### C++/CLI

```cpp
property System.int FrameLineStyle {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Frame's line style as defined by [swLineStyles_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html)

## VBA Syntax

See [Annotation::FrameLineStyle](ms-its:sldworksapivb6.chm::/sldworks~Annotation~FrameLineStyle.html).

## Remarks

[IAnnotation::UseDocDispFrame](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~UseDocDispFrame.html) must be false for this property to have any effect.

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[IAnnotation::FrameThickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~FrameThickness.html)
[IAnnotation::FrameThicknessCustom Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~FrameThicknessCustom.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
