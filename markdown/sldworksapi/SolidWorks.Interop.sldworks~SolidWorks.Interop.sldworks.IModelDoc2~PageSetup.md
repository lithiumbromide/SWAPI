---
title: "PageSetup Property (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "PageSetup"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~PageSetup.html"
---

# PageSetup Property (IModelDoc2)

Gets the page setup for this document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PageSetup As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Object

value = instance.PageSetup
```

### C#

```csharp
System.object PageSetup {get;}
```

### C++/CLI

```cpp
property System.Object^ PageSetup {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Page setup](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPageSetup.html)

## VBA Syntax

See [ModelDoc2::PageSetup](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~PageSetup.html).

## Examples

[Print Drawing and Save As PDF (VBA)](Print_Drawing_and_Save_as_PDF_Example_VB.htm)
[Print Drawing (C#)](Print_Drawing_as_High_Quality_Example_CSharp.htm)
[Print Drawing (VB.NET)](Print_Drawing_as_High_Quality_Example_VBNET.htm)
[Print Drawing (VBA)](Print_Drawing_as_High_Quality_Example_VB.htm)

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::IPageSetup Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IPageSetup.html)
[IModelDocExtension::AppPageSetup Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AppPageSetup.html)
[IModelDocExtension::UsePageSetup Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UsePageSetup.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
