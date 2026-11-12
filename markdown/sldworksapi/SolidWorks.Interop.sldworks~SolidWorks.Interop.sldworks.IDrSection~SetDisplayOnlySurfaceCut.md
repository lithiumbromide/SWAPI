---
title: "SetDisplayOnlySurfaceCut Method (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "SetDisplayOnlySurfaceCut"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetDisplayOnlySurfaceCut.html"
---

# SetDisplayOnlySurfaceCut Method (IDrSection)

Sets whether to display only the surface cut by the section line.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetDisplayOnlySurfaceCut( _
   ByVal Display As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
Dim Display As System.Boolean

instance.SetDisplayOnlySurfaceCut(Display)
```

### C#

```csharp
void SetDisplayOnlySurfaceCut(
   System.bool Display
)
```

### C++/CLI

```cpp
void SetDisplayOnlySurfaceCut(
   System.bool Display
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Display`: True displays only the surface cut by the section line, false does not

## VBA Syntax

See [DrSection::SetDisplayOnlySurfaceCut](ms-its:sldworksapivb6.chm::/sldworks~DrSection~SetDisplayOnlySurfaceCut.html).

## Examples

[Create Section View and Get Some Data (C#)](Create_Section_View_and_Get_Some_Data_Example_CSharp.htm)
[Create Section View and Get Some Data (VB.NET)](Create_Section_View_and_Get_Some_Data_Example_VBNET.htm)
[Create Section View and Get Some Data (VBA)](Create_Section_View_and_Get_Some_Data_Example_VB.htm)

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)
[IDrSection::GetDisplayOnlySurfaceCut Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetDisplayOnlySurfaceCut.html)
[IDrSection::CutSurfaceBodies Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~CutSurfaceBodies.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
