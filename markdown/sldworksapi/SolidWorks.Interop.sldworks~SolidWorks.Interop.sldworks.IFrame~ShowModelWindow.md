---
title: "ShowModelWindow Method (IFrame)"
project: "SOLIDWORKS API Help"
interface: "IFrame"
member: "ShowModelWindow"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~ShowModelWindow.html"
---

# ShowModelWindow Method (IFrame)

Shows a client model window.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ShowModelWindow( _
   ByVal LpModelWindow As ModelWindow _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IFrame
Dim LpModelWindow As ModelWindow

instance.ShowModelWindow(LpModelWindow)
```

### C#

```csharp
void ShowModelWindow(
   ModelWindow LpModelWindow
)
```

### C++/CLI

```cpp
void ShowModelWindow(
   ModelWindow^ LpModelWindow
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `LpModelWindow`: [Model window](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelWindow.html)

## VBA Syntax

See [Frame::ShowModelWindow](ms-its:sldworksapivb6.chm::/sldworks~Frame~ShowModelWindow.html).

## Examples

[Switch Documents (C#)](Switch_Documents_Example_CSharp.htm)
[Switch Documents (VB.NET)](Switch_Documents_Example_VBNET.htm)
[Switch Documents (VBA)](Switch_Documents_Example_VB.htm)

## See Also

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.html)
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.html)
[IFrame::GetHWnd Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetHWnd.html)
[IFrame::GetHWndx64 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetHWndx64.html)
[IFrame::GetModelWindowCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetModelWindowCount.html)
[IFrame::IGetModelWindows Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~IGetModelWindows.html)
[IFrame::ModelWindows Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~ModelWindows.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
