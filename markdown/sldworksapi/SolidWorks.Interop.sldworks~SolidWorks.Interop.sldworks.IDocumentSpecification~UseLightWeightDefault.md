---
title: "UseLightWeightDefault Property (IDocumentSpecification)"
project: "SOLIDWORKS API Help"
interface: "IDocumentSpecification"
member: "UseLightWeightDefault"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~UseLightWeightDefault.html"
---

# UseLightWeightDefault Property (IDocumentSpecification)

Gets or sets whether to use the system default lightweight setting.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseLightWeightDefault As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDocumentSpecification
Dim value As System.Boolean

instance.UseLightWeightDefault = value

value = instance.UseLightWeightDefault
```

### C#

```csharp
System.bool UseLightWeightDefault {get; set;}
```

### C++/CLI

```cpp
property System.bool UseLightWeightDefault {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use the system default lightweight setting, false to use [IDocumentSpecification::Lightweight value](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDocumentSpecification~LightWeight.html)

## VBA Syntax

See [DocumentSpecification::UseLightWeightDefault](ms-its:sldworksapivb6.chm::/sldworks~DocumentSpecification~UseLightWeightDefault.html).

## Examples

[Get Whether Components Are Loaded (C#)](Get_Whether_Components_Are_Loaded_Example_CSharp.htm)
[Get Whether Components Are Loaded (VB.NET)](Get_Whether_Components_Are_Loaded_Example_VBNET.htm)
[Get Whether Components Are Loaded (VBA)](Get_Whether_Components_Are_Loaded_Example_VB.htm)
[Open Assembly Document (C#)](Open_Assembly_Document_Example_CSharp.htm)
[Open Assembly Document (VB.NET)](Open_Assembly_Document_Example_VBNET.htm)
[Open Assembly Document (VBA)](Open_Assembly_Document_Example_VB.htm)

## See Also

[IDocumentSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.html)
[IDocumentSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
