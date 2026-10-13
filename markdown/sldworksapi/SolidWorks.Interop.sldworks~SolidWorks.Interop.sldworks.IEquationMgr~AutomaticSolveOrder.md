---
title: "AutomaticSolveOrder Property (IEquationMgr)"
project: "SOLIDWORKS API Help"
interface: "IEquationMgr"
member: "AutomaticSolveOrder"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~AutomaticSolveOrder.html"
---

# AutomaticSolveOrder Property (IEquationMgr)

Gets or sets whether to automatically sequence equations in an order determined by SOLIDWORKS to produce accurate results.

## Syntax

### Visual Basic (Declaration)

```vb
Property AutomaticSolveOrder As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEquationMgr
Dim value As System.Boolean

instance.AutomaticSolveOrder = value

value = instance.AutomaticSolveOrder
```

### C#

```csharp
System.bool AutomaticSolveOrder {get; set;}
```

### C++/CLI

```cpp
property System.bool AutomaticSolveOrder {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to automatically sequence equations in an order determined by SOLIDWORKS to produce accurate results and to prevent changing the order in which equations are solved, false to solve equations in the order in which they appear in the equation's Ordered View and to allow changing the order in which equations are solved

## VBA Syntax

See [EquationMgr::AutomaticSolveOrder](ms-its:sldworksapivb6.chm::/sldworks~EquationMgr~AutomaticSolveOrder.html).

## Examples

[Automatically Solve Equations in Sequence (C#)](Automatically_Solve_Equations_in_Sequence_Example_CSharp.htm)
[Automatically Solve Equations in Sequence (VB.NET)](Automatically_Solve_Equations_in_Sequence_Example_VBNET.htm)
[Automatically Solve Equations in Sequence (VBA)](Automatically_Solve_Equations_in_Sequence_Example_VB.htm)

## See Also

[IEquationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.html)
[IEquationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr_members.html)
[IEquationMgr::Equation Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Equation.html)

## Availability

SOLIDWORKS 2012 SP5, Revision 20.5
