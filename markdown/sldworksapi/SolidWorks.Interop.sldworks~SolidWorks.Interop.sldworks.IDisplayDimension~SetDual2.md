---
title: "SetDual2 Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "SetDual2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetDual2.html"
---

# SetDual2 Method (IDisplayDimension)

Controls the display of dual dimensions of this display dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetDual2( _
   ByVal UseDoc As System.Boolean, _
   ByVal InwardRounding As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim UseDoc As System.Boolean
Dim InwardRounding As System.Boolean

instance.SetDual2(UseDoc, InwardRounding)
```

### C#

```csharp
void SetDual2(
   System.bool UseDoc,
   System.bool InwardRounding
)
```

### C++/CLI

```cpp
void SetDual2(
   System.bool UseDoc,
   System.bool InwardRounding
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseDoc`: True uses the document setting, false uses the opposite of the document setting (see **Remarks**)
- `InwardRounding`: True for inward rounding of secondary unit tolerances, false for current document rounding (see **Remarks**)

## VBA Syntax

See [DisplayDimension::SetDual2](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~SetDual2.html).

## Examples

[Set Rounding of Decimal Units in Display Dimensions (VBA)](Set_Rounding_of_Decimal_Units_in_Display_Dimensions_Example_VB.htm)
[Set Rounding of Decimal Units in Display Dimensions (VB.NET)](Set_Rounding_of_Decimal_Units_in_Display_Dimensions_Example_VBNET.htm)
[Set Rounding of Decimal Units in Display Dimensions (C#)](Set_Rounding_of_Decimal_Units_in_Display_Dimensions_Example_CSharp.htm)

## Remarks

Dual dimensions can use either the same top, bottom, right, or left setting as the document or an opposite top, bottom, right, or left setting. This method allows you to set a dual dimension to use the current document setting or the opposite setting.

| If InwardRounding is false and an override unit is... | Then... |
| --- | --- |
| Not specified | Current document rounding prevails |
| Specified | Rounding setting under Override Units in the Dimensions PropertyManager page prevails |

Use [IDisplayDimension::GetUseDocDual](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~GetUseDocDual.html) to get the current value of this setting.

After using this method, use [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html) to redraw the graphics window to see your changes.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::Split Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Split.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
