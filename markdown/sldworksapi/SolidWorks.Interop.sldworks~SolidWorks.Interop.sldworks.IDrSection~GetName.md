---
title: "GetName Method (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "GetName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetName.html"
---

# GetName Method (IDrSection)

Gets the name of the section line.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetName() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
Dim value As System.String

value = instance.GetName()
```

### C#

```csharp
System.string GetName()
```

### C++/CLI

```cpp
System.String^ GetName();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Name of the section line

## VBA Syntax

See [DrSection::GetName](ms-its:sldworksapivb6.chm::/sldworks~DrSection~GetName.html).

## Examples

[Get Section View (VBA)](Get_Section_View_Data_Example_VB.htm)
[Create Section View and Get Some Data (C#)](Create_Section_View_and_Get_Some_Data_Example_CSharp.htm)
[Create Section View and Get Some Data (VB.NET)](Create_Section_View_and_Get_Some_Data_Example_VBNET.htm)
[Create Section View and Get Some Data (VBA)](Create_Section_View_and_Get_Some_Data_Example_VB.htm)

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)
[IView::EnumSectionLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~EnumSectionLines.html)
[IView::GetSectionLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLines.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
