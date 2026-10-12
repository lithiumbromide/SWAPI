---
title: "GetSectionLineCount2 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetSectionLineCount2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLineCount2.html"
---

# GetSectionLineCount2 Method (IView)

Gets the number of section lines in the view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSectionLineCount2( _
   ByRef Size As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim Size As System.Integer
Dim value As System.Integer

value = instance.GetSectionLineCount2(Size)
```

### C#

```csharp
System.int GetSectionLineCount2(
   out System.int Size
)
```

### C++/CLI

```cpp
System.int GetSectionLineCount2(
   [Out] System.int Size
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Size`: Size, which includes an extra double per section line containing the layer ID for the section line

### Return Value

Number of section lines in the view

## VBA Syntax

See [View::GetSectionLineCount2](ms-its:sldworksapivb6.chm::/sldworks~View~GetSectionLineCount2.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetSection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSection.html)
[IView::GetSectionLineInfo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLineInfo2.html)
[IView::GetSectionLineStrings Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLineStrings.html)
[IView::IGetSection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSection.html)
[IView::IGetSectionLineInfo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSectionLineInfo2.html)
[IView::IGetSectionLineStrings Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSectionLineStrings.html)
[IView::EnumSectionLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~EnumSectionLines.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
