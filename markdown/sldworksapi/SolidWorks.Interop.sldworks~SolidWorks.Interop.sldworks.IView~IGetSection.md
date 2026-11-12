---
title: "IGetSection Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetSection"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSection.html"
---

# IGetSection Method (IView)

Gets the section for this section view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSection() As DrSection
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As DrSection

value = instance.IGetSection()
```

### C#

```csharp
DrSection IGetSection()
```

### C++/CLI

```cpp
DrSection^ IGetSection();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Section](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrSection.html) for this section view

## VBA Syntax

See [View::IGetSection](ms-its:sldworksapivb6.chm::/sldworks~View~IGetSection.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::EnumSectionLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~EnumSectionLines.html)
[IView::GetSection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSection.html)
[IView::GetSectionLineCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLineCount2.html)
[IView::GetSectionLineInfo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLineInfo2.html)
[IView::GetSectionLineStrings Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLineStrings.html)
[IView::IGetSectionLineInfo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSectionLineInfo2.html)
[IView::IGetSectionLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSectionLines.html)
[IView::IGetSectionLineStrings Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSectionLineStrings.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
