---
title: "GetUnits Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "GetUnits"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUnits.html"
---

# GetUnits Method (IDisplayDimension)

Gets the units used by this display dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUnits() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Integer

value = instance.GetUnits()
```

### C#

```csharp
System.int GetUnits()
```

### C++/CLI

```cpp
System.int GetUnits();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Units for this display dimension as defined in [swLengthUnit_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLengthUnit_e.html) or [swAngleUnit_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAngleUnit_e.html) (see **Remarks**)

## VBA Syntax

See [DisplayDimension::GetUnits](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~GetUnits.html).

## Remarks

A display dimension's units are controlled by a value stored in one of two places:

- document setting.
  - or -
- local display dimension setting.

Use [IDisplayDimension::GetUseDocUnits](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~GetUseDocUnits.html) to determine whether the display dimension's settings are from the document setting or local display dimension setting.

| If the display dimension uses... | Then IDisplayDimension::GetUnits returns... |
| --- | --- |
| Document setting | -1 |
| Local display dimension setting | swLengthUnit_e or swAngleUnit_e value |

Use [IDisplayDimension::SetUnits](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~SetUnits.html) to set the display dimension's unit setting.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::GetChamferUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetChamferUnits.html)

## Availability

SOLIDWORKS 99, datecode 1999207
