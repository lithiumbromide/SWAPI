---
title: "GetSectionLineStrings Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetSectionLineStrings"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLineStrings.html"
---

# GetSectionLineStrings Method (IView)

Gets an array of strings; each string represents the text label for a section line in this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSectionLineStrings() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetSectionLineStrings()
```

### C#

```csharp
System.object GetSectionLineStrings()
```

### C++/CLI

```cpp
System.Object^ GetSectionLineStrings();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of strings with one string for each section line in the view

## VBA Syntax

See [View::GetSectionLineStrings](ms-its:sldworksapivb6.chm::/sldworks~View~GetSectionLineStrings.html).

## Remarks

To determine the number of the strings returned, call [IView::GetSectionLineCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetSectionLineCount2.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::EnumSectionLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~EnumSectionLines.html)
[IView::GetSection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSection.html)
[IView::GetSectionLineInfo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLineInfo2.html)
[IView::GetSectionLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLines.html)
[IView::IGetSection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSection.html)
[IView::IGetSectionLineInfo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSectionLineInfo2.html)
[IView::IGetSectionLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSectionLines.html)
[IView::IGetSectionLineStrings Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSectionLineStrings.html)
