---
title: "IGetCadIdentifiers Method (ISwDMDimXpertFeature)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertFeature"
member: "IGetCadIdentifiers"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature~IGetCadIdentifiers.html"
---

# IGetCadIdentifiers Method (ISwDMDimXpertFeature)

Gets all of the CAD identifiers of this DimXpert feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetCadIdentifiers( _
   ByVal Count As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertFeature
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

Use [ISwDMDimXpertFeature::GetCadIdentifierCount](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertFeature~GetCadIdentifierCount.html) to populate the Count argument.

## See Also

[ISwDMDimXpertFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature.html)
[ISwDMDimXpertFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature_members.html)
[ISwDMDimXpertFeature::GetCadIdentifiers Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature~GetCadIdentifiers.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
