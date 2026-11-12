---
title: "UpdateTitle Method (IUserProgressBar)"
project: "SOLIDWORKS API Help"
interface: "IUserProgressBar"
member: "UpdateTitle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserProgressBar~UpdateTitle.html"
---

# UpdateTitle Method (IUserProgressBar)

Changes the title of the progress indicator.

## Syntax

### Visual Basic (Declaration)

```vb
Function UpdateTitle( _
   ByVal ProgressBarTitle As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IUserProgressBar
Dim ProgressBarTitle As System.String
Dim value As System.Boolean

value = instance.UpdateTitle(ProgressBarTitle)
```

### C#

```csharp
System.bool UpdateTitle(
   System.string ProgressBarTitle
)
```

### C++/CLI

```cpp
System.bool UpdateTitle(
   System.String^ ProgressBarTitle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ProgressBarTitle`: New title of progress indicator

### Return Value

True if title successfully updated, false if not

## VBA Syntax

See [UserProgressBar::UpdateTitle](ms-its:sldworksapivb6.chm::/sldworks~UserProgressBar~UpdateTitle.html).

## Examples

See the [IUserProgressBar](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserProgressBar.html) examples.

## See Also

[IUserProgressBar Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserProgressBar.html)
[IUserProgressBar Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserProgressBar_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
