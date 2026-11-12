---
title: "UpdateProgress Method (IUserProgressBar)"
project: "SOLIDWORKS API Help"
interface: "IUserProgressBar"
member: "UpdateProgress"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserProgressBar~UpdateProgress.html"
---

# UpdateProgress Method (IUserProgressBar)

Increments the progress indicator.

## Syntax

### Visual Basic (Declaration)

```vb
Function UpdateProgress( _
   ByVal Position As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IUserProgressBar
Dim Position As System.Integer
Dim value As System.Integer

value = instance.UpdateProgress(Position)
```

### C#

```csharp
System.int UpdateProgress(
   System.int Position
)
```

### C++/CLI

```cpp
System.int UpdateProgress(
   System.int Position
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Position`: New position of the progress indicator

### Return Value

Status of progress indicator update as defined in [swUpdateProgressError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUpdateProgressError_e.html)

## VBA Syntax

See [UserProgressBar::UpdateProgress](ms-its:sldworksapivb6.chm::/sldworks~UserProgressBar~UpdateProgress.html).

## Examples

See the [IUserProgressBar](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserProgressBar.html) examples.

## See Also

[IUserProgressBar Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserProgressBar.html)
[IUserProgressBar Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserProgressBar_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
