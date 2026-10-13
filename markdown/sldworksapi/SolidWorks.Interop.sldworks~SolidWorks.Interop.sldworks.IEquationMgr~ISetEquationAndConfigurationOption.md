---
title: "ISetEquationAndConfigurationOption Method (IEquationMgr)"
project: "SOLIDWORKS API Help"
interface: "IEquationMgr"
member: "ISetEquationAndConfigurationOption"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~ISetEquationAndConfigurationOption.html"
---

# ISetEquationAndConfigurationOption Method (IEquationMgr)

Modifies the equation at the specified index for the specified configurations.

## Syntax

### Visual Basic (Declaration)

```vb
Function ISetEquationAndConfigurationOption( _
   ByVal Index As System.Integer, _
   ByVal Equation As System.String, _
   ByVal WhichConfigurations As System.Integer, _
   ByVal ConfigCount As System.Integer, _
   ByRef ConfigNames As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEquationMgr
Dim Index As System.Integer
Dim Equation As System.String
Dim WhichConfigurations As System.Integer
Dim ConfigCount As System.Integer
Dim ConfigNames As System.String
Dim value As System.Integer

value = instance.ISetEquationAndConfigurationOption(Index, Equation, WhichConfigurations, ConfigCount, ConfigNames)
```

### C#

```csharp
System.int ISetEquationAndConfigurationOption(
   System.int Index,
   System.string Equation,
   System.int WhichConfigurations,
   System.int ConfigCount,
   ref System.string ConfigNames
)
```

### C++/CLI

```cpp
System.int ISetEquationAndConfigurationOption(
   System.int Index,
   System.String^ Equation,
   System.int WhichConfigurations,
   System.int ConfigCount,
   System.String^% ConfigNames
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 0-based index of the equation to modify
- `Equation`: String containing the modified equation (see **Remarks**)
- `WhichConfigurations`: Configuration option as defined in [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)
- `ConfigCount`: Number of names in ConfigNames array
- `ConfigNames`: - in-process, in-process, unmanaged C++: Pointer to an array of strings containing configuration names

  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

0 if equation successfully added, -1 if error

## Remarks

This method modifies only equations added using [IEquationMgr::IAdd3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEquationMgr~IAdd3.html).

To add an equation using the SOLIDWORKS Design user interface, you must embed the names of dimensions and global variables in double quotes:

- Global variable assignment:
  **"B" = 2**
- Component equation:
  **"N_SPOKES@CirPattern" = "BARLENGTH@Sketch2" /10**
- Dimension equation that uses the Visual Basic IIf function:
  **"D1@Extrude2" = (IIf("D1@Extrude3">20, 15, 6))+5**
- Dimension equation that sets a dimension to the current value:
  **"D1@Extrude2" =**
- Dimension equation that modifies the right-hand side of an already existing dimension equation:
  **"D1@Extrude2" = 0.05**

**NOTES:**

- To modify an equation:

  - you must specify Equation with the names of dimensions and global variables in double double quotes and the entire equation in double quotes. The examples for [IEquationMgr::Add3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEquationMgr~Add3.html) show how to do this. [Global variables](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GlobalVariable.html) cannot be set to current values using this method.
  - added directly to an assembly component's model, you must call [IAssemblyDoc::EditPart2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EditPart2.html) before calling this method.
- If you change the active configuration, then you must call [IModelDoc2::GetEquationMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetEquationMgr.html) again.
- If the model has just one configuration, then use [IEquationMgr::Equation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Equation.html).

## See Also

[IEquationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.html)
[IEquationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr_members.html)
[IEquationMgr::SetEquationAndConfigurationOption Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~SetEquationAndConfigurationOption.html)
[IEquationMgr::GetConfigurationOption Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GetConfigurationOption.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
