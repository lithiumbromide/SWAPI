---
title: "GetAutoHatch Method (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "GetAutoHatch"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetAutoHatch.html"
---

# GetAutoHatch Method (IDrSection)

Gets whether auto hatching is enabled for the section view resulting from this section cut.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAutoHatch() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
Dim value As System.Boolean

value = instance.GetAutoHatch()
```

### C#

```csharp
System.bool GetAutoHatch()
```

### C++/CLI

```cpp
System.bool GetAutoHatch();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if auto hatching is enabled for the section view, false if it is disabled

## VBA Syntax

See [DrSection::GetAutoHatch](ms-its:sldworksapivb6.chm::/sldworks~DrSection~GetAutoHatch.html).

## Examples

[Create Section View and Get Some Data (C#)](Create_Section_View_and_Get_Some_Data_Example_CSharp.htm)
[Create Section View and Get Some Data (VB.NET)](Create_Section_View_and_Get_Some_Data_Example_VBNET.htm)
[Create Section View and Get Some Data (VBA)](Create_Section_View_and_Get_Some_Data_Example_VB.htm)

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)
[IDrSection::SetAutoHatch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetAutoHatch.html)
[IDrSection::ScaleHatchPattern Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~ScaleHatchPattern.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
