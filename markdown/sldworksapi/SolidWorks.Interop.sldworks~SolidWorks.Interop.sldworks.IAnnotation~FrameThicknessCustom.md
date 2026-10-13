---
title: "FrameThicknessCustom Property (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "FrameThicknessCustom"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~FrameThicknessCustom.html"
---

# FrameThicknessCustom Property (IAnnotation)

Gets or sets the frame's line thickness for this annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Property FrameThicknessCustom As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim value As System.Double

instance.FrameThicknessCustom = value

value = instance.FrameThicknessCustom
```

### C#

```csharp
System.double FrameThicknessCustom {get; set;}
```

### C++/CLI

```cpp
property System.double FrameThicknessCustom {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Value of frame's line thickness

## VBA Syntax

See [Annotation::FrameThicknessCustom](ms-its:sldworksapivb6.chm::/sldworks~Annotation~FrameThicknessCustom.html).

## Remarks

[IAnnotation::UseDocDispFrame](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~UseDocDispFrame.html) must be false for this property to have any effect.

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[IAnnotation::FrameLineStyle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~FrameLineStyle.html)
[IAnnotation::FrameThickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~FrameThickness.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
