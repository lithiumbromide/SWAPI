---
title: "ChangeSuppressionForAllConfigurations Method (IEquationMgr)"
project: "SOLIDWORKS API Help"
interface: "IEquationMgr"
member: "ChangeSuppressionForAllConfigurations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~ChangeSuppressionForAllConfigurations.html"
---

# ChangeSuppressionForAllConfigurations Method (IEquationMgr)

Changes the suppression state of the specified equation in all configurations.

## Syntax

### Visual Basic (Declaration)

```vb
Function ChangeSuppressionForAllConfigurations( _
   ByVal Index As System.Integer, _
   ByVal State As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEquationMgr
Dim Index As System.Integer
Dim State As System.Boolean
Dim value As System.Integer

value = instance.ChangeSuppressionForAllConfigurations(Index, State)
```

### C#

```csharp
System.int ChangeSuppressionForAllConfigurations(
   System.int Index,
   System.bool State
)
```

### C++/CLI

```cpp
System.int ChangeSuppressionForAllConfigurations(
   System.int Index,
   System.bool State
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 0-based index of the target equation
- `State`: True suppresses the equation, false unsuppresses it

### Return Value

Index of the equation; -1 if error or if the equation was created in SOLIDWORKS 2014 or later

## VBA Syntax

See [EquationMgr::ChangeSuppressionForAllConfigurations](ms-its:sldworksapivb6.chm::/sldworks~EquationMgr~ChangeSuppressionForAllConfigurations.html).

## See Also

[IEquationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.html)
[IEquationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr_members.html)
[IEquationMgr::ChangeSuppressionForConfiguration Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~ChangeSuppressionForConfiguration.html)
[IEquationMgr::GetCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GetCount.html)
[IEquationMgr::Status Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Status.html)
[IEquationMgr::Equation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Equation.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
