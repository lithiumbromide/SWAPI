---
title: "Selectable Property (IManipulator)"
project: "SOLIDWORKS API Help"
interface: "IManipulator"
member: "Selectable"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator~Selectable.html"
---

# Selectable Property (IManipulator)

Gets or sets whether the manipulator can be selected in a PropertyManager page's selection box.

## Syntax

### Visual Basic (Declaration)

```vb
Property Selectable As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IManipulator
Dim value As System.Boolean

instance.Selectable = value

value = instance.Selectable
```

### C#

```csharp
System.bool Selectable {get; set;}
```

### C++/CLI

```cpp
property System.bool Selectable {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the manipulator can be selected, false if not

## VBA Syntax

See [Manipulator::Selectable](ms-its:sldworksapivb6.chm::/sldworks~Manipulator~Selectable.html).

## Examples

[Create PropertyManager Page and Selectable Triad Manipulator (VBA)](Create_PropertyManager_Page_and_Selectable_Triad_Manipulator_Example_VB.htm)

## See Also

[IManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator.html)
[IManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
