---
title: "Add Method (IEquationMgr)"
project: "SOLIDWORKS API Help"
interface: "IEquationMgr"
member: "Add"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Add.html"
---

# Add Method (IEquationMgr)

Obsolete. Superseded by [IEquationMgr::Add2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEquationMgr~Add2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function Add( _
   ByVal Index As System.Integer, _
   ByVal Equation As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEquationMgr
Dim Index As System.Integer
Dim Equation As System.String
Dim value As System.Integer

value = instance.Add(Index, Equation)
```

### C#

```csharp
System.int Add(
   System.int Index,
   System.string Equation
)
```

### C++/CLI

```cpp
System.int Add(
   System.int Index,
   System.String^ Equation
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the new equation (-1 places it at the end of the list)
- `Equation`: String containing the equation

### Return Value

Index of the equation; -1 if there was an error

## VBA Syntax

See [EquationMgr::Add](ms-its:sldworksapivb6.chm::/sldworks~EquationMgr~Add.html).

## Remarks

The string specified for the equation argument must be formatted as if entered in the SOLIDWORKS Design user interface (that is, you must embed the names of the dimensions in double quotes). For example:

"N_SPOKES@CirPattern1" = "BARLENGTH@Sketch2" /10

You can also use the Visual Basic IIf function when specifying a model dimension in the equation argument. For example:

"D1@Extrude2" = (IIf("D1@Extrude3">20, 15, 6))+5

## See Also

[IEquationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.html)
[IEquationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr_members.html)
[IEquationMgr::Delete Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Delete.html)
[IEquationMgr::GetCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GetCount.html)
[IEquationMgr::Equation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Equation.html)
[IEquationMgr::Status Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Status.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
