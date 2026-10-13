---
title: "RenderAnnotationsToSeparateImage Property (IRayTraceRendererOptions)"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRendererOptions"
member: "RenderAnnotationsToSeparateImage"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~RenderAnnotationsToSeparateImage.html"
---

# RenderAnnotationsToSeparateImage Property (IRayTraceRendererOptions)

Gets or sets whether to render annotations and dimensions visible in the model to a separate image file.

## Syntax

### Visual Basic (Declaration)

```vb
Property RenderAnnotationsToSeparateImage As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRayTraceRendererOptions
Dim value As System.Boolean

instance.RenderAnnotationsToSeparateImage = value

value = instance.RenderAnnotationsToSeparateImage
```

### C#

```csharp
System.bool RenderAnnotationsToSeparateImage {get; set;}
```

### C++/CLI

```cpp
property System.bool RenderAnnotationsToSeparateImage {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to render annotations and dimensions visible in the model to a separate image file, false to not

## VBA Syntax

See [RayTraceRendererOptions::RenderAnnotationsToSeparateImage](ms-its:sldworksapivb6.chm::/sldworks~RayTraceRendererOptions~RenderAnnotationsToSeparateImage.html).

## Examples

[Render Annotations to Separate Image File (C#)](Render_Annotations_to_Separate_Image_File_Example_CSharp.htm)
[Render Annotations to Separate Image File (VB.NET)](Render_Annotations_to_Separate_Image_File_Example_VBNET.htm)
[Render Annotations to Separate Image File (VBA)](Render_Annotations_to_Separate_Image_File_Example_VB.htm)

## Remarks

This property is only available when:

- [rendering to a file](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~RenderToFile.html). This property is not available when only [invoking the final render window](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~InvokeFinalRender.html).
- [IRayTraceRendererOptions::IncludeAnnotationsInRendering](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~IncludeAnnotationsInRendering.html) is set to true.

When this property is set to true, then SOLIDWORKS API appends **_1** to the name of the render file. For example, if you named the render file **abc.png**, then this property creates a file named **abc_1.png** that contains only the annotations and dimensions visible in the model.

## See Also

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.html)
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
