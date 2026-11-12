---
title: "GetBelowFrameTextLineCount Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "GetBelowFrameTextLineCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetBelowFrameTextLineCount.html"
---

# GetBelowFrameTextLineCount Method (IGtol)

Gets the number of text lines in the below frame of this GTol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBelowFrameTextLineCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim value As System.Integer

value = instance.GetBelowFrameTextLineCount()
```

### C#

```csharp
System.int GetBelowFrameTextLineCount()
```

### C++/CLI

```cpp
System.int GetBelowFrameTextLineCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of text lines in the below frame

## VBA Syntax

See [Gtol::GetBelowFrameTextLineCount](ms-its:sldworksapivb6.chm::/sldworks~Gtol~GetBelowFrameTextLineCount.html).

## Examples

See **Set Text in Datum Tags and GTols** examples in [IGTol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html).

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::DeleteBelowFrameTextAt Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~DeleteBelowFrameTextAt.html)
[IGtol::GetBelowFrameTextAt Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetBelowFrameTextAt.html)
[IGtol::InsertBelowFrameTextAt Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~InsertBelowFrameTextAt.html)
[IGtol::SetBelowFrameTextAt Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetBelowFrameTextAt.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
