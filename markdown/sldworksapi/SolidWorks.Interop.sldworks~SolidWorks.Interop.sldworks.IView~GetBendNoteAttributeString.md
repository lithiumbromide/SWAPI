---
title: "GetBendNoteAttributeString Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetBendNoteAttributeString"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBendNoteAttributeString.html"
---

# GetBendNoteAttributeString Method (IView)

Gets the internal string that is used to format the text of the specified bend note attribute in this drawing view of a sheet metal part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBendNoteAttributeString( _
   ByVal Attribute As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim Attribute As System.Integer
Dim value As System.String

value = instance.GetBendNoteAttributeString(Attribute)
```

### C#

```csharp
System.string GetBendNoteAttributeString(
   System.int Attribute
)
```

### C++/CLI

```cpp
System.String^ GetBendNoteAttributeString(
   System.int Attribute
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Attribute`: Bend note attribute as defined in [swBendNoteAttribute_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBendNoteAttribute_e.html)

### Return Value

String that is used to format the bend note attribute

## VBA Syntax

See [View::GetBendNoteAttributeString](ms-its:sldworksapivb6.chm::/sldworks~View~GetBendNoteAttributeString.html).

## Remarks

Call this method to specify the Format parameter of [IView::SetBendNoteTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~SetBendNoteTextFormat.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetBendNoteTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBendNoteTextFormat.html)
[IView::ShowSheetMetalBendNotes Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ShowSheetMetalBendNotes.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
