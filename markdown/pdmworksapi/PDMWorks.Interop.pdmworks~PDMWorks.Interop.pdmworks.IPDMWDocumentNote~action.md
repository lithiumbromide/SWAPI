---
title: "action Property (IPDMWDocumentNote)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocumentNote"
member: "action"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocumentNote~action.html"
---

# action Property (IPDMWDocumentNote)

Gets the description of the SOLIDWORKS Workgroup PDM event that occurred.

## Syntax

### Visual Basic (Declaration)

```vb
Property action As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocumentNote
Dim value As System.String

instance.action = value

value = instance.action
```

### C#

```csharp
System.string action {get; set;}
```

### C++/CLI

```cpp
property System.String^ action {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Event that occurred

## VBA Syntax

See [PDMWDocumentNote::action](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocumentNote~action.html).

## Remarks

The return value can contain:

- "Check In"
- "Check Out"
- "Take Ownership"
- "Release Ownership"
- "Change Project"

## See Also

[IPDMWDocumentNote Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocumentNote.html)
[IPDMWDocumentNote Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocumentNote_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
