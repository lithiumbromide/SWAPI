---
title: "IGetProperties Method (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "IGetProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~IGetProperties.html"
---

# IGetProperties Method (ISheet)

Obsolete. Superseded by [ISheet::GetProperties2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetProperties2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetProperties() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim value As System.Double

value = instance.IGetProperties()
```

### C#

```csharp
System.double IGetProperties()
```

### C++/CLI

```cpp
System.double IGetProperties();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Array of doubles (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

The return value is the following array of seven doubles:

[ paperSize, templateIn, scale1, scale2, firstAngle, width, height ]

where:

paperSize = Paper size. This value is a long or integer packed into a double and is represented by the [swDwgPaperSizes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgPaperSizes_e.html) enumeration.

templateIn = Template index. This value is a long or integer packed into a double and is represented by the [swDwgTemplates_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgTemplates_e.html) enumeration.

scale1 = Scale numerator.

scale2 = Scale denominator.

firstAngle = Value is a Boolean packed into a double and returns true if the sheet is using first angle projection and false if not.

width = Paper width.

height = Paper height.

NOTE: To ensure a correct return value, open the document as read-write or read-only. Insufficient information is available if you open the document as view-only.

You can also use [ISheet::GetSize](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheet~GetSize.html) to get the size of the sheet and the standard sheet size.

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)
[ISheet::GetProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetProperties.html)
[ISheet::GetSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetSize.html)
[ISheet::GetTemplateName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetTemplateName.html)
[ISheet::SetProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetProperties.html)
[ISheet::SetScale Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetScale.html)
[ISheet::SetSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetSize.html)
[ISheet::SetTemplateName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetTemplateName.html)
[ISheet::IPageSetup Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~IPageSetup.html)
[ISheet::PageSetup Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~PageSetup.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
