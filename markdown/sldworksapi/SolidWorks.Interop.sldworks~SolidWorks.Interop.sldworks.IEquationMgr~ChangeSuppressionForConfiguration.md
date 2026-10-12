---
title: "ChangeSuppressionForConfiguration Method (IEquationMgr)"
project: "SOLIDWORKS API Help"
interface: "IEquationMgr"
member: "ChangeSuppressionForConfiguration"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~ChangeSuppressionForConfiguration.html"
---

# ChangeSuppressionForConfiguration Method (IEquationMgr)

Changes the suppression state of an equation in the specified configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function ChangeSuppressionForConfiguration( _
   ByVal Index As System.Integer, _
   ByVal ConfigName As System.String, _
   ByVal State As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEquationMgr
Dim Index As System.Integer
Dim ConfigName As System.String
Dim State As System.Boolean
Dim value As System.Integer

value = instance.ChangeSuppressionForConfiguration(Index, ConfigName, State)
```

### C#

```csharp
System.int ChangeSuppressionForConfiguration(
   System.int Index,
   System.string ConfigName,
   System.bool State
)
```

### C++/CLI

```cpp
System.int ChangeSuppressionForConfiguration(
   System.int Index,
   System.String^ ConfigName,
   System.bool State
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 0-based index of the target equation
- `ConfigName`: Configuration in which to supress the equation is (Nothing or null for the current configuration)
- `State`: True suppresses the equation, false unsuppresses it

### Return Value

Index of the equation; -1 if error of if the equation is created in SOLIDWORKS 2014 or later

## VBA Syntax

See [EquationMgr::ChangeSuppressionForConfiguration](ms-its:sldworksapivb6.chm::/sldworks~EquationMgr~ChangeSuppressionForConfiguration.html).

## See Also

[IEquationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.html)
[IEquationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr_members.html)
[IEquationMgr::ChangeSuppressionForAllConfigurations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~ChangeSuppressionForAllConfigurations.html)
[IEquationMgr::GetCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GetCount.html)
[IEquationMgr::Status Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Status.html)
[IEquationMgr::Equation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Equation.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
