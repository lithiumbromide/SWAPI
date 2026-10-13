---
title: "GetCadIdentifiers Method (ISwDMDimXpertFeature)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertFeature"
member: "GetCadIdentifiers"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature~GetCadIdentifiers.html"
---

# GetCadIdentifiers Method (ISwDMDimXpertFeature)

Gets all of the CAD identifiers of this DimXpert feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCadIdentifiers() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertFeature
Dim value As System.Object

value = instance.GetCadIdentifiers()
```

### C#

```csharp
System.object GetCadIdentifiers()
```

### C++/CLI

```cpp
System.Object^ GetCadIdentifiers();
```

### Return Value

Array of strings; the format of each string is bodyid:faceid

## VBA Syntax

See [SwDMDimXpertFeature::GetCadIdentifiers](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertFeature~GetCadIdentifiers.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature.html)
[ISwDMDimXpertFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature_members.html)
[ISwDMDimXpertFeature::IGetCadIdentifiers Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature~IGetCadIdentifiers.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
