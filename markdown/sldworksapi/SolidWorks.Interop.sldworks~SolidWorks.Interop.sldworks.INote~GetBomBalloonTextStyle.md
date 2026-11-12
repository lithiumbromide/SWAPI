---
title: "GetBomBalloonTextStyle Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "GetBomBalloonTextStyle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBomBalloonTextStyle.html"
---

# GetBomBalloonTextStyle Method (INote)

Gets the text style of this BOM balloon note.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBomBalloonTextStyle( _
   ByVal WhichOne As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim WhichOne As System.Boolean
Dim value As System.Integer

value = instance.GetBomBalloonTextStyle(WhichOne)
```

### C#

```csharp
System.int GetBomBalloonTextStyle(
   System.bool WhichOne
)
```

### C++/CLI

```cpp
System.int GetBomBalloonTextStyle(
   System.bool WhichOne
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WhichOne`: True for the upper text, false for the lower text

### Return Value

Balloon text style as defined in [swDetailingNoteTextContent_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDetailingNoteTextContent_e.html)

## VBA Syntax

See [Note::GetBomBalloonTextStyle](ms-its:sldworksapivb6.chm::/sldworks~Note~GetBomBalloonTextStyle.html).

## Examples

[Set BOM Balloon Text (VBA)](Set_BOM_Balloon_Example_VB.htm)
[Get BOM Balloon Properties (C#)](Get_BOM_Balloon_Properties_Example_CSharp.htm)
[Get BOM Balloon Properties (VB.NET)](Get_BOM_Balloon_Properties_Example_VBNET.htm)
[Get BOM Balloon Properties (VBA)](Get_BOM_Balloon_Properties_Example_VB.htm)

## Remarks

SOLIDWORKS 2001 FCS, Revision Number 9.0

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::GetBalloonInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonInfo.html)
[INote::GetBalloonSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonSize.html)
[INote::GetBalloonStack Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonStack.html)
[INote::GetBalloonStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonStyle.html)
[INote::GetBomBalloonText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBomBalloonText.html)
[INote::HasBalloon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~HasBalloon.html)
[INote::IGetBalloonInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetBalloonInfo.html)
[INote::IsBomBalloon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsBomBalloon.html)
[INote::IsStackedBalloon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsStackedBalloon.html)
[INote::IsStackedBalloonMaster Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsStackedBalloonMaster.html)
[INote::SetBalloon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetBalloon.html)
[INote::SetBomBalloonText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetBomBalloonText.html)
[IModelDocExtension::InsertBOMBalloon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertBOMBalloon.html)
[INote::GetBalloonOptions Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonOptions.html)
