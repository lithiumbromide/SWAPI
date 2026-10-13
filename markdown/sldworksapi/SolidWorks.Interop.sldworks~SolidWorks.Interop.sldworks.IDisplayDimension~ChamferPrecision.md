---
title: "ChamferPrecision Property (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "ChamferPrecision"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ChamferPrecision.html"
---

# ChamferPrecision Property (IDisplayDimension)

Gets or sets the precision of the length and angle values in a chamfer display dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Property ChamferPrecision( _
   ByVal Index As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim Index As System.Integer
Dim value As System.Integer

instance.ChamferPrecision(Index) = value

value = instance.ChamferPrecision(Index)
```

### C#

```csharp
System.int ChamferPrecision(
   System.int Index
) {get; set;}
```

### C++/CLI

```cpp
property System.int ChamferPrecision {
   System.int get(System.int Index);
   void set (System.int Index, System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 0 for length, 1 for angle

### Property Value

Number of decimal places to display for the value at the specified index

## VBA Syntax

See [DisplayDimension::ChamferPrecision](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~ChamferPrecision.html).

## Examples

[Get Chamfer Display Dimension (C#)](Get_Chamfer_Display_Dimension_Example_CSharp.htm)
[Get Chamfer Display Dimension (VB.NET)](Get_Chamfer_Display_Dimension_Example_VBNET.htm)
[Get Chamfer Display Dimension (VBA)](Get_Chamfer_Display_Dimension_Example_VB.htm)

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::GetChamferUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetChamferUnits.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
