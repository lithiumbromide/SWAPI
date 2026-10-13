---
title: "FilePath Property (IEquationMgr)"
project: "SOLIDWORKS API Help"
interface: "IEquationMgr"
member: "FilePath"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~FilePath.html"
---

# FilePath Property (IEquationMgr)

Gets or sets the path for an exported equation text (**.txt**) file.

## Syntax

### Visual Basic (Declaration)

```vb
Property FilePath As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IEquationMgr
Dim value As System.String

instance.FilePath = value

value = instance.FilePath
```

### C#

```csharp
System.string FilePath {get; set;}
```

### C++/CLI

```cpp
property System.String^ FilePath {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Path for the exported equation text (**.txt**) file

## VBA Syntax

See [EquationMgr::FilePath](ms-its:sldworksapivb6.chm::/sldworks~EquationMgr~FilePath.html).

## Examples

[Pack and Go Part and Linked Equation (C#)](Pack_and_Go_Part_and_Linked_Equation_Example_CSharp.htm)
[Pack and Go Part and Linked Equation (VB.NET)](Pack_and_Go_Part_and_Linked_Equation_Example_vbnet.htm)
[Pack and Go Part and Linked Equation (VBA)](Pack_and_Go_Part_and_Linked_Equation_Example_vb.htm)

## See Also

[IEquationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.html)
[IEquationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr_members.html)
[IEquationMgr::LinkToFile Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~LinkToFile.html)
[IEquationMgr::UpdateValuesFromExternalEquationFile Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~UpdateValuesFromExternalEquationFile.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
