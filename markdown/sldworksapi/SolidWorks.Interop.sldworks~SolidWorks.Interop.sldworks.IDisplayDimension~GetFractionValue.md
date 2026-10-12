---
title: "GetFractionValue Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "GetFractionValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetFractionValue.html"
---

# GetFractionValue Method (IDisplayDimension)

Gets the largest fraction denominator to be used when this display dimension is displayed in fraction format.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFractionValue() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Integer

value = instance.GetFractionValue()
```

### C#

```csharp
System.int GetFractionValue()
```

### C++/CLI

```cpp
System.int GetFractionValue();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Denominator for fraction display (see **Remarks**)

## VBA Syntax

See [DisplayDimension::GetFractionValue](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~GetFractionValue.html).

## Remarks

The unit display settings of a display dimension are controlled by a value that SOLIDWORKS stores in one of two places: on the owning document or on the individual display dimension. Use [IDisplayDimension::GetUseDocUnits](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~GetUseDocUnits.html) to determine whether this IDisplayDimension uses the document default or a specific value set for this IDisplayDimension.

If this display dimension uses the unit information stored locally, this method returns the largest fraction denominator to be used (for example, 4 for 1/4, or 32 for 1/32). This method returns -1 if this display dimension uses settings from the document.

Fraction display is valid only for unit types swINCHES or swFEETINCHES. In all other cases, this method returns -1. Use [IDisplayDimension::SetUnits](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~SetUnits.html) to set the units settings of a display dimension.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::GetFractionBase Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetFractionBase.html)
[IDisplayDimension::GetRoundToFraction Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetRoundToFraction.html)
[IDisplayDimension::SetUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetUnits.html)
[IDisplayDimension::GetUseDocUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocUnits.html)
[IDisplayDimension::GetUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUnits.html)

## Availability

SOLIDWORKS 99, datecode 1999207
