---
title: "GetProperties2 Method (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "GetProperties2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetProperties2.html"
---

# GetProperties2 Method (ISheet)

Gets the properties for this sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetProperties2() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim value As System.Object

value = instance.GetProperties2()
```

### C#

```csharp
System.object GetProperties2()
```

### C++/CLI

```cpp
System.Object^ GetProperties2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [Sheet::GetProperties2](ms-its:sldworksapivb6.chm::/sldworks~Sheet~GetProperties2.html).

## Examples

[Set Drawing Sheet Properties (C#)](Set_Drawing_Sheet_Properties_Example_CSharp.htm)
[Set Drawing Sheet Properties (VB.NET)](Set_Drawing_Sheet_Properties_Example_VBNET.htm)
[Set Drawing Sheet Properties (VBA)](Set_Drawing_Sheet_Properties_Example_VB.htm)

## Remarks

The return value is the following array of eight doubles:

[ paperSize, templateIn, scale1, scale2, firstAngle, width, height, sameCustomProp ]

where:

paperSize = Paper size; this value is a long or integer packed into a double and is represented by the [swDwgPaperSizes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgPaperSizes_e.html) enumeration

templateIn = Template index; this value is a long or integer packed into a double and is represented by the [swDwgTemplates_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgTemplates_e.html) enumeration

scale1 = Scale numerator

scale2 = Scale denominator

firstAngle = Value is a boolean packed into a double and returns true if the sheet is using first angle projection; false if not

width = Paper width

height = Paper height

`sameCustomProp` = Value is a boolean packed into a double and returns true if the **Same as sheet specified in Document Properties** in the Sheet Properties dialog is selected, false if not

NOTES:

- To ensure a correct return value, open the document as read-write or read-only. Insufficient information is available if you open the document as view-only.
- You can also use [ISheet::GetSize](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheet~GetSize.html) to get the size of the sheet and the standard sheet size.

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)
[ISheet::SetProperties2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetProperties2.html)
[ISheet::PageSetup Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~PageSetup.html)
[ISheet::GetSize Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetSize.html)
[ISheet::SetSize Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetSize.html)
[ISheet::GetTemplateName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetTemplateName.html)
[ISheet::SetTemplateName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetTemplateName.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
