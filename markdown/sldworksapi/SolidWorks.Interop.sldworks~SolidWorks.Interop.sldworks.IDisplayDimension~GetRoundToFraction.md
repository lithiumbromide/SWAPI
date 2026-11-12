---
title: "GetRoundToFraction Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "GetRoundToFraction"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetRoundToFraction.html"
---

# GetRoundToFraction Method (IDisplayDimension)

Gets whether the displayed dimension value is rounded off so that SOLIDWORKS can display it as a fraction.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRoundToFraction() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Boolean

value = instance.GetRoundToFraction()
```

### C#

```csharp
System.bool GetRoundToFraction()
```

### C++/CLI

```cpp
System.bool GetRoundToFraction();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True rounds off the displayed dimension value to a fraction, false does not (see **Remarks**)

## VBA Syntax

See [DisplayDimension::GetRoundToFraction](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~GetRoundToFraction.html).

## Remarks

The unit display settings of a display dimension are controlled by a value that SOLIDWORKS stores in one of two places: on the owning document or on the individual display dimension. Use [IDisplayDimension::GetUseDocUnits](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~GetUseDocUnits.html) to determine whether this IDisplayDimension uses the document default or a specific value set for this IDisplayDimension.

If this display dimension uses local unit information, then the return value indicates whether the displayed value of this dimension is rounded off to a value that SOLIDWORKS can represent as a fraction.

Fraction display is valid only for unit types swINCHES or swFEETINCHES. In all other cases, this method returns -1. Use [IDisplayDimension::SetUnits](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~SetUnits.html) to set the units settings of a display dimension.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[GetFractionBase Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetFractionBase.html)
[GetFractionValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetFractionValue.html)
[IDisplayDimension::GetUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUnits.html)
[IDisplayDimension::GetUseDocUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocUnits.html)
[IDisplayDimension::SetUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetUnits.html)

## Availability

SOLIDWORKS 99, datecode 1999207
