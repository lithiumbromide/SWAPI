---
title: "GetMenux64 Method (IFrame)"
project: "SOLIDWORKS API Help"
interface: "IFrame"
member: "GetMenux64"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetMenux64.html"
---

# GetMenux64 Method (IFrame)

Gets the menu handle for the main frame in 64-bit applications.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMenux64() As System.Long
```

### Visual Basic (Usage)

```vb
Dim instance As IFrame
Dim value As System.Long

value = instance.GetMenux64()
```

### C#

```csharp
System.long GetMenux64()
```

### C++/CLI

```cpp
System.int64 GetMenux64();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Menu handle for the main frame

## VBA Syntax

See [Frame::GetMenux64](ms-its:sldworksapivb6.chm::/sldworks~Frame~GetMenux64.html).

## Remarks

This method is only available through early binding and with 64-bit versions of the SOLIDWORKS Design software.

## See Also

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.html)
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.html)
[IFrame::GetMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetMenu.html)
[IFrame::GetHWndx64 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetHWndx64.html)
[IFrame::GetHWnd Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetHWnd.html)

## Availability

SOLIDWORKS 2008 SP2, Revision Number 16.2
