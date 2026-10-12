---
title: "SetWindowHandle Method (IPropertyManagerPageWindowFromHandle)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageWindowFromHandle"
member: "SetWindowHandle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageWindowFromHandle~SetWindowHandle.html"
---

# SetWindowHandle Method (IPropertyManagerPageWindowFromHandle)

Obsolete. Superseded by [IPropertyManagerPageWindowFromHandle::SetWindowHandlex64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageWindowFromHandle~SetWindowHandlex64.html).

This method is unsafe to use with 64-bit SOLIDWORKS, i.e. all versions since SOLIDWORKS 2016.

The 32-bit integer returned may be to small to contain the 64-bit window handle/pointer, and will be truncated silently. A critical exception will occur sometime later, when the truncated handle/pointer is used.

Sets the handle of this .NET control.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetWindowHandle( _
   ByVal WindowHandle As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageWindowFromHandle
Dim WindowHandle As System.Integer
Dim value As System.Boolean

value = instance.SetWindowHandle(WindowHandle)
```

### C#

```csharp
System.bool SetWindowHandle(
   System.int WindowHandle
)
```

### C++/CLI

```cpp
System.bool SetWindowHandle(
   System.int WindowHandle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WindowHandle`: Handle of the .NET control

### Return Value

True if handle is set, false if not

## VBA Syntax

See [PropertyManagerPageWindowFromHandle::SetWindowHandle](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageWindowFromHandle~SetWindowHandle.html).

## Remarks

**All applications are required to be compatible with SOLIDWORKS x64. You must replace all calls to 32-bit only APIs with calls to their 64-bit safe counterparts.**

See [Eliminating 32-bit only API use](sldworksapiprogguide.chm::/Overview/Eliminating_32-Bit_Only_API_Use.htm) for more information.

You must call this method to initialize the .NET control handle whenever you call [IPropertyManagerPage2::Show2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Show2.html), because .NET control handles are destroyed with their forms when the PropertyManager page closes.

## See Also

[IPropertyManagerPageWindowFromHandle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageWindowFromHandle.html)
[IPropertyManagerPageWindowFromHandle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageWindowFromHandle_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
