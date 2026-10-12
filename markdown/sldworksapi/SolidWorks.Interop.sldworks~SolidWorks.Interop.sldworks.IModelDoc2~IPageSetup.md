---
title: "IPageSetup Property (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IPageSetup"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IPageSetup.html"
---

# IPageSetup Property (IModelDoc2)

Gets the page setup for this document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IPageSetup As PageSetup
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As PageSetup

value = instance.IPageSetup
```

### C#

```csharp
PageSetup IPageSetup {get;}
```

### C++/CLI

```cpp
property PageSetup^ IPageSetup {
   PageSetup^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Page setup](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPageSetup.html)

## VBA Syntax

See [ModelDoc2::IPageSetup](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~IPageSetup.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::PageSetup Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~PageSetup.html)
[IModelDocExtension::AppPageSetup Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AppPageSetup.html)
[IModelDocExtension::UsePageSetup Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UsePageSetup.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
