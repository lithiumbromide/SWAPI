---
title: "DrawingColor Property (IPageSetup)"
project: "SOLIDWORKS API Help"
interface: "IPageSetup"
member: "DrawingColor"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~DrawingColor.html"
---

# DrawingColor Property (IPageSetup)

Sets the color of the drawing for printing.

## Syntax

### Visual Basic (Declaration)

```vb
Property DrawingColor As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPageSetup
Dim value As System.Integer

instance.DrawingColor = value

value = instance.DrawingColor
```

### C#

```csharp
System.int DrawingColor {get; set;}
```

### C++/CLI

```cpp
property System.int DrawingColor {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Color of drawing for printing as defined in [swPageSetupDrawingColor_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPageSetupDrawingColor_e.html)

## VBA Syntax

See [PageSetup::DrawingColor](ms-its:sldworksapivb6.chm::/sldworks~PageSetup~DrawingColor.html).

## Remarks

This method can only be set with an application-level ([IModelDocExtension::AppPageSetup](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~AppPageSetup.html)) or document-level ([IModelDoc2::PageSetup](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~PageSetup.html) or [IModelDoc2::IPageSetup](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IPageSetup.html)) object. This method is not available at the sheet level.

## See Also

[IPageSetup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.html)
[IPageSetup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup_members.html)

## Availability

SOLIDWORKS 2008 SP4, Revision Number 17.0
