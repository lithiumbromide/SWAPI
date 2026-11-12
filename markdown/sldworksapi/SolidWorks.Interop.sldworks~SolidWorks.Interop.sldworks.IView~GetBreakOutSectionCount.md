---
title: "GetBreakOutSectionCount Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetBreakOutSectionCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakOutSectionCount.html"
---

# GetBreakOutSectionCount Method (IView)

Gets the number of broken-out sections in this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBreakOutSectionCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Integer

value = instance.GetBreakOutSectionCount()
```

### C#

```csharp
System.int GetBreakOutSectionCount()
```

### C++/CLI

```cpp
System.int GetBreakOutSectionCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of broken-out sections

## VBA Syntax

See [View::GetBreakOutSectionCount](ms-its:sldworksapivb6.chm::/sldworks~View~GetBreakOutSectionCount.html).

## Examples

[Get Broken-Out Section Feature Data (VBA)](Get_Broken_Out_Section_Feature_Data_Example_VB.htm)
[Get Broken-Out Section Feature Data (VB.NET)](Get_Broken_Out_Section_Feature_Data_Example_VBNET.htm)
[Get Broken-Out Section Feature Data (C#)](Get_Broken_Out_Section_Feature_Data_Example_CSharp.htm)

## Remarks

Call this method before calling [IView::IGetBreakOutSections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetBreakOutSections.html) to determine the size of the array for that method.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetBreakOutSections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakOutSections.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
