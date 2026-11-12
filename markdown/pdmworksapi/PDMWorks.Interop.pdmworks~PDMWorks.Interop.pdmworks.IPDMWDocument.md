---
title: "IPDMWDocument Interface"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocument"
member: ""
kind: "interface"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html"
---

# IPDMWDocument Interface

Represents and provides access to a single file that is checked into the vault. Some document properties, such as configuration, references, and where used, only work with SOLIDWORKS documents (.sldprt, .sldasm, and .slddrw files).

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IPDMWDocument
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocument
```

### C#

```csharp
public interface IPDMWDocument
```

### C++/CLI

```cpp
public interface class IPDMWDocument
```

## VBA Syntax

See [PDMWDocument](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocument.html).

## Examples

[Extract Embedded eDrawings Data (VBA)](Extract_Embedded_eDrawings_Data_Example_VB.htm)
[Get Specific Document (VBA)](Get_Specific_Document_Example_VB.htm)
[List Assemblies Where Part Used (VBA)](List_Assemblies_Where_Part_Used_Example_VB.htm)
[Get Names of Projects for All Documents in Vault (VB.NET)](Get_Names_Projects_for_Documents_in_Vault_Example_VBNET.htm)

## Accessors

[IPDMWConfiguration::Document](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConfiguration~Document.html)

[IPDMWConnection::CheckIn](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~CheckIn.html)

[IPDMWConnection::GetSpecificDocument](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~GetSpecificDocument.html)

[IPDMWDocuments::Item](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocuments~Item.html)

[IPDMWLink::Document](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLink~Document.html)

[IPDMWSearchResult::Document](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchResult~Document.html)

## See Also

[IPDMWDocument Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument_members.html)
[PDMWorks.Interop.pdmworks Namespace](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks_namespace.html)
[IPDMWDocuments Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocuments.html)
