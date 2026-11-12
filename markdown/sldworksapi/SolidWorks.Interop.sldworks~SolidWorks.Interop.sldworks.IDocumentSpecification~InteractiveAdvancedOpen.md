---
title: "InteractiveAdvancedOpen Property (IDocumentSpecification)"
project: "SOLIDWORKS API Help"
interface: "IDocumentSpecification"
member: "InteractiveAdvancedOpen"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~InteractiveAdvancedOpen.html"
---

# InteractiveAdvancedOpen Property (IDocumentSpecification)

Gets whether to display an intermediate dialog, which allows the interactive user to set options before opening a document.

## Syntax

### Visual Basic (Declaration)

```vb
Property InteractiveAdvancedOpen As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDocumentSpecification
Dim value As System.Boolean

instance.InteractiveAdvancedOpen = value

value = instance.InteractiveAdvancedOpen
```

### C#

```csharp
System.bool InteractiveAdvancedOpen {get; set;}
```

### C++/CLI

```cpp
property System.bool InteractiveAdvancedOpen {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to display an intermediate dialog to the interactive user, false to not (default)

## VBA Syntax

See [DocumentSpecification::InteractiveAdvancedOpen](ms-its:sldworksapivb6.chm::/sldworks~DocumentSpecification~InteractiveAdvancedOpen.html).

## Examples

[Open Advanced Dialog On Document Open (VBA)](Open_Advanced_Dialog_On_Open_Example_VB.htm)
[Open Advanced Dialog On Document Open (VB.NET)](Open_Advanced_Dialog_On_Open_Example_VBNET.htm)
[Open Advanced Dialog On Document Open (C#)](Open_Advanced_Dialog_On_Open_Example_CSharp.htm)

## Remarks

This property is not valid for opening **3D**EXPERIENCE files using [SOLIDWORKS Design connected to the 3DEXPERIENCE platform](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm).

## See Also

[IDocumentSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.html)
[IDocumentSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
