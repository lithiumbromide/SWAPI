---
title: "GetBalloonStack Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "GetBalloonStack"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonStack.html"
---

# GetBalloonStack Method (INote)

Gets the balloon stack for this balloon note.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBalloonStack() As BalloonStack
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim value As BalloonStack

value = instance.GetBalloonStack()
```

### C#

```csharp
BalloonStack GetBalloonStack()
```

### C++/CLI

```cpp
BalloonStack^ GetBalloonStack();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Balloon stack](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBalloonStack.html) for this balloon note

## VBA Syntax

See [Note::GetBalloonStack](ms-its:sldworksapivb6.chm::/sldworks~Note~GetBalloonStack.html).

## Examples

[Add Balloon to Stacked Balloon (C#)](Add_Balloon_to_Stacked_Balloon_Example_CSharp.htm)
[Add Balloon to Stacked Balloon (VB.NET)](Add_Balloon_to_Stacked_Balloon_Example_VBNET.htm)
[Add Balloon to Stacked Balloon (VBA)](Add_Balloon_to_Stacked_Balloon_Example_VB.htm)

## Remarks

If this note is not part of a balloon stack, then this method returns null or nothing. To determine if a note is part of a balloon stack, use [INote::IsStackedBalloon](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~IsStackedBalloon.html).

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::GetBalloonInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonInfo.html)
[INote::GetBalloonSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonSize.html)
[INote::GetBalloonStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonStyle.html)
[INote::GetBomBalloonText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBomBalloonText.html)
[INote::GetBomBalloonTextStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBomBalloonTextStyle.html)
[INote::HasBalloon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~HasBalloon.html)
[INote::IGetBalloonInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetBalloonInfo.html)
[INote::IsBomBalloon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsBomBalloon.html)
[INote::IsStackedBalloon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsStackedBalloon.html)
[INote::SetBalloon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetBalloon.html)
[INote::SetBomBalloonText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetBomBalloonText.html)
[INote::MakeStackedBalloon Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~MakeStackedBalloon.html)
[INote::GetBalloonOptions Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonOptions.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
