---
title: "WitnessVisibility Property (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "WitnessVisibility"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~WitnessVisibility.html"
---

# WitnessVisibility Property (IDisplayDimension)

Gets or sets which extension lines are visible.

## Syntax

### Visual Basic (Declaration)

```vb
Property WitnessVisibility As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Integer

instance.WitnessVisibility = value

value = instance.WitnessVisibility
```

### C#

```csharp
System.int WitnessVisibility {get; set;}
```

### C++/CLI

```cpp
property System.int WitnessVisibility {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Extension-line visibility state as defined in [swWitnessLineVisibility_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWitnessLineVisibility_e.html)

## VBA Syntax

See [DisplayDimension::WitnessVisibility](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~WitnessVisibility.html).

## Remarks

After using this property, use [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html) to redraw the graphics window to see your changes.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::SmartWitness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SmartWitness.html)
[IDisplayDimension::MaxWitnessLineLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~MaxWitnessLineLength.html)
