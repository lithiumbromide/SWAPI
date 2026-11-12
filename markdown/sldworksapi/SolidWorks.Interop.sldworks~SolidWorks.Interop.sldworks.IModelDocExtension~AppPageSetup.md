---
title: "AppPageSetup Property (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "AppPageSetup"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AppPageSetup.html"
---

# AppPageSetup Property (IModelDocExtension)

Gets the SOLIDWORKS Design application page setup interface for this document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property AppPageSetup As PageSetup
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As PageSetup

value = instance.AppPageSetup
```

### C#

```csharp
PageSetup AppPageSetup {get;}
```

### C++/CLI

```cpp
property PageSetup^ AppPageSetup {
   PageSetup^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Page setup](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPageSetup.html) object for SOLIDWORKS Design

## VBA Syntax

See [ModelDocExtension::AppPageSetup](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~AppPageSetup.html).

## Examples

[Get Whether Draft Edges Scaled in Printed Drawing (C#)](Get_Whether_Draft_Edges_Scaled_in_Printed_Drawing_Example_CSharp.htm)
[Get Whether Draft Edges Scaled in Printed Drawing (VB.NET)](Get_Whether_Draft_Edges_Scaled_in_Printed_Drawing_Example_VBNET.htm)
[Get Whether Draft Edges Scaled in Printed Drawing (VBA)](Get_Whether_Draft_Edges_Scaled_in_Printed_Drawing_Example_VB.htm)

## Remarks

The page setup object used when printing depends on a document setting, which indicates whether to use the application page setup, the page setup for this document.

| To... | Use... |
| --- | --- |
| Get or set a document setting | IModelDocExtension::UsePageSetup |
| Get the document page setup | IModelDoc2::PageSetup or IModelDoc2::IPageSetup |
| Get the sheet page setup | ISheet::PageSetup or ISheet::IPageSetup |

Although the object that this property returns indicates that it contains application-level values, some of the values that it contains depend on the type of document. Therefore, this API is on a document interface, and you should retrieve a different one for each different document that you print.

This property is read only.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
