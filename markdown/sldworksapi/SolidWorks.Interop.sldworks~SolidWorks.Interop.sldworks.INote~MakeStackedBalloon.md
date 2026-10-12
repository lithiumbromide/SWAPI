---
title: "MakeStackedBalloon Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "MakeStackedBalloon"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~MakeStackedBalloon.html"
---

# MakeStackedBalloon Method (INote)

Converts this balloon to a stacked balloon.

## Syntax

### Visual Basic (Declaration)

```vb
Sub MakeStackedBalloon( _
   ByVal StackedBalloonOptions As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim StackedBalloonOptions As System.Object

instance.MakeStackedBalloon(StackedBalloonOptions)
```

### C#

```csharp
void MakeStackedBalloon(
   System.object StackedBalloonOptions
)
```

### C++/CLI

```cpp
void MakeStackedBalloon(
   System.Object^ StackedBalloonOptions
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StackedBalloonOptions`: [IStackedBalloonOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions.html)

## VBA Syntax

See [Note::MakeStackedBalloon](ms-its:sldworksapivb6.chm::/sldworks~Note~MakeStackedBalloon.html).

## Remarks

Before calling this method, use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) to select the entity to add to the balloon stack.

After calling this method to convert the balloon to a stacked balloon, add more balloons by calling:

1. [INote::GetBalloonStack](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonStack.html)
2. [IBalloonStack::AddTo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack~AddTo.html)

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[IModelDocExtension::InsertStackedBalloon2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertStackedBalloon2.html)
[INote::GetBalloonOptions Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonOptions.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
