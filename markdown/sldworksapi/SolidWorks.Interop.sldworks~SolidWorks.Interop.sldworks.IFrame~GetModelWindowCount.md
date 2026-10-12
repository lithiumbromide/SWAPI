---
title: "GetModelWindowCount Method (IFrame)"
project: "SOLIDWORKS API Help"
interface: "IFrame"
member: "GetModelWindowCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetModelWindowCount.html"
---

# GetModelWindowCount Method (IFrame)

Gets the number of child model windows for this frame.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetModelWindowCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFrame
Dim value As System.Integer

value = instance.GetModelWindowCount()
```

### C#

```csharp
System.int GetModelWindowCount()
```

### C++/CLI

```cpp
System.int GetModelWindowCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of child model windows for this frame

## VBA Syntax

See [Frame::GetModelWindowCount](ms-its:sldworksapivb6.chm::/sldworks~Frame~GetModelWindowCount.html).

## Remarks

Call this method before calling [IFrame::IGetModelWindows](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFrame~IGetModelWindows.html) to get the size of the array.

## See Also

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.html)
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.html)
[IFrame::GetHWnd Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetHWnd.html)
[IFrame::GetHWndx64 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetHWndx64.html)
[IFrame::RemoveMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RemoveMenu.html)
[IFrame::RenameMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RenameMenu.html)
[IFrame::ShowModelWindow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~ShowModelWindow.html)
[IFrame::ModelWindows Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~ModelWindows.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
