---
title: "SolidLeader Property (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "SolidLeader"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SolidLeader.html"
---

# SolidLeader Property (IDisplayDimension)

Gets or sets whether this display dimension is displayed with a solid leader for arc and radial dimensions.

## Syntax

### Visual Basic (Declaration)

```vb
Property SolidLeader As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Boolean

instance.SolidLeader = value

value = instance.SolidLeader
```

### C#

```csharp
System.bool SolidLeader {get; set;}
```

### C++/CLI

```cpp
property System.bool SolidLeader {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True displays a solid leader, false does not

## VBA Syntax

See [DisplayDimension::SolidLeader](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~SolidLeader.html).

## Remarks

After using this property, use [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html) to redraw the graphics window to see your changes.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::SetBrokenLeader2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetBrokenLeader2.html)
[IDisplayDimension::GetUseDocBrokenLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocBrokenLeader.html)
[IDisplayDimension::GetBrokenLeader2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetBrokenLeader2.html)

## Availability

SOLIDWORKS 99, datecode 1999207
