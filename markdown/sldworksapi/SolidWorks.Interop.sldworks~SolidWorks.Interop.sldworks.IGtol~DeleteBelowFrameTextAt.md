---
title: "DeleteBelowFrameTextAt Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "DeleteBelowFrameTextAt"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~DeleteBelowFrameTextAt.html"
---

# DeleteBelowFrameTextAt Method (IGtol)

Deletes the specified text line in the below frame of this GTol.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteBelowFrameTextAt( _
   ByVal Index As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim Index As System.Integer
Dim value As System.Boolean

value = instance.DeleteBelowFrameTextAt(Index)
```

### C#

```csharp
System.bool DeleteBelowFrameTextAt(
   System.int Index
)
```

### C++/CLI

```cpp
System.bool DeleteBelowFrameTextAt(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 1-based index of the below frame text line to delete; -1 to delete all of the below frame text lines

### Return Value

True if text line successfully deleted, false if not

## VBA Syntax

See [Gtol::DeleteBelowFrameTextAt](ms-its:sldworksapivb6.chm::/sldworks~Gtol~DeleteBelowFrameTextAt.html).

## Examples

See **Set Text in Datum Tags and GTols** examples in [IGTol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html).

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::GetBelowFrameTextAt Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetBelowFrameTextAt.html)
[IGtol::GetBelowFrameTextLineCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetBelowFrameTextLineCount.html)
[IGtol::InsertBelowFrameTextAt Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~InsertBelowFrameTextAt.html)
[IGtol::SetBelowFrameTextAt Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetBelowFrameTextAt.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
