---
title: "UseSolidWorksViewAspectRatio Property (IRayTraceRendererOptions)"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRendererOptions"
member: "UseSolidWorksViewAspectRatio"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~UseSolidWorksViewAspectRatio.html"
---

# UseSolidWorksViewAspectRatio Property (IRayTraceRendererOptions)

Gets or sets whether to use the aspect ratio of the SOLIDWORKS view for ray-trace rendering engine preview and final renders.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseSolidWorksViewAspectRatio As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRayTraceRendererOptions
Dim value As System.Boolean

instance.UseSolidWorksViewAspectRatio = value

value = instance.UseSolidWorksViewAspectRatio
```

### C#

```csharp
System.bool UseSolidWorksViewAspectRatio {get; set;}
```

### C++/CLI

```cpp
property System.bool UseSolidWorksViewAspectRatio {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use the aspect ratio of the SOLIDWORKS view for ray-trace rendering engine preview and final renders, false to not

## VBA Syntax

See [RayTraceRendererOptions::UseSolidWorksViewAspectRatio](ms-its:sldworksapivb6.chm::/sldworks~RayTraceRendererOptions~UseSolidWorksViewAspectRatio.html).

## Examples

See the [IRayTraceRendererOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.html) examples.

## See Also

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.html)
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.html)
[IRayTraceRendererOptions::UseSceneBackgroundImageAspectRatio Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~UseSceneBackgroundImageAspectRatio.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
