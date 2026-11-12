---
title: "GetConfigurationOption Method (IEquationMgr)"
project: "SOLIDWORKS API Help"
interface: "IEquationMgr"
member: "GetConfigurationOption"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GetConfigurationOption.html"
---

# GetConfigurationOption Method (IEquationMgr)

Gets the configuration option for the equation at the specified index.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetConfigurationOption( _
   ByVal Index As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEquationMgr
Dim Index As System.Integer
Dim value As System.Integer

value = instance.GetConfigurationOption(Index)
```

### C#

```csharp
System.int GetConfigurationOption(
   System.int Index
)
```

### C++/CLI

```cpp
System.int GetConfigurationOption(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 0-based index of equation for which to get the configuration option

### Return Value

Configuration option as defined in [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)

## VBA Syntax

See [EquationMgr::GetConfigurationOption](ms-its:sldworksapivb6.chm::/sldworks~EquationMgr~GetConfigurationOption.html).

## Remarks

This method only works for documents created in SOLIDWORKS 2014 or later.

## See Also

[IEquationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.html)
[IEquationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr_members.html)
[IEquationMgr::Add3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Add3.html)
[IEquationMgr::IAdd3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~IAdd3.html)
[IEquationMgr::Equation Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Equation.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
