---
title: "OnSubmitSelection Method (IPropertyManagerPage2Handler8)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler8"
member: "OnSubmitSelection"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8~OnSubmitSelection.html"
---

# OnSubmitSelection Method (IPropertyManagerPage2Handler8)

Obsolete. Superseded by[IPropertyManagerPage2Handler9::OnSubmitSelection](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler9~OnSubmitSelection.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function OnSubmitSelection( _
   ByVal Id As System.Integer, _
   ByVal Selection As System.Object, _
   ByVal SelType As System.Integer, _
   ByRef ItemText As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler8
Dim Id As System.Integer
Dim Selection As System.Object
Dim SelType As System.Integer
Dim ItemText As System.String
Dim value As System.Boolean

value = instance.OnSubmitSelection(Id, Selection, SelType, ItemText)
```

### C#

```csharp
System.bool OnSubmitSelection(
   System.int Id,
   System.object Selection,
   System.int SelType,
   out System.string ItemText
)
```

### C++/CLI

```cpp
System.bool OnSubmitSelection(
   System.int Id,
   System.Object^ Selection,
   System.int SelType,
   [Out] System.String^ ItemText
)
```

### Parameters

- `Id`: ID of the active selection box, where this selection is being made
- `Selection`: Object being selected
- `SelType`: Entity type of the selection as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)
- `ItemText`: Item for selection list box (see **Remarks**)

### Return Value

True if the selection is accepted, false if the selection is rejected

## VBA Syntax

See [PropertyManagerPage2Handler8::OnSubmitSelection](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler8~OnSubmitSelection.html).

## Remarks

If writing a macro, you must set this method to true for the user to select something (see the example). If this method is not set to true, then the user cannot select anything. This method is set to false by default.

This method is called by SOLIDWORKS when an add-in has a PropertyManager page displayed and a selection is made that passes the selection filter criteria set up for a selection list box. The add-in can then:

1. Take the Dispatch pointer and the selection type.
2. QueryInterface the Dispatch pointer to get the specific interface.
3. Use APIs of that interface to determine if the selection should be allowed or not.

The add-in should not Release() the Dispatch pointer. SOLIDWORKS will Release() the Dispatch pointer upon return from this method.

The method is called during the process of SOLIDWORKS selection. It is neither a pre-notification nor post-notification. The add-in should not be taking any action that might affect the model or the selection list. The add-in should only be querying information and then returning true/VARIANT_TRUE or false/VARIANT_FALSE.

ItemText is returned to SOLIDWORKS and stored on the selected object and can be used by your PropertyManager page selection list boxes for the life of that selection.

## See Also

[IPropertyManagerPage2Handler8 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8.html)
[IPropertyManagerPage2Handler8 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
