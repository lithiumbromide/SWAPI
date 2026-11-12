---
title: "SetTitleBitmap Method (IPropertyManagerPage2)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPage2"
member: "SetTitleBitmap"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~SetTitleBitmap.html"
---

# SetTitleBitmap Method (IPropertyManagerPage2)

Obsolete. Superseded by [IPropertyManagerPage2::SetTitleBitmapx64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~SetTitleBitmapx64.html).

This method is unsafe to use with 64-bit SOLIDWORKS, i.e. all versions since SOLIDWORKS 2016.

The 32-bit integer returned may be to small to contain the 64-bit window handle/pointer, and will be truncated silently. A critical exception will occur sometime later, when the truncated handle/pointer is used.

Sets the bitmap to display in the title of this PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetTitleBitmap( _
   ByVal ModuleHandle As System.Integer, _
   ByVal Identifier As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2
Dim ModuleHandle As System.Integer
Dim Identifier As System.Integer
Dim value As System.Boolean

value = instance.SetTitleBitmap(ModuleHandle, Identifier)
```

### C#

```csharp
System.bool SetTitleBitmap(
   System.int ModuleHandle,
   System.int Identifier
)
```

### C++/CLI

```cpp
System.bool SetTitleBitmap(
   System.int ModuleHandle,
   System.int Identifier
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ModuleHandle`:
- `Identifier`:

## VBA Syntax

See [PropertyManagerPage2::SetTitleBitmap](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPage2~SetTitleBitmap.html).

## Remarks

**All applications are required to be compatible with SOLIDWORKS x64. You must replace all calls to 32-bit only APIs with calls to their 64-bit safe counterparts.**

See [Eliminating 32-bit only API use](sldworksapiprogguide.chm::/Overview/Eliminating_32-Bit_Only_API_Use.htm) for more information.

## See Also

[IPropertyManagerPage2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.html)
[IPropertyManagerPage2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2_members.html)
