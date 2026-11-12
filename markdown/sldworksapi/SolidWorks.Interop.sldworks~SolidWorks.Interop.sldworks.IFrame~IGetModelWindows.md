---
title: "IGetModelWindows Method (IFrame)"
project: "SOLIDWORKS API Help"
interface: "IFrame"
member: "IGetModelWindows"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~IGetModelWindows.html"
---

# IGetModelWindows Method (IFrame)

Gets the child model windows for this frame.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetModelWindows( _
   ByVal ModelWindowCount As System.Integer _
) As ModelWindow
```

### Visual Basic (Usage)

```vb
Dim instance As IFrame
Dim ModelWindowCount As System.Integer
Dim value As ModelWindow

value = instance.IGetModelWindows(ModelWindowCount)
```

### C#

```csharp
ModelWindow IGetModelWindows(
   System.int ModelWindowCount
)
```

### C++/CLI

```cpp
ModelWindow^ IGetModelWindows(
   System.int ModelWindowCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ModelWindowCount`: Number of child windows for this frame

### Return Value

- in-process, unmanaged C++: Pointer to an array of [model windows](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelWindow.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IFrame::GetModelWindowCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFrame~GetModelWindowCount.html) before calling this method to get the size of the array.

## See Also

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.html)
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.html)
[IFrame::GetHWnd Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetHWnd.html)
[IFrame::GetHWndx64 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetHWndx64.html)
[IFrame::ShowModelWindow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~ShowModelWindow.html)
[IFrame::ModelWindows Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~ModelWindows.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
