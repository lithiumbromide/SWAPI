---
title: "DocumentType Property (IDocumentSpecification)"
project: "SOLIDWORKS API Help"
interface: "IDocumentSpecification"
member: "DocumentType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~DocumentType.html"
---

# DocumentType Property (IDocumentSpecification)

Gets or sets the type of model document to open.

## Syntax

### Visual Basic (Declaration)

```vb
Property DocumentType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDocumentSpecification
Dim value As System.Integer

instance.DocumentType = value

value = instance.DocumentType
```

### C#

```csharp
System.int DocumentType {get; set;}
```

### C++/CLI

```cpp
property System.int DocumentType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of document as defined by [swDocumentTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)

## VBA Syntax

See [DocumentSpecification::DocumentType](ms-its:sldworksapivb6.chm::/sldworks~DocumentSpecification~DocumentType.html).

## Examples

[Open Drawing Document Read-only (VBA)](Open_Drawing_Document_Read-only_Example_VB.htm)
[Get Whether Components Are Loaded (C#)](Get_Whether_Components_Are_Loaded_Example_CSharp.htm)
[Get Whether Components Are Loaded (VB.NET)](Get_Whether_Components_Are_Loaded_Example_VBNET.htm)
[Get Whether Components Are Loaded (VBA)](Get_Whether_Components_Are_Loaded_Example_VB.htm)
[Open Assembly Document (C#)](Open_Assembly_Document_Example_CSharp.htm)
[Open Assembly Document (VB.NET)](Open_Assembly_Document_Example_VBNET.htm)
[Open Assembly Document (VBA)](Open_Assembly_Document_Example_VB.htm)

## Remarks

This property is not valid for opening **3D**EXPERIENCE files using [SOLIDWORKS Design connected to the 3DEXPERIENCE platform](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm).

## See Also

[IDocumentSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.html)
[IDocumentSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
