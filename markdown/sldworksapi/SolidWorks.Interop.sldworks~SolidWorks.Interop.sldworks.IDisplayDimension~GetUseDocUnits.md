---
title: "GetUseDocUnits Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "GetUseDocUnits"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocUnits.html"
---

# GetUseDocUnits Method (IDisplayDimension)

Gets whether this display dimension uses the document default setting for units.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUseDocUnits() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Boolean

value = instance.GetUseDocUnits()
```

### C#

```csharp
System.bool GetUseDocUnits()
```

### C++/CLI

```cpp
System.bool GetUseDocUnits();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if this display dimension uses the document setting, false if it uses the local display dimension setting

## VBA Syntax

See [DisplayDimension::GetUseDocUnits](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~GetUseDocUnits.html).

## Examples

[Get Chamfer Display Dimension (C#)](Get_Chamfer_Display_Dimension_Example_CSharp.htm)
[Get Chamfer Display Dimension (VB.NET)](Get_Chamfer_Display_Dimension_Example_VBNET.htm)
[Get Chamfer Display Dimension (VBA)](Get_Chamfer_Display_Dimension_Example_VB.htm)

## Remarks

The unit display settings of a display dimension are controlled by a value stored in one of two places: on the owning document or on the individual display dimension. This method determines whether this display dimension uses the default document setting for units.

Use [IDisplayDimension::SetUnits](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~SetUnits.html) to set this value.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::GetUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUnits.html)

## Availability

SOLIDWORKS 99, datecode 1999207
