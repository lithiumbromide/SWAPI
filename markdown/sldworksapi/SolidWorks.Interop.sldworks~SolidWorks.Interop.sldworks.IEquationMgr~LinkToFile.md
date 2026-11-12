---
title: "LinkToFile Property (IEquationMgr)"
project: "SOLIDWORKS API Help"
interface: "IEquationMgr"
member: "LinkToFile"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~LinkToFile.html"
---

# LinkToFile Property (IEquationMgr)

Gets or sets whether the equation is linked to an exported equation text (**.txt**) file.

## Syntax

### Visual Basic (Declaration)

```vb
Property LinkToFile As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEquationMgr
Dim value As System.Boolean

instance.LinkToFile = value

value = instance.LinkToFile
```

### C#

```csharp
System.bool LinkToFile {get; set;}
```

### C++/CLI

```cpp
property System.bool LinkToFile {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the equation is linked to an exported equation text (**.txt**) file, false if not

## VBA Syntax

See [EquationMgr::LinkToFile](ms-its:sldworksapivb6.chm::/sldworks~EquationMgr~LinkToFile.html).

## Examples

Dim swApp As SldWorks.SldWorks
Dim swmodel As SldWorks.ModelDoc2

Option Explicit

Sub main()

Set swApp = Application.SldWorks
Dim equationMgr As SldWorks.EquationMgr
Set swmodel = swApp.**ActiveDoc**
Set equationMgr = swmodel.**GetEquationMgr**
equationMgr.**FilePath** = 'E:\API_SR\equations2.txt'
equationMgr.**LinkToFile** = True

End Sub

## Examples

[Pack and Go Part and Linked Equation (C#)](Pack_and_Go_Part_and_Linked_Equation_Example_CSharp.htm)
[Pack and Go Part and Linked Equation (VB.NET)](Pack_and_Go_Part_and_Linked_Equation_Example_vbnet.htm)
[Pack and Go Part and Linked Equation (VBA)](Pack_and_Go_Part_and_Linked_Equation_Example_vb.htm)

## Remarks

The setter of this property works only after you have set [IEquationMgr::FilePath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~FilePath.html).

## See Also

[IEquationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.html)
[IEquationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr_members.html)
[IEquationMgr::UpdateValuesFromExternalEquationFile Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~UpdateValuesFromExternalEquationFile.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
