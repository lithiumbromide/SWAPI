---
title: "IsBomBalloon Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "IsBomBalloon"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsBomBalloon.html"
---

# IsBomBalloon Method (INote)

Gets whether this note has a BOM balloon.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsBomBalloon() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim value As System.Boolean

value = instance.IsBomBalloon()
```

### C#

```csharp
System.bool IsBomBalloon()
```

### C++/CLI

```cpp
System.bool IsBomBalloon();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the note has a BOM balloon, false if not

## VBA Syntax

See [Note::IsBomBalloon](ms-its:sldworksapivb6.chm::/sldworks~Note~IsBomBalloon.html).

## Examples

[Get BOM Balloon Properties (VBA)](Get_BOM_Balloon_Properties_Example_VB.htm)
[Set BOM Balloon Text (VBA)](Set_BOM_Balloon_Example_VB.htm)
[Insert and Show BOM Table and BOM Balloon (C#)](Insert_and_Show_BOM_Table_and_BOM_Balloon_Example_CSharp.htm)
[Insert and Show BOM Table and BOM Balloon (VB.NET)](Insert_and_Show_BOM_Table_and_BOM_Balloon_Example_VBNET.htm)
[Insert and Show BOM Table and BOM Balloon (VBA)](Insert_and_Show_BOM_Table_and_BOM_Balloon_Example_VB.htm)

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::GetBalloonInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonInfo.html)
[INote::GetBalloonSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonSize.html)
[INote::GetBalloonStack Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonStack.html)
[INote::GetBalloonStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonStyle.html)
[INote::GetBomBalloonText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBomBalloonText.html)
[INote::GetBomBalloonTextStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBomBalloonTextStyle.html)
[INote::HasBalloon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~HasBalloon.html)
[INote::IGetBalloonInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetBalloonInfo.html)
[INote::IsStackedBalloon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsStackedBalloon.html)
[INote::IsStackedBalloonMaster Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsStackedBalloonMaster.html)
[INote::SetBalloon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetBalloon.html)
[INote::SetBomBalloonText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetBomBalloonText.html)
[IModelDocExtension::InsertBOMBalloon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertBOMBalloon.html)
[INote::vGetBalloonOptions Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonOptions.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
