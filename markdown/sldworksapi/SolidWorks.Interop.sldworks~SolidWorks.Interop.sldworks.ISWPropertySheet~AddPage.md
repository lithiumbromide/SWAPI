---
title: "AddPage Method (ISWPropertySheet)"
project: "SOLIDWORKS API Help"
interface: "ISWPropertySheet"
member: "AddPage"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet~AddPage.html"
---

# AddPage Method (ISWPropertySheet)

Obsolete. Superseded by [ISWPropertySheet::AddPagex64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet~AddPagex64.html).

This method is unsafe to use with 64-bit SOLIDWORKS, i.e. all versions since SOLIDWORKS 2016.

The 32-bit integer returned may be to small to contain the 64-bit window handle/pointer, and will be truncated silently. A critical exception will occur sometime later, when the truncated handle/pointer is used.

Adds a CPropertyPage-derived page to an [ISWPropertySheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISWPropertySheet.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddPage( _
   ByVal Page As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISWPropertySheet
Dim Page As System.Integer
Dim value As System.Integer

value = instance.AddPage(Page)
```

### C#

```csharp
System.int AddPage(
   System.int Page
)
```

### C++/CLI

```cpp
System.int AddPage(
   System.int Page
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Page`: Pointer to the CPropertyPage to add, cast to a long

### Return Value

True if successful, false if not

## VBA Syntax

See [SWPropertySheet::AddPage](ms-its:sldworksapivb6.chm::/sldworks~SWPropertySheet~AddPage.html).

## Remarks

**All applications are required to be compatible with SOLIDWORKS x64. You must replace all calls to 32-bit only APIs with calls to their 64-bit safe counterparts.**

See [Eliminating 32-bit only API use](sldworksapiprogguide.chm::/Overview/Eliminating_32-Bit_Only_API_Use.htm) for more information.

## See Also

[ISWPropertySheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet.html)
[ISWPropertySheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet_members.html)
