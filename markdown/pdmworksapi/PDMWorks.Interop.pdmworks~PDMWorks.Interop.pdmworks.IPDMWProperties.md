---
title: "IPDMWProperties Interface"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWProperties"
member: ""
kind: "interface"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProperties.html"
---

# IPDMWProperties Interface

Contains [IPDMWProperty](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProperty.html) objects.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IPDMWProperties
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWProperties
```

### C#

```csharp
public interface IPDMWProperties
```

### C++/CLI

```cpp
public interface class IPDMWProperties
```

## VBA Syntax

See [PDMWProperties](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWProperties.html).

## Remarks

You can get collections of configuration, document, and vault administrator-defined custom properties. You can [add](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProperties~Add.html) new properties to configurations and documents; however, you cannot add new vault adminstrator-defined custom properties.

## Accessors

[IPDMWConfiguration::Properties](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConfiguration~Properties.html)

[IPDMWConnection::AdminDefinedProperties](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~AdminDefinedProperties.html)

[IPDMWDocument::Properties](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~Properties.html)

## See Also

[IPDMWProperties Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProperties_members.html)
[PDMWorks.Interop.pdmworks Namespace](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks_namespace.html)
[IPDMWProperty Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProperty.html)
