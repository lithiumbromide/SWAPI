---
title: "AnnotationViews Property (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "AnnotationViews"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AnnotationViews.html"
---

# AnnotationViews Property (IModelDocExtension)

Gets the annotation views in this part or assembly document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property AnnotationViews As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Object

value = instance.AnnotationViews
```

### C#

```csharp
System.object AnnotationViews {get;}
```

### C++/CLI

```cpp
property System.Object^ AnnotationViews {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [annotation views](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotationView.html) in this part or assembly document

## VBA Syntax

See [IModelDocExtension::AnnotationViews](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~AnnotationViews.html).

## Examples

[Move Annotations to Notes Area Annotation View (C#)](Move_Annotations_to_First_Annotation_View_Example_CSharp.htm)
[Move Annotations to Notes Area Annotation View (VB.NET)](Move_Annotations_to_First_Annotation_View_Example_VBNET.htm)
[Move Annotations to Notes Area Annotation View (VBA)](Move_Annotations_to_First_Annotation_View_Example_VB.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::IGetAnnotationViews Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetAnnotationViews.html)
[IModelDocExtension::AnnotationViewCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AnnotationViewCount.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
