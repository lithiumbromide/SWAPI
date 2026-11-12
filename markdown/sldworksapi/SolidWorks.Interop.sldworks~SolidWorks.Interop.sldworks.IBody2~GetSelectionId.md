---
title: "GetSelectionId Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "GetSelectionId"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetSelectionId.html"
---

# GetSelectionId Method (IBody2)

Gets the selection ID of the body, if one exists.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSelectionId() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As System.String

value = instance.GetSelectionId()
```

### C#

```csharp
System.string GetSelectionId()
```

### C++/CLI

```cpp
System.String^ GetSelectionId();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Selection ID of the body

## VBA Syntax

See [Body2::GetSelectionId](ms-its:sldworksapivb6.chm::/sldworks~Body2~GetSelectionId.html).

## Examples

[Get Names of Bodies in MultiBody Part (VBA)](Get_Names_of_Bodies_in_MultiBody_Part_Example_VB.htm)
[Select Bodies (VBA)](Select_Bodies_Example_VB.htm)
[Set Body for View (C#)](Set_Body_for_View_Example_CSharp.htm)
[Set Body for View (VB.NET)](Set_Body_for_View_Example_VBNET.htm)
[Set Body for View (VBA)](Set_Body_for_View_Example_VB.htm)

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
