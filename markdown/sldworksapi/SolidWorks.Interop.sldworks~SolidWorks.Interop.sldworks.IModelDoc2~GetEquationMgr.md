---
title: "GetEquationMgr Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetEquationMgr"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetEquationMgr.html"
---

# GetEquationMgr Method (IModelDoc2)

Gets the equation manager.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEquationMgr() As EquationMgr
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As EquationMgr

value = instance.GetEquationMgr()
```

### C#

```csharp
EquationMgr GetEquationMgr()
```

### C++/CLI

```cpp
EquationMgr^ GetEquationMgr();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Equation manager](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEquationMgr.html)

## VBA Syntax

See [ModelDoc2::GetEquationMgr](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetEquationMgr.html).

## Examples

[Use IIf Function When Adding an Equation (VBA)](Use_IIf_Function_When_Adding_an_Equation_Example_VB.htm)
[Automatically Solve Equations in Sequence (C#)](Automatically_Solve_Equations_in_Sequence_Example_CSharp.htm)
[Automatically Solve Equations in Sequence (VB.NET)](Automatically_Solve_Equations_in_Sequence_Example_VBNET.htm)
[Automatically Solve Equations in Sequence (VBA)](Automatically_Solve_Equations_in_Sequence_Example_VB.htm)
[Get Equation Values (C#)](Get_Equation_Values_Example_CSharp.htm)
[Get Equation Values (VB.NET)](Get_Equation_Values_Example_VBNET.htm)
[Get Equation Values (VBA)](Get_Equation_Values_Example_VB.htm)

## Remarks

Use the equation manager to work with the existing equations in a model and modify a specific equation.

The [IEquationMgr](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEquationMgr.html) object is associated with the configuration that was active at the time it was acquired. If you change the active configuration while holding an IEquationMgr object reference, release it and reacquire it if it is needed.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
