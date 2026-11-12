---
title: "GetHWndx64 Method (IFrame)"
project: "SOLIDWORKS API Help"
interface: "IFrame"
member: "GetHWndx64"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetHWndx64.html"
---

# GetHWndx64 Method (IFrame)

Gets the window handle for the main frame in 64-bit applications.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetHWndx64() As System.Long
```

### Visual Basic (Usage)

```vb
Dim instance As IFrame
Dim value As System.Long

value = instance.GetHWndx64()
```

### C#

```csharp
System.long GetHWndx64()
```

### C++/CLI

```cpp
System.int64 GetHWndx64();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Window handle

## VBA Syntax

See [Frame::GetHWndx64](ms-its:sldworksapivb6.chm::/sldworks~Frame~GetHWndx64.html).

## Remarks

This method is only available through early binding and with 64-bit versions of the SOLIDWORKS Design software.

## See Also

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.html)
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.html)
[IFrame::GetHWnd Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetHWnd.html)
[IFrame::GetModelWindowCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetModelWindowCount.html)
[IFrame::IGetModelWindows Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~IGetModelWindows.html)
[IFrame::ShowModelWindow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~ShowModelWindow.html)
[IFrame::ModelWindows Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~ModelWindows.html)

## Availability

SOLIDWORKS 2006 SP2, Revision Number 14.2
