---
title: "SelectName2 Property (ISwDMComponent11)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMComponent11"
member: "SelectName2"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent11~SelectName2.html"
---

# SelectName2 Property (ISwDMComponent11)

Gets the name of the component needed to specify in the component list in [ISldWorks::IDocumentSpecification](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDocumentSpecification~ComponentList.html) during a selective open using [SldWorks::OpenDoc7](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~OpenDoc7.html).

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property SelectName2 As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMComponent11
Dim value As System.String

value = instance.SelectName2
```

### C#

```csharp
System.string SelectName2 {get;}
```

### C++/CLI

```cpp
property System.String^ SelectName2 {
   System.String^ get();
}
```

### Property Value

Name to use during a selective open

## VBA Syntax

See [SwDMComponent11::SelectName2](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMComponent11~SelectName2.html).

## Examples

See the [ISwDMComponent11](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent11.html) examples.

## See Also

[ISwDMComponent11 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent11.html)
[ISwDMComponent11 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent11_members.html)

## Availability

SOLIDWORKS Document Manager API 2021 SP0
