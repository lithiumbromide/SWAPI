---
title: "EditTemplate Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "EditTemplate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditTemplate.html"
---

# EditTemplate Method (IDrawingDoc)

Puts the template of the current drawing sheet in edit mode.

## Syntax

### Visual Basic (Declaration)

```vb
Sub EditTemplate()
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc

instance.EditTemplate()
```

### C#

```csharp
void EditTemplate()
```

### C++/CLI

```cpp
void EditTemplate();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [DrawingDoc::EditTemplate](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~EditTemplate.html).

## Examples

[Place Note Behind Drawing Sheet (C#)](Place_Note_Behind_Drawing_Sheet_Example_CSharp.htm)
[Place Note Behind Drawing Sheet (VB.NET)](Place_Note_Behind_Drawing_Sheet_Example_VBNET.htm)
[Place Note Behind Drawing Sheet (VBA)](Place_Note_Behind_Drawing_Sheet_Example_VB.htm)

## Remarks

Creating subsequent geometry resides on the drawing template.

You can use this method with [IDrawingDoc::EditSheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~EditSheet.html) or [IDrawingDoc::EditSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~EditSketch.html). Use [IDrawingDoc::GetEditSheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~GetEditSheet.html) to determine the current state.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[ISheet::ReloadTemplate Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~ReloadTemplate.html)
[ISheet::SaveFormat Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SaveFormat.html)
