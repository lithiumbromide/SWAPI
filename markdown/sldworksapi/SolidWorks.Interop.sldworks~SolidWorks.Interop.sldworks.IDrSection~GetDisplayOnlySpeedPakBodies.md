---
title: "GetDisplayOnlySpeedPakBodies Method (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "GetDisplayOnlySpeedPakBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetDisplayOnlySpeedPakBodies.html"
---

# GetDisplayOnlySpeedPakBodies Method (IDrSection)

Gets whether to display in this section view only the bodies included in the SpeedPak configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDisplayOnlySpeedPakBodies() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
Dim value As System.Boolean

value = instance.GetDisplayOnlySpeedPakBodies()
```

### C#

```csharp
System.bool GetDisplayOnlySpeedPakBodies()
```

### C++/CLI

```cpp
System.bool GetDisplayOnlySpeedPakBodies();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True to display only the bodies included in the SpeedPak configuration, false to not

## VBA Syntax

See [DrSection::GetDisplayOnlySpeedPakBodies](ms-its:sldworksapivb6.chm::/sldworks~DrSection~GetDisplayOnlySpeedPakBodies.html).

## Examples

[Create Section View and Get Some Data (VBA)](Create_Section_View_and_Get_Some_Data_Example_VB.htm)
[Create Section View and Get Some Data (VB.NET)](Create_Section_View_and_Get_Some_Data_Example_VBNET.htm)
[Create Section View and Get Some Data (C#)](Create_Section_View_and_Get_Some_Data_Example_CSharp.htm)

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)
[IDrSection::SetDisplayOnlySpeedPakBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetDisplayOnlySpeedPakBodies.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
