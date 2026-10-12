---
title: "ParentPath Property (IPDMWSearchResult)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWSearchResult"
member: "ParentPath"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchResult~ParentPath.html"
---

# ParentPath Property (IPDMWSearchResult)

Gets the full path of the parent project and any subprojects of a document in a [search result](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchResult.html).

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ParentPath As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWSearchResult
Dim value As System.String

value = instance.ParentPath
```

### C#

```csharp
System.string ParentPath {get;}
```

### C++/CLI

```cpp
property System.String^ ParentPath {
   System.String^ get();
}
```

### Property Value

Path to parent project and any subprojects

## VBA Syntax

See [PDMWSearchResult::ParentPath](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWSearchResult~ParentPath.html).

## Remarks

For example:

If the path is:

```vb
Sample Project ->
       Second Level SubProject ->
               Third Level SubSubProject ->
                       Document.sldprt
```

Then this property returns:

```vb
Sample Project/Second Level SubProject/Third Level SubSubProject
```

## See Also

[IPDMWSearchResult Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchResult.html)
[IPDMWSearchResult Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchResult_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2006 FCS
