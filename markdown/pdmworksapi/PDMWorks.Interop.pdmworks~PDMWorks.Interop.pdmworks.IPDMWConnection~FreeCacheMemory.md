---
title: "FreeCacheMemory Method (IPDMWConnection)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWConnection"
member: "FreeCacheMemory"
kind: "method"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~FreeCacheMemory.html"
---

# FreeCacheMemory Method (IPDMWConnection)

Frees the cache memory.

## Syntax

### Visual Basic (Declaration)

```vb
Sub FreeCacheMemory()
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWConnection

instance.FreeCacheMemory()
```

### C#

```csharp
void FreeCacheMemory()
```

### C++/CLI

```cpp
void FreeCacheMemory();
```

## VBA Syntax

See [PDMWConnection::FreeCacheMemory](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWConnection~FreeCacheMemory.html).

## Examples

Set PDMW_conn = CreateObject("PDMWorks.PDMWConnection")

PDMW_conn.**Login** "pdmwadmin", "pdmwadmin", "localhost"

PDMW_conn.**FreeCacheMemory**

PDMW_conn.**Logout**

## Remarks

Only a vault adminstrator call use this method.

## See Also

[IPDMWConnection Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection.html)
[IPDMWConnection Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2009 FCS
