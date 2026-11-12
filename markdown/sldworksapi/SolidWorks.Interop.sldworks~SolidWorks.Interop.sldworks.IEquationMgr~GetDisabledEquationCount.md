---
title: "GetDisabledEquationCount Method (IEquationMgr)"
project: "SOLIDWORKS API Help"
interface: "IEquationMgr"
member: "GetDisabledEquationCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GetDisabledEquationCount.html"
---

# GetDisabledEquationCount Method (IEquationMgr)

Gets the number of disabled equations in the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDisabledEquationCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEquationMgr
Dim value As System.Integer

value = instance.GetDisabledEquationCount()
```

### C#

```csharp
System.int GetDisabledEquationCount()
```

### C++/CLI

```cpp
System.int GetDisabledEquationCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of disabled equations in the model

## VBA Syntax

See [EquationMgr::GetDisabledEquationCount](ms-its:sldworksapivb6.chm::/sldworks~EquationMgr~GetDisabledEquationCount.html).

## Examples

[Disable Equation (C#)](Disable_Equation_Example_CSharp.htm)
[Disable Equation (VB.NET)](Disable_Equation_Example_VBNET.htm)
[Disable Equation (VBA)](Disable_Equation_Example_VB.htm)

## See Also

[IEquationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.html)
[IEquationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr_members.html)
[IEquationMgr::Disabled Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Disabled.html)
[IEquationMgr::GetCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GetCount.html)
[IEquationMgr::Equation Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Equation.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
