---
title: "UseSpeedPak Property (IDocumentSpecification)"
project: "SOLIDWORKS API Help"
interface: "IDocumentSpecification"
member: "UseSpeedPak"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~UseSpeedPak.html"
---

# UseSpeedPak Property (IDocumentSpecification)

Gets or sets whether to open an assembly document using the SpeedPak option.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseSpeedPak As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDocumentSpecification
Dim value As System.Boolean

instance.UseSpeedPak = value

value = instance.UseSpeedPak
```

### C#

```csharp
System.bool UseSpeedPak {get; set;}
```

### C++/CLI

```cpp
property System.bool UseSpeedPak {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use SpeedPak, false to not

## VBA Syntax

See [DocumentSpecification::UseSpeedPak](ms-its:sldworksapivb6.chm::/sldworks~DocumentSpecification~UseSpeedPak.html).

## See Also

[IDocumentSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.html)
[IDocumentSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.html)
[IAssemblyDoc::UseSpeedPak Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UseSpeedPak.html)

## Availability

SOLIDWORKS 2011 FCS, Revision 19.0
