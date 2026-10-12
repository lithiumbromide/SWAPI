---
title: "BendCalculationTableFile Property (ICustomBendAllowance)"
project: "SOLIDWORKS API Help"
interface: "ICustomBendAllowance"
member: "BendCalculationTableFile"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance~BendCalculationTableFile.html"
---

# BendCalculationTableFile Property (ICustomBendAllowance)

Gets or sets the bend calculation table file path name.

## Syntax

### Visual Basic (Declaration)

```vb
Property BendCalculationTableFile As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICustomBendAllowance
Dim value As System.String

instance.BendCalculationTableFile = value

value = instance.BendCalculationTableFile
```

### C#

```csharp
System.string BendCalculationTableFile {get; set;}
```

### C++/CLI

```cpp
property System.String^ BendCalculationTableFile {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Bend calculation table file path name

## VBA Syntax

See [CustomBendAllowance::BendCalculationTableFile](ms-its:sldworksapivb6.chm::/sldworks~CustomBendAllowance~BendCalculationTableFile.html).

## Examples

See the [ICustomBendAllowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance.html) example.

## Remarks

If using this property to set a value for the bend deduction, then the [type of custom bend allowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomBendAllowance~Type.html) is set to this type. However, the last ICustomBendAllowance property called to set a value also re-sets the type of custom bend allowance to its type.

See the ICustomBendAllowance Remarks.

## See Also

[ICustomBendAllowance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance.html)
[ICustomBendAllowance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance_members.html)

## Availability

SOLIDWORKS 2025 SP03, Revision Number 33.3
