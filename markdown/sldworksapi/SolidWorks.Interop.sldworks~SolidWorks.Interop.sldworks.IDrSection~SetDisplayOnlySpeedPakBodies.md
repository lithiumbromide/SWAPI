---
title: "SetDisplayOnlySpeedPakBodies Method (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "SetDisplayOnlySpeedPakBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetDisplayOnlySpeedPakBodies.html"
---

# SetDisplayOnlySpeedPakBodies Method (IDrSection)

Sets whether to display in this section view only the bodies included in the SpeedPak configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetDisplayOnlySpeedPakBodies( _
   ByVal Display As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
Dim Display As System.Boolean

instance.SetDisplayOnlySpeedPakBodies(Display)
```

### C#

```csharp
void SetDisplayOnlySpeedPakBodies(
   System.bool Display
)
```

### C++/CLI

```cpp
void SetDisplayOnlySpeedPakBodies(
   System.bool Display
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Display`: True to display only the bodies included in the SpeedPak configuration, false to not

## VBA Syntax

See [DrSection::SetDisplayOnlySpeedPakBodies](ms-its:sldworksapivb6.chm::/sldworks~DrSection~SetDisplayOnlySpeedPakBodies.html).

## Examples

[Create Section View and Get Some Data (VBA)](Create_Section_View_and_Get_Some_Data_Example_VB.htm)
[Create Section View and Get Some Data (VB.NET)](Create_Section_View_and_Get_Some_Data_Example_VBNET.htm)
[Create Section View and Get Some Data (C#)](Create_Section_View_and_Get_Some_Data_Example_CSharp.htm)

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)
[IDrSection::GetDisplayOnlySpeedPakBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetDisplayOnlySpeedPakBodies.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
