---
title: "GetColorTable Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetColorTable"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetColorTable.html"
---

# GetColorTable Method (ISldWorks)

Gets a color table from the SOLIDWORKS Design application.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetColorTable() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.Object

value = instance.GetColorTable()
```

### C#

```csharp
System.object GetColorTable()
```

### C++/CLI

```cpp
System.Object^ GetColorTable();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Color table](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IColorTable.html)

## VBA Syntax

See [SldWorks::GetColorTable](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetColorTable.html).

## Examples

[Get COLORREF Values of Standard User-interface Elements (C#)](Get_COLORREF_Values_of_Standard_User-interface_Elements_Example_CSharp.htm)
[Get COLORREF Values of Standard User-interface Elements (VB.NET)](Get_COLORREF_Values_of_Standard_User-interface_Elements_Example_VBNET.htm)
[Get COLORREF Values of Standard User-interface Elements (VBA)](Get_COLORREF_Values_of_Standard_User-interface_Elements_Example_VB.htm)

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::IGetColorTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetColorTable.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
