---
title: "DisplayState Property (IDocumentSpecification)"
project: "SOLIDWORKS API Help"
interface: "IDocumentSpecification"
member: "DisplayState"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~DisplayState.html"
---

# DisplayState Property (IDocumentSpecification)

Gets or sets the name of the display state to use when opening a model document.

## Syntax

### Visual Basic (Declaration)

```vb
Property DisplayState As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDocumentSpecification
Dim value As System.String

instance.DisplayState = value

value = instance.DisplayState
```

### C#

```csharp
System.string DisplayState {get; set;}
```

### C++/CLI

```cpp
property System.String^ DisplayState {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of the display state to use

## VBA Syntax

See [DocumentSpecification::DisplayState](ms-its:sldworksapivb6.chm::/sldworks~DocumentSpecification~DisplayState.html).

## Examples

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
