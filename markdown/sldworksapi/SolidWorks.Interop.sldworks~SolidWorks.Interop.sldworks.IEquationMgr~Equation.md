---
title: "Equation Property (IEquationMgr)"
project: "SOLIDWORKS API Help"
interface: "IEquationMgr"
member: "Equation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Equation.html"
---

# Equation Property (IEquationMgr)

Gets or sets the equation at the specified index.

## Syntax

### Visual Basic (Declaration)

```vb
Property Equation( _
   ByVal Index As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IEquationMgr
Dim Index As System.Integer
Dim value As System.String

instance.Equation(Index) = value

value = instance.Equation(Index)
```

### C#

```csharp
System.string Equation(
   System.int Index
) {get; set;}
```

### C++/CLI

```cpp
property System.String^ Equation {
   System.String^ get(System.int Index);
   void set (System.int Index, System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 0-based index of the equation

### Property Value

String containing the equation

## VBA Syntax

See [EquationMgr::Equation](ms-its:sldworksapivb6.chm::/sldworks~EquationMgr~Equation.html).

## Examples

[Use IIf Function When Adding an Equation (VBA)](Use_IIf_Function_When_Adding_an_Equation_Example_VB.htm)
[Disable Equation (C#)](Disable_Equation_Example_CSharp.htm)
[Disable Equation (VB.NET)](Disable_Equation_Example_VBNET.htm)
[Disable Equation (VBA)](Disable_Equation_Example_VB.htm)
[Get Equation Values (C#)](Get_Equation_Values_Example_CSharp.htm)
[Get Equation Values (VB.NET)](Get_Equation_Values_Example_VBNET.htm)
[Get Equation Values (VBA)](Get_Equation_Values_Example_VB.htm)

## Remarks

The string set by this property must be formatted as if entered in the SOLIDWORKS Design user interface; that is, you must embed the names of the dimensions and global variables in double double quotes. To use the following examples to specify Equation, you must replace every double quote with double double quotes, and enclose the entire equation with double quotes.

Global variable assignment:

**"B" = 2**

Component equation:

"**N_SPOKES@CirPattern1" = "BARLENGTH@Sketch2" /10**

Dimension equation that uses the Visual Basic IIf function:

**"D1@Extrude2" = (("D1@Extrude3">20, 15, 6))+5**

Dimension equation that sets a dimension to the current value:

**"D1@Extrude2" =**

Dimension equation that modifies the right-hand side of an already existing dimension equation:

**"D1@Extrude2" = 0.05**

**NOTE:** To set an equation:

- directly to an assembly component's model, you must call [IAssemblyDoc::EditPart2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EditPart2.html) before calling this method.
- for specific configurations in a model with multiple configurations, use [IEquationMgr::SetEquationAndConfigurationOption](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~SetEquationAndConfigurationOption.html).

## See Also

[IEquationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.html)
[IEquationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr_members.html)
[IEquationMgr::Add2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Add2.html)
[IEquationMgr::Delete Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Delete.html)
[IEquationMgr::GetCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GetCount.html)
[IEquationMgr::EvaluateAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~EvaluateAll.html)
[IEquationMgr::Add3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Add3.html)
[IEquationMgr::Disabled Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Disabled.html)
[IEquationMgr::GetDisabledEquationCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GetDisabledEquationCount.html)
[IEquationMgr::GlobalVariable Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GlobalVariable.html)
[IEquationMgr::AutomaticSolveOrder Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~AutomaticSolveOrder.html)
[IEquationMgr::AutomaticRebuild Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~AutomaticRebuild.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
