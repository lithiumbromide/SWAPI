---
title: "SetTitleBitmapx64 Method (IPropertyManagerPage2)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPage2"
member: "SetTitleBitmapx64"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~SetTitleBitmapx64.html"
---

# SetTitleBitmapx64 Method (IPropertyManagerPage2)

Sets the bitmap to display in the title of this PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetTitleBitmapx64( _
   ByVal ModuleHandle As System.Long, _
   ByVal Identifier As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2
Dim ModuleHandle As System.Long
Dim Identifier As System.Integer
Dim value As System.Boolean

value = instance.SetTitleBitmapx64(ModuleHandle, Identifier)
```

### C#

```csharp
System.bool SetTitleBitmapx64(
   System.long ModuleHandle,
   System.int Identifier
)
```

### C++/CLI

```cpp
System.bool SetTitleBitmapx64(
   System.int64 ModuleHandle,
   System.int Identifier
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ModuleHandle`: Module handle of the application instance that contains the bitmap resource (see **Remarks**)
- `Identifier`: Resource ID of the bitmap (see **Remarks**)

### Return Value

True if successful, false if not

## VBA Syntax

See [PropertyManagerPage2::SetTitleBitmapx64](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPage2~SetTitleBitmapx64.html).

## Remarks

This method is only available through early binding and with 64-bit versions of the SOLIDWORKS Design software. Its intended use is for SOLIDWORKS PropertyManager .NET add-ins. For VBA PropertyManager pages, use [IPropertyManagerPage2::SetTitleBitmap2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~SetTitleBitmap2.html).

You can only use this method to set properties on the PropertyManager page before it is displayed or while it is closed. See [IPropertyManagerPage2::Show2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Show2.html) and [IPropertyManagerPage2::Close](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Close.html) for details.

The bitmap:

- must have less than 256 colors. Its recommended size is 18 - 22 cells wide. However, the bitmap can be any size, as long as it fits on the title bar.
- appears transparent by mapping any white (RGB(255,255,255)) cells to the current PropertyManager page title bar background color. Remember the special use of this color as you design your bitmap.
- must be a resource in your Visual Studio application. You must discover its resource ID before you can specify Identifier.

Specify ModuleHandle using the add-in ID.

| If this method is... | Then the title bar contains... |
| --- | --- |
| Used | Specified bitmap starting at the left edge of the PropertyManager title bar, followed by the title bar text (see ISldWorks::CreatePropertyManagerPage or ISldWorks::ICreatePropertyManagerPage ). |
| Not used | Only the text, centered on the title bar. |

## See Also

[IPropertyManagerPage2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.html)
[IPropertyManagerPage2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2_members.html)

## Availability

SOLIDWORKS 2010 SP3, Revision Number 18.3
