---
title: "GetBalloonStyle Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "GetBalloonStyle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonStyle.html"
---

# GetBalloonStyle Method (INote)

Gets the balloon style of this note.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBalloonStyle() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim value As System.Integer

value = instance.GetBalloonStyle()
```

### C#

```csharp
System.int GetBalloonStyle()
```

### C++/CLI

```cpp
System.int GetBalloonStyle();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Balloon style as defined in [swBalloonStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonStyle_e.html)

## VBA Syntax

See [Note::GetBalloonStyle](ms-its:sldworksapivb6.chm::/sldworks~Note~GetBalloonStyle.html).

## Examples

[Get BOM Balloon Properties (VBA)](Get_BOM_Balloon_Properties_Example_VB.htm)

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::GetBalloonInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonInfo.html)
[INote::GetBalloonSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonSize.html)
[INote::GetBalloonStack Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonStack.html)
[INote::GetBomBalloonText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBomBalloonText.html)
[INote::GetBomBalloonTextStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBomBalloonTextStyle.html)
[INote::HasBalloon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~HasBalloon.html)
[INote::IGetBalloonInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetBalloonInfo.html)
[INote::IsBomBalloon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsBomBalloon.html)
[INote::IsStackedBalloon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsStackedBalloon.html)
[INote::IsStackedBalloonMaster Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsStackedBalloonMaster.html)
[INote::SetBalloon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetBalloon.html)
[INote::SetBomBalloonText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetBomBalloonText.html)
[INote::GetBalloonOptions Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonOptions.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
