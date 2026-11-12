---
title: "OnSelectionboxListChanged Method (IPropertyManagerPage2Handler5)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler5"
member: "OnSelectionboxListChanged"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler5~OnSelectionboxListChanged.html"
---

# OnSelectionboxListChanged Method (IPropertyManagerPage2Handler5)

Obsoleted. Superseded by [IPropertyManagerPage2Handler6::OnSelectionboxListChanged](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler6~OnSelectionboxListChanged.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnSelectionboxListChanged( _
   ByVal Id As System.Integer, _
   ByVal Count As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler5
Dim Id As System.Integer
Dim Count As System.Integer

instance.OnSelectionboxListChanged(Id, Count)
```

### C#

```csharp
void OnSelectionboxListChanged(
   System.int Id,
   System.int Count
)
```

### C++/CLI

```cpp
void OnSelectionboxListChanged(
   System.int Id,
   System.int Count
)
```

### Parameters

- `Id`: ID of this selection box
- `Count`: Number of items in this selection box

## VBA Syntax

See [PropertyManagerPage2Handler5::OnSelectionboxListChanged](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler5~OnSelectionboxListChanged.html).

## Remarks

This method is called when your application uses a selection method, such as [IModelDocExtension::SelectByID2](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html), just as if the selection was made interactively.

The method is called during the process of SOLIDWORKS selection. It is neither a pre-notification nor a post-notification. The add-in should not be taking any action that may affect the model or the selection list. The add-in should only be querying information, presumably about the state of selections to set up its own information correctly.

Regardless of how many items the user selects, this method is called only once per interactive box selection. In other words, if the user selects six faces using a box selection, this method is called only once.

## See Also

[IPropertyManagerPage2Handler5 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler5.html)
[IPropertyManagerPage2Handler5 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler5_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
