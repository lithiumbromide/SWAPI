---
title: "GetModelDoc Method (IDerivedPartFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDerivedPartFeatureData"
member: "GetModelDoc"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~GetModelDoc.html"
---

# GetModelDoc Method (IDerivedPartFeatureData)

Gets the model document from which this part was derived (i.e., the base model document).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetModelDoc() As ModelDoc2
```

### Visual Basic (Usage)

```vb
Dim instance As IDerivedPartFeatureData
Dim value As ModelDoc2

value = instance.GetModelDoc()
```

### C#

```csharp
ModelDoc2 GetModelDoc()
```

### C++/CLI

```cpp
ModelDoc2^ GetModelDoc();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Base [model document](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html)

## VBA Syntax

See [DerivedPartFeatureData::GetModelDoc](ms-its:sldworksapivb6.chm::/sldworks~DerivedPartFeatureData~GetModelDoc.html).

## See Also

[IDerivedPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData.html)
[IDerivedPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
