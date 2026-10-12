---
title: "FileName Property (IDocumentSpecification)"
project: "SOLIDWORKS API Help"
interface: "IDocumentSpecification"
member: "FileName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~FileName.html"
---

# FileName Property (IDocumentSpecification)

Gets or sets the path and filename of the model document to open.

## Syntax

### Visual Basic (Declaration)

```vb
Property FileName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDocumentSpecification
Dim value As System.String

instance.FileName = value

value = instance.FileName
```

### C#

```csharp
System.string FileName {get; set;}
```

### C++/CLI

```cpp
property System.String^ FileName {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Path and filename of the model document to open

## VBA Syntax

See [DocumentSpecification::FileName](ms-its:sldworksapivb6.chm::/sldworks~DocumentSpecification~FileName.html).

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
