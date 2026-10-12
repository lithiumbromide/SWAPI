---
title: "CustomRenderSettings Property (IRayTraceRendererOptions)"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRendererOptions"
member: "CustomRenderSettings"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~CustomRenderSettings.html"
---

# CustomRenderSettings Property (IRayTraceRendererOptions)

Gets or sets whether to enable custom render settings.

## Syntax

### Visual Basic (Declaration)

```vb
Property CustomRenderSettings As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRayTraceRendererOptions
Dim value As System.Boolean

instance.CustomRenderSettings = value

value = instance.CustomRenderSettings
```

### C#

```csharp
System.bool CustomRenderSettings {get; set;}
```

### C++/CLI

```cpp
property System.bool CustomRenderSettings {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to enable custom render settings, false to not

## VBA Syntax

See [RayTraceRendererOptions::CustomRenderSettings](ms-its:sldworksapivb6.chm::/sldworks~RayTraceRendererOptions~CustomRenderSettings.html).

## Remarks

Enabling custom render settings allows access to the number of:

- [reflections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~NumberOfReflections.html)
- [refractions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~NumberOfRefractions.html)

in the [final render](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~InvokeFinalRender.html).

## See Also

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.html)
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
