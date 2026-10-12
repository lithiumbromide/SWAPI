---
title: "InsertBelowFrameTextAt Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "InsertBelowFrameTextAt"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~InsertBelowFrameTextAt.html"
---

# InsertBelowFrameTextAt Method (IGtol)

Inserts the specified text at the specified line index in the below frame of this GTol.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertBelowFrameTextAt( _
   ByVal Index As System.Integer, _
   ByVal Text As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim Index As System.Integer
Dim Text As System.String
Dim value As System.Boolean

value = instance.InsertBelowFrameTextAt(Index, Text)
```

### C#

```csharp
System.bool InsertBelowFrameTextAt(
   System.int Index,
   System.string Text
)
```

### C++/CLI

```cpp
System.bool InsertBelowFrameTextAt(
   System.int Index,
   System.String^ Text
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 1-based index where to insert the line of Text in the below frame
- `Text`: Text to insert

### Return Value

True if text line successfully inserted, false if not

## VBA Syntax

See [Gtol::InsertBelowFrameTextAt](ms-its:sldworksapivb6.chm::/sldworks~Gtol~InsertBelowFrameTextAt.html).

## Examples

See **Set Text in Datum Tags and GTols** examples in [IGTol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html).

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::DeleteBelowFrameTextAt Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~DeleteBelowFrameTextAt.html)
[IGtol::GetBelowFrameTextAt Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetBelowFrameTextAt.html)
[IGtol::GetBelowFrameTextLineCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetBelowFrameTextLineCount.html)
[IGtol::SetBelowFrameTextAt Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetBelowFrameTextAt.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
