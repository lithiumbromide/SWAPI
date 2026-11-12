---
title: "Name Property (ISwDMComponent)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMComponent"
member: "Name"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent~Name.html"
---

# Name Property (ISwDMComponent)

Obsolete. Superseded by [ISwDMComponent11::Name3](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent11~Name3.html).

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Name As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMComponent
Dim value As System.String

value = instance.Name
```

### C#

```csharp
System.string Name {get;}
```

### C++/CLI

```cpp
property System.String^ Name {
   System.String^ get();
}
```

### Property Value

Name of the component

## VBA Syntax

See [SwDMComponent::Name](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMComponent~Name.html).

## Examples

[Get Whether Component Is Envelope and Excluded from BOM (C#)](Get_Whether_Component_Is_Envelope_And_Excluded_From_BOM_Example_CSharp.htm)
[Get Whether Component Is Envelope and Excluded from BOM (VB.NET)](Get_Whether_Component_Is_Envelope_And_Excluded_From_BOM_Example_VBNET.htm)
[Replace Component (C#)](Replace_Component_Example_CSharp.htm)
[Replace Component (VB.NET)](Replace_Component_Example_VBNET.htm)

## Remarks

This property only supports documents saved in SOLIDWORKS 2003 (Version 2200) and later. To get the version of a document, use [ISwDMDocument::GetVersion](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument~GetVersion.html).

## See Also

[ISwDMComponent Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent.html)
[ISwDMComponent Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent_members.html)

## Availability

SOLIDWORKS Document Manager API 2004 SP1
