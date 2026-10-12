---
title: "Number Property (IPDMWDocument)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocument"
member: "Number"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~Number.html"
---

# Number Property (IPDMWDocument)

Gets the number of this document.

## Syntax

### Visual Basic (Declaration)

```vb
Property Number As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocument
Dim value As System.String

instance.Number = value

value = instance.Number
```

### C#

```csharp
System.string Number {get; set;}
```

### C++/CLI

```cpp
property System.String^ Number {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Number of document

## VBA Syntax

See [PDMWDocument::Number](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocument~Number.html).

## Remarks

You can change the document's number property by accessing the document's custom property; for example, [IPDMWDocument::Properties](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~Properties.html)("Number").

## See Also

[IPDMWDocument Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html)
[IPDMWDocument Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
