---
title: "SmartWitness Property (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "SmartWitness"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SmartWitness.html"
---

# SmartWitness Property (IDisplayDimension)

Gets or sets the smart display of extension lines.

## Syntax

### Visual Basic (Declaration)

```vb
Property SmartWitness As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Boolean

instance.SmartWitness = value

value = instance.SmartWitness
```

### C#

```csharp
System.bool SmartWitness {get; set;}
```

### C++/CLI

```cpp
property System.bool SmartWitness {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True uses extension line smart display, false does not

## VBA Syntax

See [DisplayDimension::SmartWitness](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~SmartWitness.html).

## Examples

[Get Display Dimension Properties (VBA)](Get_Display_Dimension_Properties_Example_VB.htm)

## Remarks

After using this property, use [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html) to redraw the graphics window to see your changes.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::MaxWitnessLineLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~MaxWitnessLineLength.html)
[IDisplayDimension::WitnessVisibility Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~WitnessVisibility.html)
