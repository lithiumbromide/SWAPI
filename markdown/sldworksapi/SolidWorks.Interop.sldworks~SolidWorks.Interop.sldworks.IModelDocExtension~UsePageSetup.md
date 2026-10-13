---
title: "UsePageSetup Property (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "UsePageSetup"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UsePageSetup.html"
---

# UsePageSetup Property (IModelDocExtension)

Gets or sets whether this document uses its own page setup values, SOLIDWORKS Design application page setup values, or setup values on individual drawing sheets.

## Syntax

### Visual Basic (Declaration)

```vb
Property UsePageSetup As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Integer

instance.UsePageSetup = value

value = instance.UsePageSetup
```

### C#

```csharp
System.int UsePageSetup {get; set;}
```

### C++/CLI

```cpp
property System.int UsePageSetup {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Page setup to use as defined in [swPageSetupInUse_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPageSetupInUse_e.html)

## VBA Syntax

See [ModelDocExtension::UsePageSetup](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~UsePageSetup.html).

## Examples

[Print Drawing (C#)](Print_Drawing_as_High_Quality_Example_CSharp.htm)
[Print Drawing (VB.NET)](Print_Drawing_as_High_Quality_Example_VBNET.htm)
[Print Drawing (VBA)](Print_Drawing_as_High_Quality_Example_VB.htm)

## Remarks

| To retrieve this page setup... | Use... |
| --- | --- |
| Application | IModelDocExtension::AppPageSetup |
| Document | IModelDoc2::PageSetup or IModelDoc2::IPageSetup |
| Sheet | ISheet::PageSetup or ISheet::IPageSetup |

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IPageSetup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
