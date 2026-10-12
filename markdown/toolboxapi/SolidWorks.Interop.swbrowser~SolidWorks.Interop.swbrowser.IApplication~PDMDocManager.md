---
title: "PDMDocManager Property (IApplication)"
project: "SOLIDWORKS Toolbox Browser API"
interface: "IApplication"
member: "PDMDocManager"
kind: "property"
source: "toolboxapi/SolidWorks.Interop.swbrowser~SolidWorks.Interop.swbrowser.IApplication~PDMDocManager.html"
---

# PDMDocManager Property (IApplication)

Gets the PDM document manager.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PDMDocManager As PDMDocManager
```

### Visual Basic (Usage)

```vb
Dim instance As IApplication
Dim value As PDMDocManager

value = instance.PDMDocManager
```

### C#

```csharp
PDMDocManager PDMDocManager {get;}
```

### C++/CLI

```cpp
property PDMDocManager^ PDMDocManager {
   PDMDocManager^ get();
}
```

### Property Value

[IPDMDocManager](SOLIDWORKS.Interop.swbrowser~SOLIDWORKS.Interop.swbrowser.IPDMDocManager.html)

## VBA Syntax

See [Application::PDMDocManager](ms-its:toolboxapivb6.chm::/ToolboxBrowser~Application~PDMDocManager.html).

## Remarks

Available only if you installed SOLIDWORKS Toolbox.

## See Also

[IApplication Interface](SolidWorks.Interop.swbrowser~SolidWorks.Interop.swbrowser.IApplication.html)
[IApplication Members](SolidWorks.Interop.swbrowser~SolidWorks.Interop.swbrowser.IApplication_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
