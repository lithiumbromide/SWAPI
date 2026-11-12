---
title: "DimensionLineDirection Property (IDimension)"
project: "SOLIDWORKS API Help"
interface: "IDimension"
member: "DimensionLineDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~DimensionLineDirection.html"
---

# DimensionLineDirection Property (IDimension)

Gets or sets the direction of this dimension line.

## Syntax

### Visual Basic (Declaration)

```vb
Property DimensionLineDirection As MathVector
```

### Visual Basic (Usage)

```vb
Dim instance As IDimension
Dim value As MathVector

instance.DimensionLineDirection = value

value = instance.DimensionLineDirection
```

### C#

```csharp
MathVector DimensionLineDirection {get; set;}
```

### C++/CLI

```cpp
property MathVector^ DimensionLineDirection {
   MathVector^ get();
   void set (    MathVector^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pointer to the [IMathVector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) object

## VBA Syntax

See [Dimension::DimensionLineDirection](ms-its:sldworksapivb6.chm::/sldworks~Dimension~DimensionLineDirection.html).

## Remarks

This method only supports feature dimensions.

## See Also

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html)
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html)
[IDimension::ExtensionLineDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ExtensionLineDirection.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
