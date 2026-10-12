---
title: "UpdateValuesFromExternalEquationFile Method (IEquationMgr)"
project: "SOLIDWORKS API Help"
interface: "IEquationMgr"
member: "UpdateValuesFromExternalEquationFile"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~UpdateValuesFromExternalEquationFile.html"
---

# UpdateValuesFromExternalEquationFile Method (IEquationMgr)

Updates equations dependent on a linked equation file and ensures that the linked equation file exists and updates its current path, if necessary.

## Syntax

### Visual Basic (Declaration)

```vb
Function UpdateValuesFromExternalEquationFile() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEquationMgr
Dim value As System.Boolean

value = instance.UpdateValuesFromExternalEquationFile()
```

### C#

```csharp
System.bool UpdateValuesFromExternalEquationFile()
```

### C++/CLI

```cpp
System.bool UpdateValuesFromExternalEquationFile();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the equations are updated, false if not

## VBA Syntax

See [EquationMgr::UpdateValuesFromExternalEquationFile](ms-its:sldworksapivb6.chm::/sldworks~EquationMgr~UpdateValuesFromExternalEquationFile.html).

## Examples

[Pack and Go Part and Linked Equation (C#)](Pack_and_Go_Part_and_Linked_Equation_Example_CSharp.htm)
[Pack and Go Part and Linked Equation (VB.NET)](Pack_and_Go_Part_and_Linked_Equation_Example_vbnet.htm)
[Pack and Go Part and Linked Equation (VBA)](Pack_and_Go_Part_and_Linked_Equation_Example_vb.htm)

## See Also

[IEquationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.html)
[IEquationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr_members.html)
[IEquationMgr::LinkToFile Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~LinkToFile.html)
[IEquationMgr::FilePath Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~FilePath.html)

## Availability

SOLIDWORKS 2014 SP1, Revision Number 22.1
