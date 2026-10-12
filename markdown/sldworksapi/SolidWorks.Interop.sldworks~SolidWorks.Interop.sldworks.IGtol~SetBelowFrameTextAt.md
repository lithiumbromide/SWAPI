---
title: "SetBelowFrameTextAt Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "SetBelowFrameTextAt"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetBelowFrameTextAt.html"
---

# SetBelowFrameTextAt Method (IGtol)

Edits or inserts a text line at the specified below frame line index of this GTol.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetBelowFrameTextAt( _
   ByVal Index As System.Integer, _
   ByVal Text As System.String, _
   ByVal Overwrite As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim Index As System.Integer
Dim Text As System.String
Dim Overwrite As System.Boolean
Dim value As System.Boolean

value = instance.SetBelowFrameTextAt(Index, Text, Overwrite)
```

### C#

```csharp
System.bool SetBelowFrameTextAt(
   System.int Index,
   System.string Text,
   System.bool Overwrite
)
```

### C++/CLI

```cpp
System.bool SetBelowFrameTextAt(
   System.int Index,
   System.String^ Text,
   System.bool Overwrite
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 1-based line index at which to edit or insert text
- `Text`: New text
- `Overwrite`: True to overwrite the text at Index; false to insert a new line at Index

### Return Value

True if the text is successfully edited or inserted, false if not

## VBA Syntax

See [Gtol::SetBelowFrameTextAt](ms-its:sldworksapivb6.chm::/sldworks~Gtol~SetBelowFrameTextAt.html).

## Examples

See **Set Text in Datum Tags and GTols** examples in [IGTol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html).

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::DeleteBelowFrameTextAt Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~DeleteBelowFrameTextAt.html)
[IGtol::GetBelowFrameTextAt Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetBelowFrameTextAt.html)
[IGtol::GetBelowFrameTextLineCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetBelowFrameTextLineCount.html)
[IGtol::InsertBelowFrameTextAt Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~InsertBelowFrameTextAt.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
