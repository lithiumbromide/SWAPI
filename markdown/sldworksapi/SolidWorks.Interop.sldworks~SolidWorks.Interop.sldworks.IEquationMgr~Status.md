---
title: "Status Property (IEquationMgr)"
project: "SOLIDWORKS API Help"
interface: "IEquationMgr"
member: "Status"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Status.html"
---

# Status Property (IEquationMgr)

Gets the status of the last equation that was executed.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Status As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEquationMgr
Dim value As System.Integer

value = instance.Status
```

### C#

```csharp
System.int Status {get;}
```

### C++/CLI

```cpp
property System.int Status {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0-based index of the last equation to successfully execute; -1 if there was an error (see **Remarks**)

## VBA Syntax

See [EquationMgr::Status](ms-its:sldworksapivb6.chm::/sldworks~EquationMgr~Status.html).

## Examples

[Get Equation Values (C#)](Get_Equation_Values_Example_CSharp.htm)
[Get Equation Values (VB.NET)](Get_Equation_Values_Example_VBNET.htm)
[Get Equation Values (VBA)](Get_Equation_Values_Example_VB.htm)

## Remarks

If you call an IEquationMgr method or property that takes the index of an equation as an argument (e.g., [IEquationMgr::Value](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEquationMgr~Value.html)) and call IEquationMgr::Status, then the return value is:

- index of the equation if the call is successful.
- -1 if there is an error.

## See Also

[IEquationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.html)
[IEquationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr_members.html)
[IEquationMgr::Add2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Add2.html)
[IEquationMgr::ChangeSuppressionForAllConfigurations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~ChangeSuppressionForAllConfigurations.html)
[IEquationMgr::ChangeSuppressionForConfiguration Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~ChangeSuppressionForConfiguration.html)
[IEquationMgr::Delete Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Delete.html)
[IEquationMgr::Equation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Equation.html)
[IEquationMgr::EvaluateAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~EvaluateAll.html)
[IEquationMgr::Add3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Add3.html)
[IEquationMgr::GetCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GetCount.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
