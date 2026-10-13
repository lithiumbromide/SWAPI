---
title: "SupplementaryAngle Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "SupplementaryAngle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SupplementaryAngle.html"
---

# SupplementaryAngle Method (IDisplayDimension)

Changes the angle in the selected angular dimension to its supplementary angle.

## Syntax

### Visual Basic (Declaration)

```vb
Function SupplementaryAngle() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Boolean

value = instance.SupplementaryAngle()
```

### C#

```csharp
System.bool SupplementaryAngle()
```

### C++/CLI

```cpp
System.bool SupplementaryAngle();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the angle in the selected angular dimension changes to its supplementary angle, false if not

## VBA Syntax

See [DisplayDimension::SupplementaryAngle](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~SupplementaryAngle.html).

## Examples

[Change Angle to Supplementary Angle (C#)](Change_Angle_to_Supplementary_Angle_Example_CSharp.htm)
[Change Angle to Supplementary Angle (VB.NET)](Change_Angle_to_Supplementary_Angle_Example_VBNET.htm)
[Change Angle to Supplementary Angle (VBA)](Change_Angle_to_Supplementary_Angle_Example_VB.htm)

## Remarks

| If the angle in the selected angular dimension is... | Then the supplementary angle is its... |
| --- | --- |
| >180 degrees (i.e., exterior) | Interior angle |
| <180 degrees (i.e., interior) | Exterior angle |

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IModelDocExtension::AddDimension Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddDimension.html)
[IModelDoc2::AddDimension2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddDimension2.html)

## Availability

SOLIDWORKS 2016 SP3, Revision Number 24.3
