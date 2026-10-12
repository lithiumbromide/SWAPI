---
title: "GetScaleWithModelChanges Method (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "GetScaleWithModelChanges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetScaleWithModelChanges.html"
---

# GetScaleWithModelChanges Method (IDrSection)

Gets whether the section line scales with changes to the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetScaleWithModelChanges() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
Dim value As System.Boolean

value = instance.GetScaleWithModelChanges()
```

### C#

```csharp
System.bool GetScaleWithModelChanges()
```

### C++/CLI

```cpp
System.bool GetScaleWithModelChanges();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the section line scales with changes to the model, false if it does not

## VBA Syntax

See [DrSection::GetScaleWithModelChanges](ms-its:sldworksapivb6.chm::/sldworks~DrSection~GetScaleWithModelChanges.html).

## Examples

[Create Section View and Get Some Data (C#)](Create_Section_View_and_Get_Some_Data_Example_CSharp.htm)
[Create Section View and Get Some Data (VB.NET)](Create_Section_View_and_Get_Some_Data_Example_VBNET.htm)
[Create Section View and Get Some Data (VBA)](Create_Section_View_and_Get_Some_Data_Example_VB.htm)

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)
[IDrSection::SetScaleWithModelChanges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetScaleWithModelChanges.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
