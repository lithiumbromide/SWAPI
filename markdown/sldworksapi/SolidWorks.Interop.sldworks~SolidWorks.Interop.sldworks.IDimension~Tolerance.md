---
title: "Tolerance Property (IDimension)"
project: "SOLIDWORKS API Help"
interface: "IDimension"
member: "Tolerance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~Tolerance.html"
---

# Tolerance Property (IDimension)

Gets the [IDimensionTolerance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance.html) object.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Tolerance As DimensionTolerance
```

### Visual Basic (Usage)

```vb
Dim instance As IDimension
Dim value As DimensionTolerance

value = instance.Tolerance
```

### C#

```csharp
DimensionTolerance Tolerance {get;}
```

### C++/CLI

```cpp
property DimensionTolerance^ Tolerance {
   DimensionTolerance^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pointer to the [IDimensionTolerance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance.html) object

## VBA Syntax

See [Dimension::Tolerance](ms-its:sldworksapivb6.chm::/sldworks~Dimension~Tolerance.html).

## Examples

[Get Dimension Tolerance (VBA)](Get_Dimension_Tolerance_Example_VB.htm)
[Get Dimension Tolerance (VB.NET)](Get_Dimension_Tolerance_Example_VBNET.htm)
[Get Dimension Tolerance (C#)](Get_Dimension_Tolerance_Example_CSharp.htm)

## See Also

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html)
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
