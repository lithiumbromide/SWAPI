---
title: "IGetCadIdentifiers Method (ISwDMDimXpertAnnotation)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertAnnotation"
member: "IGetCadIdentifiers"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAnnotation~IGetCadIdentifiers.html"
---

# IGetCadIdentifiers Method (ISwDMDimXpertAnnotation)

Gets all of the CAD identifiers of this DimXpert annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetCadIdentifiers( _
   ByVal Count As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertAnnotation
Dim Count As System.Integer
Dim value As System.String

value = instance.IGetCadIdentifiers(Count)
```

### C#

```csharp
System.string IGetCadIdentifiers(
   System.int Count
)
```

### C++/CLI

```cpp
System.String^ IGetCadIdentifiers(
   System.int Count
)
```

### Parameters

- `Count`: Number of CAD identifiers

### Return Value

in-process, unmanaged C++: Pointer to an array of strings; the format of each string is bodyid:faceid

VBA, VB.NET, C#, and C++/CLI: Not supported

## Remarks

Use [ISwDMDimXpertAnnotation::GetCadIdentifierCount](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertAnnotation~GetCadIdentifierCount.html) to populate the Count argument.

## See Also

[ISwDMDimXpertAnnotation Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAnnotation.html)
[ISwDMDimXpertAnnotation Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAnnotation_members.html)
[ISwDMDimXpertAnnotation::GetCadIdentifiers Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAnnotation~GetCadIdentifiers.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
