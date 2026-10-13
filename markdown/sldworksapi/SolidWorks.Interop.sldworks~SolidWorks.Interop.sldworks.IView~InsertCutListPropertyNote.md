---
title: "InsertCutListPropertyNote Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "InsertCutListPropertyNote"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertCutListPropertyNote.html"
---

# InsertCutListPropertyNote Method (IView)

Inserts a note that contains all of the cut list item properties of a sheet metal part.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertCutListPropertyNote( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double

instance.InsertCutListPropertyNote(X, Y, Z)
```

### C#

```csharp
void InsertCutListPropertyNote(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
void InsertCutListPropertyNote(
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: x coordinate of the note
- `Y`: y coordinate of the note
- `Z`: z coordinate of the note

## VBA Syntax

See [View::InsertCutListPropertyNote](ms-its:sldworksapivb6.chm::/sldworks~View~InsertCutListPropertyNote.html).

## Examples

[Insert Cut List Item Property Note (VBA)](Insert_Cut_List_Item_Property_Note_Example_VB.htm)
[Insert Cut List Item Property Note (VB.NET)](Insert_Cut_List_Item_Property_Note_Example_VBNET.htm)
[Insert Cut List Item Property Note (C#)](Insert_Cut_List_Item_Property_Note_Example_CSharp.htm)

## Remarks

This method requires a flat pattern drawing view.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
