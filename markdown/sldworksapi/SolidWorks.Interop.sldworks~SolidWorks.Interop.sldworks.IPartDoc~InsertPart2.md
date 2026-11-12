---
title: "InsertPart2 Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "InsertPart2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~InsertPart2.html"
---

# InsertPart2 Method (IPartDoc)

Obsolete. Superseded by [IPartDoc::InsertPart3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~InsertPart3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertPart2( _
   ByVal FileName As System.String, _
   ByVal Options As System.Integer _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim FileName As System.String
Dim Options As System.Integer
Dim value As Feature

value = instance.InsertPart2(FileName, Options)
```

### C#

```csharp
Feature InsertPart2(
   System.string FileName,
   System.int Options
)
```

### C++/CLI

```cpp
Feature^ InsertPart2(
   System.String^ FileName,
   System.int Options
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Name of part file
- `Options`: Insertion options as defined in [swInsertPartOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInsertPartOptions_e.html)

### Return Value

Inserted [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [PartDoc::InsertPart2](ms-its:sldworksapivb6.chm::/Sldworks~PartDoc~InsertPart2.html).

## Remarks

This method inserts the specified part at the origin of this part. To position the inserted part at a different location or orientation or both, use [IFeatureManager::InsertMoveCopyBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertMoveCopyBody2.html).

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IDerivedPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
