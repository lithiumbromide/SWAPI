---
title: "EnumSectionLines Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "EnumSectionLines"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~EnumSectionLines.html"
---

# EnumSectionLines Method (IView)

Obsolete. Superseded by [IView::EnumSectionLines2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~EnumSectionLines2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function EnumSectionLines() As EnumDrSections
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As EnumDrSections

value = instance.EnumSectionLines()
```

### C#

```csharp
EnumDrSections EnumSectionLines()
```

### C++/CLI

```cpp
EnumDrSections^ EnumSectionLines();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Section lines enumeration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumDrSections.html)

## VBA Syntax

See [View::EnumSectionLines](ms-its:sldworksapivb6.chm::/sldworks~View~EnumSectionLines.html).

## Remarks

This method returns the section lines regardless of whether the view is visible. If the view is hidden, then the section lines are still returned.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetSectionLineCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLineCount2.html)
[IView::GetSectionLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLines.html)
[IView::GetSectionLineStrings Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLineStrings.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
