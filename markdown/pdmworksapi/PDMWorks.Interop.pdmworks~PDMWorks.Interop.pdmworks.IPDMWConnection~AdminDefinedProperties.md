---
title: "AdminDefinedProperties Property (IPDMWConnection)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWConnection"
member: "AdminDefinedProperties"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~AdminDefinedProperties.html"
---

# AdminDefinedProperties Property (IPDMWConnection)

Gets a collection of vault administrator-defined custom properties.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property AdminDefinedProperties As PDMWProperties
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWConnection
Dim value As PDMWProperties

value = instance.AdminDefinedProperties
```

### C#

```csharp
PDMWProperties AdminDefinedProperties {get;}
```

### C++/CLI

```cpp
property PDMWProperties^ AdminDefinedProperties {
   PDMWProperties^ get();
}
```

### Property Value

[IPDMWProperties](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProperties.html) collection

## VBA Syntax

See [PDMWConnection::AdminDefinedProperties](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWConnection~AdminDefinedProperties.html).

## Remarks

These properties are read-only. [IPDMWPropertes::Add](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProperties~Add.html) does nothing when used in this context.

## See Also

[IPDMWConnection Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection.html)
[IPDMWConnection Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2004 FCS
