---
title: "DisplayedUnit Property (IPropertyManagerPageNumberbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageNumberbox"
member: "DisplayedUnit"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox~DisplayedUnit.html"
---

# DisplayedUnit Property (IPropertyManagerPageNumberbox)

Gets or sets the unit type to display in this PropertyManager page number box.

## Syntax

### Visual Basic (Declaration)

```vb
Property DisplayedUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageNumberbox
Dim value As System.Integer

instance.DisplayedUnit = value

value = instance.DisplayedUnit
```

### C#

```csharp
System.int DisplayedUnit {get; set;}
```

### C++/CLI

```cpp
property System.int DisplayedUnit {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Unit type to display in this PropertyManager page number box (see **Remarks**)

## VBA Syntax

See [PropertyManagerPageNumberbox::DisplayedUnit](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageNumberbox~DisplayedUnit.html).

## Remarks

This property depends on the unit type specified for the [IPropertyManagerPageNumberbox::SetRange2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageNumberbox~SetRange2.html)'s Units parameter, which is a value from [swNumberboxUnitType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swNumberboxUnitType_e.html).

| If IPropertyManagerPageNumberbox::SetRange2's Units parameter is... | Then specifiy an enumerator from this enumeration for IPropertyManagerPageNumber::DisplayedUnit... |
| --- | --- |
| swNumberBox_Length | swLengthUnit_e |
| swNumberBox_Angle | swAngleUnit_e |
| swNumberBox_Force | swUnitsForce_e |
| swNumberBox_Time | swUnitsTimeUnit_e |

For example, IPropertyManagerPageNumberbox::DisplayedUnit allows an add-in to have a number box that shows length values in inches, even though the system default units are meters. Remember that the values specified for both [IPropertyManagerPageNumberbox::Value](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageNumberbox~Value.html) and IPropertyManagerPageNumberbox::SetRange2 are in system units; IPropertyManagerPageNumberbox::DisplayedUnits simply controls how that value is displayed in the PropertyManager page number box.

You can call IPropertyManagerPageNumberbox::DisplayedUnit and change the units displayed in a number box while a Propertymanager page is displayed.

## See Also

[IPropertyManagerPageNumberbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox.html)
[IPropertyManagerPageNumberbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox_members.html)
