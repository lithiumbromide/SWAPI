---
title: "Visible Property (IManipulator)"
project: "SOLIDWORKS API Help"
interface: "IManipulator"
member: "Visible"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator~Visible.html"
---

# Visible Property (IManipulator)

Gets or sets whether the manipulator is visible in this SOLIDWORKS part or assembly document.

## Syntax

### Visual Basic (Declaration)

```vb
Property Visible As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IManipulator
Dim value As System.Boolean

instance.Visible = value

value = instance.Visible
```

### C#

```csharp
System.bool Visible {get; set;}
```

### C++/CLI

```cpp
property System.bool Visible {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the manipulator is visible, false if not

## VBA Syntax

See [Manipulator::Visible](ms-its:sldworksapivb6.chm::/sldworks~Manipulator~Visible.html).

## See Also

[IManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator.html)
[IManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
