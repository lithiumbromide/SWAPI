---
title: "IncludeAnnotationsInRendering Property (IRayTraceRendererOptions)"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRendererOptions"
member: "IncludeAnnotationsInRendering"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~IncludeAnnotationsInRendering.html"
---

# IncludeAnnotationsInRendering Property (IRayTraceRendererOptions)

Gets or sets whether to include annotations and dimensions visible in the model when [rendering to a file](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~RenderToFile.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeAnnotationsInRendering As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRayTraceRendererOptions
Dim value As System.Boolean

instance.IncludeAnnotationsInRendering = value

value = instance.IncludeAnnotationsInRendering
```

### C#

```csharp
System.bool IncludeAnnotationsInRendering {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeAnnotationsInRendering {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to include annotations and dimensions visible in the model when rendering to a file, false to not

## VBA Syntax

See [RayTraceRendererOptions::IncludeAnnotationsInRendering](ms-its:sldworksapivb6.chm::/sldworks~RayTraceRendererOptions~IncludeAnnotationsInRendering.html).

## Examples

[Include Note in Render File (C#)](Include_Note_in_Render_File_Example_CSharp.htm)
[Include Note in Render File (VB.NET)](Include_Note_in_Render_File_Example_VBNET.htm)
[Include Note in Render File (VBA)](Include_Note_in_Render_File_Example_VB.htm)

## Remarks

This property is only available when rendering to a file; this property is not available when only [invoking the final render window](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~InvokeFinalRender.html).

To render the annotations and dimensions visible in the model to a separate image file, call [IRayTraceRendererOptions::RenderAnnotationsToSeparateImage](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~RenderAnnotationsToSeparateImage.html).

## See Also

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.html)
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
