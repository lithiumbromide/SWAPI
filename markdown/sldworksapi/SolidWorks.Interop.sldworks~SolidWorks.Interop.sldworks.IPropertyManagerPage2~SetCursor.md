---
title: "SetCursor Method (IPropertyManagerPage2)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPage2"
member: "SetCursor"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~SetCursor.html"
---

# SetCursor Method (IPropertyManagerPage2)

Sets the cursor after a selection is made in the SOLIDWORKS graphics area.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetCursor( _
   ByVal Mode As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2
Dim Mode As System.Integer

instance.SetCursor(Mode)
```

### C#

```csharp
void SetCursor(
   System.int Mode
)
```

### C++/CLI

```cpp
void SetCursor(
   System.int Mode
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Mode`: Cursor as defined by [swPropertyManagerPageCursors_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertyManagerPageCursors_e.html)

## VBA Syntax

See [PropertyManagerPage2::SetCursor](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPage2~SetCursor.html).

## Examples

See the [IPropertyManagerPage2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.html) examples.

## Remarks

Calling this method in [IPropertyManagerPage2Hander8::OnSelectionboxListChanged](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler8~OnSelectionboxListChanged.html) enables the right-mouse button and cursor and allows an interactive user to:

- move to the next selection box on the PropertyManager page
- okay and close a PropertyManager page

after making a selection in the SOLIDWORKS graphics area.

## See Also

[IPropertyManagerPage2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.html)
[IPropertyManagerPage2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
