---
title: "GetCadIdentifiers Method (ISwDMDimXpertAnnotation)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertAnnotation"
member: "GetCadIdentifiers"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAnnotation~GetCadIdentifiers.html"
---

# GetCadIdentifiers Method (ISwDMDimXpertAnnotation)

Gets all of the CAD identifiers of this DimXpert annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCadIdentifiers() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertAnnotation
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

See [SwDMDimXpertAnnotation::GetCadIdentifiers](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertAnnotation~GetCadIdentifiers.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertAnnotation Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAnnotation.html)
[ISwDMDimXpertAnnotation Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAnnotation_members.html)
[ISwDMDimXpertAnnotation::IGetCadIdentifiers Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAnnotation~IGetCadIdentifiers.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
