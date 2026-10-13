---
title: "AnnotationViewCount Property (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "AnnotationViewCount"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AnnotationViewCount.html"
---

# AnnotationViewCount Property (IModelDocExtension)

Gets the number of annotation views in this part or assembly document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property AnnotationViewCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Integer

value = instance.AnnotationViewCount
```

### C#

```csharp
System.int AnnotationViewCount {get;}
```

### C++/CLI

```cpp
property System.int AnnotationViewCount {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of annotation views in this model document

## VBA Syntax

See [ModelDocExtension::AnnotationViewCount](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~AnnotationViewCount.html).

## Examples

[Move Annotations to Notes Area Annotation View (C#)](Move_Annotations_to_First_Annotation_View_Example_CSharp.htm)
[Move Annotations to Notes Area Annotation View (VB.NET)](Move_Annotations_to_First_Annotation_View_Example_VBNET.htm)
[Move Annotations to Notes Area Annotation View (VBA)](Move_Annotations_to_First_Annotation_View_Example_VB.htm)

## Remarks

Call this method before calling [IModelDocExtension::IGetAnnotationViews](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~IGetAnnotationViews.html) to get the size of the array for that method.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::IGetAnnotationViews Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetAnnotationViews.html)
[IModelDocExtension::AnnotationViews Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AnnotationViews.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
