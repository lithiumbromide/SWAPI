---
title: "AngularEquationUnits Property (IEquationMgr)"
project: "SOLIDWORKS API Help"
interface: "IEquationMgr"
member: "AngularEquationUnits"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~AngularEquationUnits.html"
---

# AngularEquationUnits Property (IEquationMgr)

Gets or sets the angular units used in equations.

## Syntax

### Visual Basic (Declaration)

```vb
Property AngularEquationUnits As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEquationMgr
Dim value As System.Integer

instance.AngularEquationUnits = value

value = instance.AngularEquationUnits
```

### C#

```csharp
System.int AngularEquationUnits {get; set;}
```

### C++/CLI

```cpp
property System.int AngularEquationUnits {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Angular units used in equations as defined in [swAngularEquationUnits_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAngularEquationUnits_e.html)

## VBA Syntax

See [EquationMgr::AngularEquationUnits](ms-its:sldworksapivb6.chm::/sldworks~EquationMgr~AngularEquationUnits.html).

## See Also

[IEquationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.html)
[IEquationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr_members.html)
[IEquationMgr::Equation Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Equation.html)

## Availability

SOLIDWORKS 2006 SP5, Revision Number 14.5
