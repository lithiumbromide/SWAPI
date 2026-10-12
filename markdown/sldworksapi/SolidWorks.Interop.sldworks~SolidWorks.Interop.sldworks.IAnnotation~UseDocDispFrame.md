---
title: "UseDocDispFrame Property (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "UseDocDispFrame"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~UseDocDispFrame.html"
---

# UseDocDispFrame Property (IAnnotation)

Gets or sets whether to use the document's frame's line style and thickness or a specified line style and thickness for this annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseDocDispFrame As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim value As System.Boolean

instance.UseDocDispFrame = value

value = instance.UseDocDispFrame
```

### C#

```csharp
System.bool UseDocDispFrame {get; set;}
```

### C++/CLI

```cpp
property System.bool UseDocDispFrame {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use the document's frame's line style and thickness, false to use a specified line style and thickness

## VBA Syntax

See [Annotation::UseDocDispFrame](ms-its:sldworksapivb6.chm::/sldworks~Annotation~UseDocDispFrame.html).

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[IAnnotation::FrameLineStyle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~FrameLineStyle.html)
[IAnnotation::FrameThickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~FrameThickness.html)
[IAnnotation::FrameThicknessCustom Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~FrameThicknessCustom.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
