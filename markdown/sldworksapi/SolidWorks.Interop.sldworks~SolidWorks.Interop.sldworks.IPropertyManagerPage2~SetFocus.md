---
title: "SetFocus Method (IPropertyManagerPage2)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPage2"
member: "SetFocus"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~SetFocus.html"
---

# SetFocus Method (IPropertyManagerPage2)

Sets focus on the specified control on this PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetFocus( _
   ByVal ID As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2
Dim ID As System.Integer
Dim value As System.Boolean

value = instance.SetFocus(ID)
```

### C#

```csharp
System.bool SetFocus(
   System.int ID
)
```

### C++/CLI

```cpp
System.bool SetFocus(
   System.int ID
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ID`: User-defined ID of the control where to set focus

### Return Value

True if focus is set on the control, false if not

## VBA Syntax

See [PropertyManagerPage2::SetFocus](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPage2~SetFocus.html).

## Examples

[Set Focus on PropertyManager Page Control (C#)](Set_Focus_on_PropertyManager_Page_Control_Example_CSharp.htm)
[Set Focus on PropertyManager Page Control (VB.NET)](Set_Focus_on_PropertyManager_Page_Control_Example_VBNET.htm)
[Set Focus on PropertyManager Page Control (VBA)](Set_Focus_on_PropertyManager_Page_Control_Example_VB.htm)

## See Also

[IPropertyManagerPage2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.html)
[IPropertyManagerPage2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2_members.html)
[IPropertyManagerPage2::GetFocus Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~GetFocus.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
