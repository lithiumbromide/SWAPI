---
title: "End Method (IUserProgressBar)"
project: "SOLIDWORKS API Help"
interface: "IUserProgressBar"
member: "End"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserProgressBar~End.html"
---

# End Method (IUserProgressBar)

Removes the progress indicator from the SOLIDWORKS status bar.

## Syntax

### Visual Basic (Declaration)

```vb
Function End() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IUserProgressBar
Dim value As System.Boolean

value = instance.End()
```

### C#

```csharp
System.bool End()
```

### C++/CLI

```cpp
System.bool End();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the progress indicator is removed, false if not

## VBA Syntax

See [UserProgressBar::End](ms-its:sldworksapivb6.chm::/sldworks~UserProgressBar~End.html).

## Examples

See the [IUserProgressBar](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserProgressBar.html) examples.

## Remarks

This method does not immediately remove the progress bar from the status bar. Instead, a show-window event is posted to the message queue of the given window when this method is called. After Windows processes the message, the progress bar is removed
from the status bar.

## See Also

[IUserProgressBar Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserProgressBar.html)
[IUserProgressBar Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserProgressBar_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
