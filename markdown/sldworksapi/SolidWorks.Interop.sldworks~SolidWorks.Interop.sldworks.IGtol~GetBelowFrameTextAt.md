---
title: "GetBelowFrameTextAt Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "GetBelowFrameTextAt"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetBelowFrameTextAt.html"
---

# GetBelowFrameTextAt Method (IGtol)

Gets the specified line of text in this GTol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBelowFrameTextAt( _
   ByVal Index As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim Index As System.Integer
Dim value As System.String

value = instance.GetBelowFrameTextAt(Index)
```

### C#

```csharp
System.string GetBelowFrameTextAt(
   System.int Index
)
```

### C++/CLI

```cpp
System.String^ GetBelowFrameTextAt(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 1-based index of the line whose text to get

### Return Value

Below frame line of text

## VBA Syntax

See [Gtol::GetBelowFrameTextAt](ms-its:sldworksapivb6.chm::/sldworks~Gtol~GetBelowFrameTextAt.html).

## Examples

See **Set Text in Datum Tags and GTols** examples in [IGTol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html).

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::DeleteBelowFrameTextAt Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~DeleteBelowFrameTextAt.html)
[IGtol::GetBelowFrameTextLineCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetBelowFrameTextLineCount.html)
[IGtol::InsertBelowFrameTextAt Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~InsertBelowFrameTextAt.html)
[IGtol::SetBelowFrameTextAt Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetBelowFrameTextAt.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
