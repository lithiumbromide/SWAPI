---
title: "UpdateStamp Property (IPDMWDocument)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocument"
member: "UpdateStamp"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~UpdateStamp.html"
---

# UpdateStamp Property (IPDMWDocument)

Gets the date on which this document was last updated.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property UpdateStamp As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocument
Dim value As System.Integer

value = instance.UpdateStamp
```

### C#

```csharp
System.int UpdateStamp {get;}
```

### C++/CLI

```cpp
property System.int UpdateStamp {
   System.int get();
}
```

### Property Value

Date document last updated

## VBA Syntax

See [PDMWDocument::UpdateStamp](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocument~UpdateStamp.html).

## Remarks

The update stamp is an integer representing the time stamp. The update stamp in a SOLIDWORKS document is incremented when:

- the state of the model changes (for example, you suppress or unsuppress a feature in a part or an assembly)
- the geometry changes (for example, any action that requires a rebuild)

This time stamp is not incremented for such operations as color changes, feature or configuration name changes, and so on.

This property returns 0 for non-SOLIDWORKS documents.

## See Also

[IPDMWDocument Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html)
[IPDMWDocument Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument_members.html)
[IPDMWDocument::DateModified Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~DateModified.html)

## Availability

SOLIDWORKS Workgroup PDM 2004 FCS
