---
title: "BendTableFile Property (ICustomBendAllowance)"
project: "SOLIDWORKS API Help"
interface: "ICustomBendAllowance"
member: "BendTableFile"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance~BendTableFile.html"
---

# BendTableFile Property (ICustomBendAllowance)

Gets or sets the path and file name for the bend table.

## Syntax

### Visual Basic (Declaration)

```vb
Property BendTableFile As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICustomBendAllowance
Dim value As System.String

instance.BendTableFile = value

value = instance.BendTableFile
```

### C#

```csharp
System.string BendTableFile {get; set;}
```

### C++/CLI

```cpp
property System.String^ BendTableFile {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Path and file name for the bend table

## VBA Syntax

See [CustomBendAllowance::BendTableFile](ms-its:sldworksapivb6.chm::/sldworks~CustomBendAllowance~BendTableFile.html).

## Examples

See [ICustomBendAllowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomBendAllowance.html) examples.

## Examples

[Change Bend Radius of Sketch Bend (VBA)](Change_Bend_Radius_of_Sketched_Bend_Example_VB.htm)

## Remarks

When using this property to set the path and file name for a bend table, then the [type of custom bend allowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomBendAllowance~Type.html) is set to this type. However, the last ICustomBendAllowance property called to set a value also re-sets the type of custom bend allowance to its type.

See the ICustomBendAllowance Remarks.

## See Also

[ICustomBendAllowance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance.html)
[ICustomBendAllowance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
