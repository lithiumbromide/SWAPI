---
title: "SetSheetsSelected Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "SetSheetsSelected"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetSheetsSelected.html"
---

# SetSheetsSelected Method (IDrawingDoc)

Sets the specified drawing sheets whose setups to modify.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetSheetsSelected( _
   ByVal NewSheetList As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim NewSheetList As System.Object

instance.SetSheetsSelected(NewSheetList)
```

### C#

```csharp
void SetSheetsSelected(
   System.object NewSheetList
)
```

### C++/CLI

```cpp
void SetSheetsSelected(
   System.Object^ NewSheetList
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NewSheetList`: Names of the drawing sheets whose setups to modify (see **Remarks**)

## VBA Syntax

See [DrawingDoc::SetSheetsSelected](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~SetSheetsSelected.html).

## Examples

[Modify Multiple Drawing Sheets Setups (C#)](Modify_Multiple_Drawing_Sheets_Setups_Example_CSharp.htm)
[Modify Multiple Drawing Sheets Setups (VB.NET)](Modify_Multiple_Drawing_Sheets_Setups_Example_VBNET.htm)
[Modify Multiple Drawing Sheets Setups (VBA)](Modify_Multiple_Drawing_Sheets_Setups_Example_VB.htm)

## Remarks

The first drawing sheet in the drawing is automatically included in NewSheetList and need not be specified.

After calling this method, call [IDrawingDoc::SetupSheet6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetupSheet6.html) to specify how to modify the setups of the specified drawing sheets.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
