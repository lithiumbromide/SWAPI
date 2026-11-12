---
title: "GetFractionBase Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "GetFractionBase"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetFractionBase.html"
---

# GetFractionBase Method (IDisplayDimension)

Gets whether this display dimension is displayed as a decimal value or a fraction.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFractionBase() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Integer

value = instance.GetFractionBase()
```

### C#

```csharp
System.int GetFractionBase()
```

### C++/CLI

```cpp
System.int GetFractionBase();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Value indicating decimal or fractional display as defined in [swFractionDisplay_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFractionDisplay_e.html)

## VBA Syntax

See [DisplayDimension::GetFractionBase](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~GetFractionBase.html).

## Remarks

The unit display settings of a display dimension are controlled by a value that SOLIDWORKS stores in one of two places: on the owning document or on the individual display dimension. Use [IDisplayDimension::GetUseDocUnits](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~GetUseDocUnits.html) to determine whether this IDisplayDimension uses the document default or a specific value set for this IDisplayDimension.

If this display dimension is using the unit information stored locally on the DisplayDimension, this method returns a value defined in [swFractionDisplay_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFractionDisplay_e.html). If this display dimension uses settings from the document, then this method returns -1.

Use [IDisplayDimension::SetUnits](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~SetUnits.html) to set the units settings of a display dimension.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::GetFractionValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetFractionValue.html)
[IDisplayDimension::GetRoundToFraction Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetRoundToFraction.html)
[IDisplayDimension::GetUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUnits.html)
[IDisplayDimension::SetUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetUnits.html)
[IDisplayDimension::GetUseDocUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocUnits.html)

## Availability

SOLIDWORKS 99, datecode 1999207
