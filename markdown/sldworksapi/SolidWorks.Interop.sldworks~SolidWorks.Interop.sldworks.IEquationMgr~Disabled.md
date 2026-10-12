---
title: "Disabled Property (IEquationMgr)"
project: "SOLIDWORKS API Help"
interface: "IEquationMgr"
member: "Disabled"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Disabled.html"
---

# Disabled Property (IEquationMgr)

Gets or sets whether to disable the specified equation in the model.

## Syntax

### Visual Basic (Declaration)

```vb
Property Disabled( _
   ByVal Index As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEquationMgr
Dim Index As System.Integer
Dim value As System.Boolean

instance.Disabled(Index) = value

value = instance.Disabled(Index)
```

### C#

```csharp
System.bool Disabled(
   System.int Index
) {get; set;}
```

### C++/CLI

```cpp
property System.bool Disabled {
   System.bool get(System.int Index);
   void set (System.int Index, System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 0-based index of the equation

### Property Value

True to disable the specified equation, false to not

## VBA Syntax

See [EquationMgr::Disabled](ms-its:sldworksapivb6.chm::/sldworks~EquationMgr~Disabled.html).

## Examples

[Disable Equation (C#)](Disable_Equation_Example_CSharp.htm)
[Disable Equation (VB.NET)](Disable_Equation_Example_VBNET.htm)
[Disable Equation (VBA)](Disable_Equation_Example_VB.htm)

## Remarks

When you disable an equation, you are removing it from the list of relations. Thus, do not disable an equation while traversing the equations in a model, because SOLIDWORKS could crash.

## See Also

[IEquationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.html)
[IEquationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr_members.html)
[IEquationMgr::Add2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Add2.html)
[IEquationMgr::Add3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Add3.html)
[IEquationMgr::Delete Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Delete.html)
[IEquationMgr::GetCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GetCount.html)
[IEquationMgr::GetDisabledEquationCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GetDisabledEquationCount.html)
[IEquationMgr::Equation Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Equation.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
