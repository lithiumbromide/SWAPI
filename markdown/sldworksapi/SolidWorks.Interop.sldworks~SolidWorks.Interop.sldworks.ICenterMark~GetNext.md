---
title: "GetNext Method (ICenterMark)"
project: "SOLIDWORKS API Help"
interface: "ICenterMark"
member: "GetNext"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~GetNext.html"
---

# GetNext Method (ICenterMark)

Gets the next center mark.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNext() As CenterMark
```

### Visual Basic (Usage)

```vb
Dim instance As ICenterMark
Dim value As CenterMark

value = instance.GetNext()
```

### C#

```csharp
CenterMark GetNext()
```

### C++/CLI

```cpp
CenterMark^ GetNext();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Next [center mark](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICenterMark.html)

## VBA Syntax

See [CenterMark::GetNext](ms-its:sldworksapivb6.chm::/sldworks~CenterMark~GetNext.html).

## Examples

[List Center Marks in Drawing (VBA)](List_Center_Marks_in_Drawing_Example_VB.htm)
[Select All Center Marks (C#)](Select_All_Center_Marks_Example_CSharp.htm)
[Select All Center Marks (VB.NET)](Select_All_Center_Marks_Example_VBNET.htm)
[Select All Center Marks (VBA)](Select_All_Center_Marks_Example_VB.htm)

## See Also

[ICenterMark Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.html)
[ICenterMark Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark_members.html)
[IView::GetCenterMarks Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterMarks.html)
[IView::GetFirstCenterMark Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstCenterMark.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
