---
title: "GetDimension2 Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "GetDimension2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetDimension2.html"
---

# GetDimension2 Method (IDisplayDimension)

Gets the model dimension used to create this display dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDimension2( _
   ByVal Index As System.Integer _
) As Dimension
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim Index As System.Integer
Dim value As Dimension

value = instance.GetDimension2(Index)
```

### C#

```csharp
Dimension GetDimension2(
   System.int Index
)
```

### C++/CLI

```cpp
Dimension^ GetDimension2(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: - 0 to get the first chamfer display dimension
  - 1 to get the second chamfer display dimension

### Return Value

[Dimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension.html)

## VBA Syntax

See [DisplayDimension::GetDimension2](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~GetDimension2.html).

## Examples

[Get and Set Sensor (C#)](Get_and_Set_Sensor_Example_CSharp.htm)
[Get and Set Sensor (VB.NET)](Get_and_Set_Sensor_Example_VBNET.htm)
[Get and Set Sensor (VBA)](Get_and_Set_Sensor_Example_VB.htm)

## Remarks

The Index argument is valid for chamfer display dimensions only. If the display dimension is not a chamfer display dimension, then Index is ignored. To get both chamfer display dimensions, you must call this property twice; specify 0 for Index in the first call and 1 for Index in the second call.

SOLIDWORKS can display a dimension more than once. For example, a base-extrude dimension can be brought into three different views on a drawing. These three dimensions are referred to as display dimensions and are represented by the DisplayDimension object in the SOLIDWORKS API. The original base-extrude dimension is represented by the Dimension object in the SOLIDWORKS API.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
