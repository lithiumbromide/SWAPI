---
title: "GlobalVariable Property (IEquationMgr)"
project: "SOLIDWORKS API Help"
interface: "IEquationMgr"
member: "GlobalVariable"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GlobalVariable.html"
---

# GlobalVariable Property (IEquationMgr)

Gets whether the equation at the specified index is a global variable.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property GlobalVariable( _
   ByVal Index As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEquationMgr
Dim Index As System.Integer
Dim value As System.Boolean

value = instance.GlobalVariable(Index)
```

### C#

```csharp
System.bool GlobalVariable(
   System.int Index
) {get;}
```

### C++/CLI

```cpp
property System.bool GlobalVariable {
   System.bool get(System.int Index);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 0-based index of the equation

### Property Value

True if the equation at the specified index is a global variable, false if not

## VBA Syntax

See [EquationMgr::GlobalVariable](ms-its:sldworksapivb6.chm::/sldworks~EquationMgr~GlobalVariable.html).

## Examples

[Get Equation Values (C#)](Get_Equation_Values_Example_CSharp.htm)
[Get Equation Values (VB.NET)](Get_Equation_Values_Example_VBNET.htm)
[Get Equation Values (VBA)](Get_Equation_Values_Example_VB.htm)

## See Also

[IEquationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.html)
[IEquationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr_members.html)
[IEquationMgr::GetCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GetCount.html)
[IEquationMgr::Equation Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Equation.html)
[IEquationMgr::Value Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Value.html)

## Availability

SOLIDWORKS 2016 SP4, Revision Number 24.4
