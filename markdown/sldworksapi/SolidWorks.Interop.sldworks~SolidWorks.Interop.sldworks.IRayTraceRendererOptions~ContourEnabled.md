---
title: "ContourEnabled Property (IRayTraceRendererOptions)"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRendererOptions"
member: "ContourEnabled"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ContourEnabled.html"
---

# ContourEnabled Property (IRayTraceRendererOptions)

Obsolete. Superseded by [IRayTraceRendererOptions::ContourCartoonRenderingEnabled](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ContourCartoonRenderingEnabled.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property ContourEnabled As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRayTraceRendererOptions
Dim value As System.Boolean

instance.ContourEnabled = value

value = instance.ContourEnabled
```

### C#

```csharp
System.bool ContourEnabled {get; set;}
```

### C++/CLI

```cpp
property System.bool ContourEnabled {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to render with contour lines, false to not

## VBA Syntax

See [RayTraceRendererOptions::ContourEnabled](ms-its:sldworksapivb6.chm::/sldworks~RayTraceRendererOptions~ContourEnabled.html).

## See Also

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.html)
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
