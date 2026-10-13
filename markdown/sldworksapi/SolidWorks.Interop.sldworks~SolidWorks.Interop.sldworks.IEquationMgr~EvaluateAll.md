---
title: "EvaluateAll Method (IEquationMgr)"
project: "SOLIDWORKS API Help"
interface: "IEquationMgr"
member: "EvaluateAll"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~EvaluateAll.html"
---

# EvaluateAll Method (IEquationMgr)

Evaluates all equations.

## Syntax

### Visual Basic (Declaration)

```vb
Function EvaluateAll() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEquationMgr
Dim value As System.Integer

value = instance.EvaluateAll()
```

### C#

```csharp
System.int EvaluateAll()
```

### C++/CLI

```cpp
System.int EvaluateAll();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

-1 for both success and failure

## VBA Syntax

See [EquationMgr::EvaluateAll](ms-its:sldworksapivb6.chm::/sldworks~EquationMgr~EvaluateAll.html).

## Examples

[Use IIf Function When Adding an Equation (VBA)](Use_IIf_Function_When_Adding_an_Equation_Example_VB.htm)
[Add Equation and Evaluate All (VBA)](Add_Equation_And_Evaluate_All_Example_VB.htm)
[Add Equation and Evaluate All (VB.NET)](Add_Equation_And_Evaluate_All_Example_VBNET.htm)
[Add Equation and Evaluate All (C#)](Add_Equation_And_Evaluate_All_Example_CSharp.htm)

## Remarks

Use this method to solve all equations that were added by [IEquationMgr::Add2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEquationMgr~Add2.html) or [IEquationMgr::Add3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEquationMgr~Add3.html) where Solve is set to false.

## See Also

[IEquationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.html)
[IEquationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr_members.html)
[IEquationMgr::GetCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GetCount.html)
[IEquationMgr::Equation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Equation.html)
[IEquationMgr::Status Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Status.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
