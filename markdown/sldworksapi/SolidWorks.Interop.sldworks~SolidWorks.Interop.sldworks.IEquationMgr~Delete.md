---
title: "Delete Method (IEquationMgr)"
project: "SOLIDWORKS API Help"
interface: "IEquationMgr"
member: "Delete"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Delete.html"
---

# Delete Method (IEquationMgr)

Deletes the equation at the specified index.

## Syntax

### Visual Basic (Declaration)

```vb
Function Delete( _
   ByVal Index As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEquationMgr
Dim Index As System.Integer
Dim value As System.Integer

value = instance.Delete(Index)
```

### C#

```csharp
System.int Delete(
   System.int Index
)
```

### C++/CLI

```cpp
System.int Delete(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 0-based index of the equation to delete

### Return Value

0 if the equation is deleted; -1 if there was an error

## VBA Syntax

See [EquationMgr::Delete](ms-its:sldworksapivb6.chm::/sldworks~EquationMgr~Delete.html).

## Examples

[Add Equation and Evalute All (C#)](Add_Equation_And_Evaluate_All_Example_CSharp.htm)
[Add Equation and Evalute All (VB.NET)](Add_Equation_And_Evaluate_All_Example_VBNET.htm)
[Add Equation and Evalute All (VBA)](Add_Equation_And_Evaluate_All_Example_VB.htm)

## Remarks

When you delete an equation, you are removing it from the list of relations. Thus, do not delete an equation while traversing the equations in a model, because SOLIDWORKS could crash.

## See Also

[IEquationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.html)
[IEquationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr_members.html)
[IEquationMgr::Add2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Add2.html)
[IEquationMgr::Add3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Add3.html)
[IEquationMgr::GetCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GetCount.html)
[IEquationMgr::Equation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Equation.html)
[IEquationMgr::Disabled Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Disabled.html)
[IEquationMgr::GetDisabledEquationCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GetDisabledEquationCount.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
