---
title: "UseSceneBackgroundImageAspectRatio Property (IRayTraceRendererOptions)"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRendererOptions"
member: "UseSceneBackgroundImageAspectRatio"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~UseSceneBackgroundImageAspectRatio.html"
---

# UseSceneBackgroundImageAspectRatio Property (IRayTraceRendererOptions)

Gets or sets whether to use the aspect ratio of the scene's background image for ray-trace rendering engine preview and final renders.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseSceneBackgroundImageAspectRatio As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRayTraceRendererOptions
Dim value As System.Boolean

instance.UseSceneBackgroundImageAspectRatio = value

value = instance.UseSceneBackgroundImageAspectRatio
```

### C#

```csharp
System.bool UseSceneBackgroundImageAspectRatio {get; set;}
```

### C++/CLI

```cpp
property System.bool UseSceneBackgroundImageAspectRatio {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use the aspect ratio of the scene's background image for ray-trace rendering engine preview and final renders, false to not

## VBA Syntax

See [RayTraceRendererOptions::UseSceneBackgroundImageAspectRatio](ms-its:sldworksapivb6.chm::/sldworks~RayTraceRendererOptions~UseSceneBackgroundImageAspectRatio.html).

## See Also

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.html)
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.html)
[IRayTraceRendererOptions::UseSolidWorksViewAspectRatio Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~UseSolidWorksViewAspectRatio.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
