---
title: "INote Interface"
project: "SOLIDWORKS API Help"
interface: "INote"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html"
---

# INote Interface

Allows you to get standard note information.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface INote
```

### Visual Basic (Usage)

```vb
Dim instance As INote
```

### C#

```csharp
public interface INote
```

### C++/CLI

```cpp
public interface class INote
```

## VBA Syntax

See [Note](ms-its:sldworksapivb6.chm::/sldworks~Note.html).

## Examples

[Get Notes from New or Existing Title Block (C#)](Get_Notes_from_New_or_Existing_Title_Block_Example_CSharp.htm)
[Get Notes from New or Existing Title Block (VB.NET)](Get_Notes_from_New_or_Existing_Title_Block_Example_VBNET.htm)
[Get Notes from New or Existing Title Block (VBA)](Get_Notes_from_New_or_Existing_Title_Block_Example_VB.htm)
[Anchor a Note (VBA)](Anchor_a_Note_Example_VB.htm)
[Anchor a Note (VB.NET)](Anchor_a_Note_Example_VBNET.htm)
[Anchor a Note (C#)](Anchor_a_Note_Example_CSharp.htm)

## Remarks

**Important**: [Compound notes](ms-its:sldworksapiprogguide.chm::/Overview/Compound_Note.htm) are no longer creatable through the SOLIDWORKS Design user interface. As such, they are a legacy annotation type. SOLIDWORKS APIs that work on compound notes should only be used with legacy SOLIDWORKS files. [ISketchBlockDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.html) and [ISketchBlockInstance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.html) can be used to mimic the functionality of compound notes. See [Block Definitions and Block Instances](ms-its:sldworksapiprogguide.chm::/Overview/Block_Definitions_and_Block_Instances.htm).

## Accessors

[IAnnotation::GetSpecificAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetSpecificAnnotation.html) and [IAnnotation::IGetSpecificAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~IGetSpecificAnnotation.html)

[IBalloonStack::AddTo](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBalloonStack~AddTo.html)

[IBalloonStack::IGetStack](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBalloonStack~IGetStack.html)

[IBalloonStack::Master](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBalloonStack~Master.html)

[IBalloonStack::Stack](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBalloonStack~Stack.html)

[ICThread::ThreadCallout](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICThread~ThreadCallout.html)

[IDrawingDoc::AutoBalloon5](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~AutoBalloon5.html)

[IDrawingDoc::CreateText2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~CreateText2.html) and [IDrawingDoc::ICreateText2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~ICreateText2.html)

[IDrawingDoc::InsertRevisionSymbol](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~InsertRevisionSymbol.html)

[IFeatureManager::InsertSecurityNote](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertSecurityNote.html)

[IModelDoc2::InsertNote](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertNote.html) and [IModelDoc2::IInsertNote](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IInsertNote.html)

[IModelDocExtension::EditBalloonProperties2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~EditBalloonProperties2.html)

[IModelDocExtension::InsertBomBalloon2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~InsertBOMBalloon2.html)

[IModelDocExtension::InsertStackedBalloon2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~InsertStackedBalloon2.html)

[INote::GetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~GetNext.html) and [INote::IGetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~IGetNext.html)

[IPartDoc::InsertBendNotes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~InsertBendNotes.html)

[IRevisionTableAnnotation::GetRevisionSymbols](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionTableAnnotation~GetRevisionSymbols.html) and [RevisionTableAnnotation::IGetRevisionSymbols](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionTableAnnotation~IGetRevisionSymbols.html)

[ISketchBlockDefinition::GetNotes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~GetNotes.html) and [ISketchBlockDefinition::IGetNotes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~IGetNotes.html)

[ISketchBlockInstance::GetAttributes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockInstance~GetAttributes.html) and [ISketchBlockInstance::IGetAttributes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockInstance~IGetAttributes.html)

[IView::GetFirstNote](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFirstNote.html) and [IView::IGetFirstNote](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetFirstNote.html)

[IView::GetNotes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetNotes.html)

## Access Diagram

[Note](SWObjectModel.pdf#Note)

## See Also

[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IModelDoc2::InsertNewNote3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertNewNote3.html)
[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
