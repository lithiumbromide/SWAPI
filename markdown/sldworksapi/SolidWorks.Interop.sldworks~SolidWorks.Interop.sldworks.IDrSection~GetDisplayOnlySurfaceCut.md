---
title: "GetDisplayOnlySurfaceCut Method (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "GetDisplayOnlySurfaceCut"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetDisplayOnlySurfaceCut.html"
---

# GetDisplayOnlySurfaceCut Method (IDrSection)

Gets whether to display only the surface cut by the section line.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDisplayOnlySurfaceCut() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
Dim value As System.Boolean

value = instance.GetDisplayOnlySurfaceCut()
```

### C#

```csharp
System.bool GetDisplayOnlySurfaceCut()
```

### C++/CLI

```cpp
System.bool GetDisplayOnlySurfaceCut();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True to display only the surface cut by the section line, false to not

## VBA Syntax

See [DrSection::GetDisplayOnlySurfaceCut](ms-its:sldworksapivb6.chm::/sldworks~DrSection~GetDisplayOnlySurfaceCut.html).

## Examples

[Create Section View and Get Some Data (C#)](Create_Section_View_and_Get_Some_Data_Example_CSharp.htm)
[Create Section View and Get Some Data (VB.NET)](Create_Section_View_and_Get_Some_Data_Example_VBNET.htm)
[Create Section View and Get Some Data (VBA)](Create_Section_View_and_Get_Some_Data_Example_VB.htm)

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)
[IDrSection::SetDisplayOnlySurfaceCut Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetDisplayOnlySurfaceCut.html)
[IDrSection::CutSurfaceBodies Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~CutSurfaceBodies.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
