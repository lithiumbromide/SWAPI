---
title: "Value Property (IEquationMgr)"
project: "SOLIDWORKS API Help"
interface: "IEquationMgr"
member: "Value"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Value.html"
---

# Value Property (IEquationMgr)

Gets the value of the equation at the specified index.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Value( _
   ByVal Index As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IEquationMgr
Dim Index As System.Integer
Dim value As System.Double

value = instance.Value(Index)
```

### C#

```csharp
System.double Value(
   System.int Index
) {get;}
```

### C++/CLI

```cpp
property System.double Value {
   System.double get(System.int Index);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 0-based index of the equation

### Property Value

Value or -1 if Index is out of range

## VBA Syntax

See [EquationMgr::Value](ms-its:sldworksapivb6.chm::/sldworks~EquationMgr~Value.html).

## Examples

[Use IIf Function When Adding an Equation (VBA)](Use_IIf_Function_When_Adding_an_Equation_Example_VB.htm)
[Get Equation Values (C#)](Get_Equation_Values_Example_CSharp.htm)
[Get Equation Values (VB.NET)](Get_Equation_Values_Example_VBNET.htm)
[Get Equation Values (VBA)](Get_Equation_Values_Example_VB.htm)

## Remarks

## See Also

[IEquationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.html)
[IEquationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr_members.html)
[IEquationMgr::Status Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Status.html)
[IEquationMgr::GetCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GetCount.html)
[IEquationMgr::Equation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Equation.html)
[IEquationMgr::GlobalVariable Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GlobalVariable.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
