---
title: "GetType Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "GetType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetType.html"
---

# GetType Method (IDisplayDimension)

Obsolete. Superseded by [IDisplayDimension::Type2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~Type2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Integer

value = instance.GetType()
```

### C#

```csharp
System.int GetType()
```

### C++/CLI

```cpp
System.int GetType();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Dimension type as defined in [swDimensionType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDimensionType_e.html)

## VBA Syntax

See [DisplayDimension::GetType](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~GetType.html).

## Remarks

Radial and diametric dimensions both return swRadialDimension. To determine how this radial dimension is currently displayed, use [IDisplayDimension::Diametric](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~Diametric.html) and [IDisplayDimension::DisplayAsLinear](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~DisplayAsLinear.html).

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::Type2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Type2.html)
[IDisplayDimension::Diametric Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Diametric.html)

## Availability

SOLIDWORKS 99 SP06, datecode 1999355
