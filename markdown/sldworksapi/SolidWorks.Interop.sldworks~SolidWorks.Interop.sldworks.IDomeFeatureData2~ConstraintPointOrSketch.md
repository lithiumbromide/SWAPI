---
title: "ConstraintPointOrSketch Property (IDomeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IDomeFeatureData2"
member: "ConstraintPointOrSketch"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2~ConstraintPointOrSketch.html"
---

# ConstraintPointOrSketch Property (IDomeFeatureData2)

Gets or sets the constraining point or sketch for a dome feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ConstraintPointOrSketch As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDomeFeatureData2
Dim value As System.Object

instance.ConstraintPointOrSketch = value

value = instance.ConstraintPointOrSketch
```

### C#

```csharp
System.object ConstraintPointOrSketch {get; set;}
```

### C++/CLI

```cpp
property System.Object^ ConstraintPointOrSketch {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Point or sketch for the dome feature

## VBA Syntax

See [DomeFeatureData2::ConstraintPointOrSketch](ms-its:sldworksapivb6.chm::/sldworks~DomeFeatureData2~ConstraintPointOrSketch.html).

## Examples

[Get and Set Constraint for Dome Feature (VBA)](Get_and_Set_Constraint_for_Dome_Feature_Example_VB.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IDomeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2.html)
[IDomeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
