---
title: "SetWindowHandlex64 Method (IPropertyManagerPageWindowFromHandle)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageWindowFromHandle"
member: "SetWindowHandlex64"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageWindowFromHandle~SetWindowHandlex64.html"
---

# SetWindowHandlex64 Method (IPropertyManagerPageWindowFromHandle)

Sets the handle of this .NET control on 64-bit machines.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetWindowHandlex64( _
   ByVal WindowHandle As System.Long _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageWindowFromHandle
Dim WindowHandle As System.Long
Dim value As System.Boolean

value = instance.SetWindowHandlex64(WindowHandle)
```

### C#

```csharp
System.bool SetWindowHandlex64(
   System.long WindowHandle
)
```

### C++/CLI

```cpp
System.bool SetWindowHandlex64(
   System.int64 WindowHandle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WindowHandle`: 64-bit handle of the .NET control

### Return Value

True if handle is set, false if not

## VBA Syntax

See [PropertyManagerPageWindowFromHandle::SetWindowHandlex64](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageWindowFromHandle~SetWindowHandlex64.html).

## Examples

See the [IPropertyManagerPageWindowFromHandle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageWindowFromHandle.html) examples.

## Remarks

This method is only available through early binding and with 64-bit versions of the SOLIDWORKS Design software.

You must call this method to initialize the .NET control handle whenever you call [IPropertyManagerPage2::Show2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Show2.html), because .NET control handles are destroyed with their forms when the PropertyManager page closes.

## See Also

[IPropertyManagerPageWindowFromHandle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageWindowFromHandle.html)
[IPropertyManagerPageWindowFromHandle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageWindowFromHandle_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
