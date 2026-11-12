---
title: "Start Method (IUserProgressBar)"
project: "SOLIDWORKS API Help"
interface: "IUserProgressBar"
member: "Start"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserProgressBar~Start.html"
---

# Start Method (IUserProgressBar)

Sets the range of the progress indicator display and shows it on the SOLIDWORKS status bar.

## Syntax

### Visual Basic (Declaration)

```vb
Function Start( _
   ByVal LowerBound As System.Integer, _
   ByVal UpperBound As System.Integer, _
   ByVal ProgressBarTitle As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IUserProgressBar
Dim LowerBound As System.Integer
Dim UpperBound As System.Integer
Dim ProgressBarTitle As System.String
Dim value As System.Boolean

value = instance.Start(LowerBound, UpperBound, ProgressBarTitle)
```

### C#

```csharp
System.bool Start(
   System.int LowerBound,
   System.int UpperBound,
   System.string ProgressBarTitle
)
```

### C++/CLI

```cpp
System.bool Start(
   System.int LowerBound,
   System.int UpperBound,
   System.String^ ProgressBarTitle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `LowerBound`: Lower bound of range
- `UpperBound`: Upper bound of range
- `ProgressBarTitle`: Title of progress indicator to show in status bar

### Return Value

True if progress indicator successfully started, false if not

## VBA Syntax

See [UserProgressBar::Start](ms-its:sldworksapivb6.chm::/sldworks~UserProgressBar~Start.html).

## Examples

See the [IUserProgressBar](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserProgressBar.html) examples.

## See Also

[IUserProgressBar Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserProgressBar.html)
[IUserProgressBar Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserProgressBar_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
