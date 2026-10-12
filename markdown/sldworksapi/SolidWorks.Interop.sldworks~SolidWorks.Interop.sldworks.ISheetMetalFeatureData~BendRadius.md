---
title: "BendRadius Property (ISheetMetalFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISheetMetalFeatureData"
member: "BendRadius"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~BendRadius.html"
---

# BendRadius Property (ISheetMetalFeatureData)

Gets or sets the sheet metal bend radius.

## Syntax

### Visual Basic (Declaration)

```vb
Property BendRadius As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISheetMetalFeatureData
Dim value As System.Double

instance.BendRadius = value

value = instance.BendRadius
```

### C#

```csharp
System.double BendRadius {get; set;}
```

### C++/CLI

```cpp
property System.double BendRadius {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Value for the bend radius

## VBA Syntax

See [SheetMetalFeatureData::BendRadius](ms-its:sldworksapivb6.chm::/sldworks~SheetMetalFeatureData~BendRadius.html).

## Examples

See [ISheetMetalFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheetMetalFeatureData.html) examples.

## Examples

[Change Bend Radius of Sheet Metal Part (VBA)](Change_Bend_Radius_of_Sheet_Metal_Part_Example_VB.htm)

## See Also

[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.html)
[ISheetMetalFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData_members.html)

## Availability

SOLIDWORKS 2001 SP1, Revision Number 9.1
