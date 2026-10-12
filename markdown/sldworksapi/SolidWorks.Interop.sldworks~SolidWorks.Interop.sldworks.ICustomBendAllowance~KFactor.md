---
title: "KFactor Property (ICustomBendAllowance)"
project: "SOLIDWORKS API Help"
interface: "ICustomBendAllowance"
member: "KFactor"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance~KFactor.html"
---

# KFactor Property (ICustomBendAllowance)

Gets or sets the K-factor.

## Syntax

### Visual Basic (Declaration)

```vb
Property KFactor As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICustomBendAllowance
Dim value As System.Double

instance.KFactor = value

value = instance.KFactor
```

### C#

```csharp
System.double KFactor {get; set;}
```

### C++/CLI

```cpp
property System.double KFactor {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

K-factor value

## VBA Syntax

See [CustomBendAllowance::KFactor](ms-its:sldworksapivb6.chm::/sldworks~CustomBendAllowance~KFactor.html).

## Examples

See [ICustomBendAllowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomBendAllowance.html) examples.

## Examples

[Change Bend Radius of Sketch Bend (VBA)](Change_Bend_Radius_of_Sketched_Bend_Example_VB.htm)

## Remarks

When using this property to set a value for K-factor, then the [type of custom bend allowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomBendAllowance~Type.html) is set to this type. However, the last ICustomBendAllowance property called to set a value also re-sets the type of custom bend allowance to its type.

See the ICustomBendAllowance Remarks.

## See Also

[ICustomBendAllowance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance.html)
[ICustomBendAllowance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
