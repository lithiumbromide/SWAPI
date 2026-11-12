---
title: "PDMDocManager Property (CTbcApplication)"
project: "SOLIDWORKS Toolbox Browser API"
interface: "CTbcApplication"
member: "PDMDocManager"
kind: "property"
source: "toolboxapi/SolidWorks.Interop.sldtoolboxconfigureaddin~SolidWorks.Interop.sldtoolboxconfigureaddin.CTbcApplication~PDMDocManager.html"
---

# PDMDocManager Property (CTbcApplication)

Gets the PDM document manager.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PDMDocManager As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As CTbcApplication
Dim value As System.Object

value = instance.PDMDocManager
```

### C#

```csharp
System.object PDMDocManager {get;}
```

### C++/CLI

```cpp
property System.Object^ PDMDocManager {
   System.Object^ get();
}
```

### Property Value

[IPDMDocManager](ms-its:toolboxapi.chm::/SOLIDWORKS.Interop.swbrowser~SOLIDWORKS.Interop.swbrowser.IPDMDocManager.html)

## VBA Syntax

See [ToolBoxConfiguratorApplication::PDMDocManager](ms-its:toolboxapivb6.chm::/ToolboxConfigurationApplicationLib~CTbcApplication~PDMDocManager.html).

## See Also

[CTbcApplication Interface](SolidWorks.Interop.sldtoolboxconfigureaddin~SolidWorks.Interop.sldtoolboxconfigureaddin.CTbcApplication.html)
[CTbcApplication Members](SolidWorks.Interop.sldtoolboxconfigureaddin~SolidWorks.Interop.sldtoolboxconfigureaddin.CTbcApplication_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
