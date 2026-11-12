---
title: "Silent Property (IDocumentSpecification)"
project: "SOLIDWORKS API Help"
interface: "IDocumentSpecification"
member: "Silent"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~Silent.html"
---

# Silent Property (IDocumentSpecification)

Gets or sets whether to open the model document silently.

## Syntax

### Visual Basic (Declaration)

```vb
Property Silent As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDocumentSpecification
Dim value As System.Boolean

instance.Silent = value

value = instance.Silent
```

### C#

```csharp
System.bool Silent {get; set;}
```

### C++/CLI

```cpp
property System.bool Silent {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to open the model document silently, false to not

## VBA Syntax

See [DocumentSpecification::Silent](ms-its:sldworksapivb6.chm::/sldworks~DocumentSpecification~Silent.html).

## Examples

[Get Whether Components Are Loaded (C#)](Get_Whether_Components_Are_Loaded_Example_CSharp.htm)
[Get Whether Components Are Loaded (VB.NET)](Get_Whether_Components_Are_Loaded_Example_VBNET.htm)
[Get Whether Components Are Loaded (VBA)](Get_Whether_Components_Are_Loaded_Example_VB.htm)
[Open Assembly Document (C#)](Open_Assembly_Document_Example_CSharp.htm)
[Open Assembly Document (VB.NET)](Open_Assembly_Document_Example_VBNET.htm)
[Open Assembly Document (VBA)](Open_Assembly_Document_Example_VB.htm)

## Remarks

The software uses the last-displayed configuration if it discovers missing configurations or component references. No warnings or errors display if this property is set to true.

## See Also

[IDocumentSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.html)
[IDocumentSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.html)
[IDocumentSpecification::AutoRepair Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~AutoRepair.html)
[IDocumentSpecification::CriticalDataRepair Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~CriticalDataRepair.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
