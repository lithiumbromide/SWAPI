---
title: "DateModified Property (IPDMWDocument)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocument"
member: "DateModified"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~DateModified.html"
---

# DateModified Property (IPDMWDocument)

Gets the date and time that this document was last modified.

## Syntax

### Visual Basic (Declaration)

```vb
Property DateModified As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocument
Dim value As System.Object

instance.DateModified = value

value = instance.DateModified
```

### C#

```csharp
System.object DateModified {get; set;}
```

### C++/CLI

```cpp
property System.Object^ DateModified {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

### Property Value

Date and time document last modified

## VBA Syntax

See [PDMWDocument::DateModified](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocument~DateModified.html).

## Remarks

For Visual Basic for Applications (VBA) and unmanaged C++ COM, this property returns a VARIANT of type VT_DATE that corresponds to the Windows date-modified field: date, hours, minutes, seconds.

## See Also

[IPDMWDocument Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html)
[IPDMWDocument Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument_members.html)
[IPDMWDocument::UpdateStamp Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~UpdateStamp.html)

## Availability

SOLIDWORKS Workgroup PDM 2006 FCS
