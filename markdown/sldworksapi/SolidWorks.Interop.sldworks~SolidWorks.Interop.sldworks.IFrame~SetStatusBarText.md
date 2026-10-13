---
title: "SetStatusBarText Method (IFrame)"
project: "SOLIDWORKS API Help"
interface: "IFrame"
member: "SetStatusBarText"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~SetStatusBarText.html"
---

# SetStatusBarText Method (IFrame)

Displays a text string in the main status bar area to the left of the status bar.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetStatusBarText( _
   ByVal MessageString As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IFrame
Dim MessageString As System.String

instance.SetStatusBarText(MessageString)
```

### C#

```csharp
void SetStatusBarText(
   System.string MessageString
)
```

### C++/CLI

```cpp
void SetStatusBarText(
   System.String^ MessageString
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `MessageString`: Text to display in the status bar

## VBA Syntax

See [Frame::SetStatusBarText](ms-its:sldworksapivb6.chm::/sldworks~Frame~SetStatusBarText.html).

## See Also

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.html)
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.html)
[IFrame::GetStatusBarPane Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetStatusBarPane.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
