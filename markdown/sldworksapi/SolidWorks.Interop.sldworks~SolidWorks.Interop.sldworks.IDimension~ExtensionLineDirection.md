---
title: "ExtensionLineDirection Property (IDimension)"
project: "SOLIDWORKS API Help"
interface: "IDimension"
member: "ExtensionLineDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ExtensionLineDirection.html"
---

# ExtensionLineDirection Property (IDimension)

Gets or sets the direction of the extension line.

## Syntax

### Visual Basic (Declaration)

```vb
Property ExtensionLineDirection As MathVector
```

### Visual Basic (Usage)

```vb
Dim instance As IDimension
Dim value As MathVector

instance.ExtensionLineDirection = value

value = instance.ExtensionLineDirection
```

### C#

```csharp
MathVector ExtensionLineDirection {get; set;}
```

### C++/CLI

```cpp
property MathVector^ ExtensionLineDirection {
   MathVector^ get();
   void set (    MathVector^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pointer to the [IMathVector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) object

## VBA Syntax

See [Dimension::ExtensionLineDirection](ms-its:sldworksapivb6.chm::/sldworks~Dimension~ExtensionLineDirection.html).

## Examples

[Get Extension Line Direction (VBA)](Get_Extension_Line_Direction_Example_VB.htm)

## Remarks

This method only supports feature dimensions. Additionally, it returns non-0 vector for feature dimensions ([IDimension::GetFeatureOwner](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension~GetFeatureOwner.html)) and 0 vector for radial and chamfer dimensions.

## See Also

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html)
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html)
[IDimension::DimensionLineDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~DimensionLineDirection.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
