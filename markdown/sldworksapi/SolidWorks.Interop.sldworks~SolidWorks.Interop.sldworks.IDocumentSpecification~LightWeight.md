---
title: "LightWeight Property (IDocumentSpecification)"
project: "SOLIDWORKS API Help"
interface: "IDocumentSpecification"
member: "LightWeight"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~LightWeight.html"
---

# LightWeight Property (IDocumentSpecification)

Gets or sets whether to open an assembly or drawing document with lightweight parts.

## Syntax

### Visual Basic (Declaration)

```vb
Property LightWeight As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDocumentSpecification
Dim value As System.Boolean

instance.LightWeight = value

value = instance.LightWeight
```

### C#

```csharp
System.bool LightWeight {get; set;}
```

### C++/CLI

```cpp
property System.bool LightWeight {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to open the assembly or drawing document with lightweight parts, false to not

## VBA Syntax

See [DocumentSpecification::LightWeight](ms-its:sldworksapivb6.chm::/sldworks~DocumentSpecification~LightWeight.html).

## Examples

[Get Whether Components Are Loaded (C#)](Get_Whether_Components_Are_Loaded_Example_CSharp.htm)
[Get Whether Components Are Loaded (VB.NET)](Get_Whether_Components_Are_Loaded_Example_VBNET.htm)
[Get Whether Components Are Loaded (VBA)](Get_Whether_Components_Are_Loaded_Example_VB.htm)
[Open Assembly Document (C#)](Open_Assembly_Document_Example_CSharp.htm)
[Open Assembly Document (VB.NET)](Open_Assembly_Document_Example_VBNET.htm)
[Open Assembly Document (VBA)](Open_Assembly_Document_Example_VB.htm)

## Remarks

[IDocumentSpecification::UseLightWeightDefault](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDocumentSpecification~UseLightWeightDefault.html) must be false for this property to have an effect.

## See Also

[IDocumentSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.html)
[IDocumentSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
