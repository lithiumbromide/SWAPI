---
title: "MaxWitnessLineLength Property (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "MaxWitnessLineLength"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~MaxWitnessLineLength.html"
---

# MaxWitnessLineLength Property (IDisplayDimension)

Gets or sets the maximum length of dimension extension lines.

## Syntax

### Visual Basic (Declaration)

```vb
Property MaxWitnessLineLength As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Double

instance.MaxWitnessLineLength = value

value = instance.MaxWitnessLineLength
```

### C#

```csharp
System.double MaxWitnessLineLength {get; set;}
```

### C++/CLI

```cpp
property System.double MaxWitnessLineLength {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Length

## VBA Syntax

See [DisplayDimension::MaxWitnessLineLength](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~MaxWitnessLineLength.html).

## Examples

[Set and Get Maximum Extension Line Length (VBA)](Set_and_Get_Maximum_Extension_Line_Length_Example_VB.htm)

## Remarks

After using this property, use [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html) to redraw the graphics window to see your changes.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::SmartWitness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SmartWitness.html)
[IDisplayDimension::WitnessVisibility Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~WitnessVisibility.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
