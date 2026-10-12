---
title: "SummaryInfo Property (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SummaryInfo"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SummaryInfo.html"
---

# SummaryInfo Property (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SummaryInfo](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SummaryInfo.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property SummaryInfo( _
   ByVal FieldId As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim FieldId As System.Integer
Dim value As System.String

instance.SummaryInfo(FieldId) = value

value = instance.SummaryInfo(FieldId)
```

### C#

```csharp
System.string SummaryInfo(
   System.int FieldId
) {get; set;}
```

### C++/CLI

```cpp
property System.String^ SummaryInfo {
   System.String^ get(System.int FieldId);
   void set (System.int FieldId, System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FieldId`:

## VBA Syntax

See [ModelDoc::SummaryInfo](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SummaryInfo.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
