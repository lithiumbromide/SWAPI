---
title: "GetBreakOutSections Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetBreakOutSections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakOutSections.html"
---

# GetBreakOutSections Method (IView)

Gets all of the broken-out sections in this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBreakOutSections() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetBreakOutSections()
```

### C#

```csharp
System.object GetBreakOutSections()
```

### C++/CLI

```cpp
System.Object^ GetBreakOutSections();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of broken-out section [features](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [View::GetBreakOutSections](ms-its:sldworksapivb6.chm::/sldworks~View~GetBreakOutSections.html).

## Examples

[Get Broken-Out Section Feature Data (C#)](Get_Broken_Out_Section_Feature_Data_Example_CSharp.htm)
[Get Broken-Out Section Feature Data (VB.NET)](Get_Broken_Out_Section_Feature_Data_Example_VBNET.htm)
[Get Broken-Out Section Feature Data (VBA)](Get_Broken_Out_Section_Feature_Data_Example_VB.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::IGetBreakOutSections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBreakOutSections.html)
[IView::GetBreakOutSectionCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakOutSectionCount.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
