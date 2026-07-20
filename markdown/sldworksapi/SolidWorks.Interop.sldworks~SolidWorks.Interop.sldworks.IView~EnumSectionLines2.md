---
title: "EnumSectionLines2 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "EnumSectionLines2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~EnumSectionLines2.html"
---

# EnumSectionLines2 Method (IView)

Gets the section lines enumeration in the view.

## Syntax

### Visual Basic (Declaration)

```vb
Function EnumSectionLines2( _
   ByVal IgnoreSuppressed As System.Boolean _
) As EnumDrSections
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim IgnoreSuppressed As System.Boolean
Dim value As EnumDrSections

value = instance.EnumSectionLines2(IgnoreSuppressed)
```

### C#

```csharp
EnumDrSections EnumSectionLines2(
   System.bool IgnoreSuppressed
)
```

### C++/CLI

```cpp
EnumDrSections^ EnumSectionLines2(
   System.bool IgnoreSuppressed
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `IgnoreSuppressed`: True to ignore suppressed section lines, false to include them

### Return Value

[Section lines enumeration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumDrSections.html)

## VBA Syntax

See

[View::EnumSectionLines2](ms-its:sldworksapivb6.chm::/sldworks~View~EnumSectionLines2.html)

.

## Remarks

This method returns section lines whether the view is visible or not. If the view is hidden, then the section lines are still returned.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)

[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)

[IView::GetSectionLineCount2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLineCount2.html)

[IView::GetSectionLines Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLines.html)

[IView::GetSectionLineStrings Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLineStrings.html)

## Availability

SOLIDWORKS 2024 SP01, Revision Number 32.1
