---
title: "InsertPart3 Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "InsertPart3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~InsertPart3.html"
---

# InsertPart3 Method (IPartDoc)

Inserts the specified part in the specified configuration into this part.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertPart3( _
   ByVal FileName As System.String, _
   ByVal Options As System.Integer, _
   ByVal ConfigurationName As System.String _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim FileName As System.String
Dim Options As System.Integer
Dim ConfigurationName As System.String
Dim value As Feature

value = instance.InsertPart3(FileName, Options, ConfigurationName)
```

### C#

```csharp
Feature InsertPart3(
   System.string FileName,
   System.int Options,
   System.string ConfigurationName
)
```

### C++/CLI

```cpp
Feature^ InsertPart3(
   System.String^ FileName,
   System.int Options,
   System.String^ ConfigurationName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Name of the part file to insert
- `Options`: Insertion options as defined in [swInsertPartOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInsertPartOptions_e.html)
- `ConfigurationName`: Name of FileName's configuration

### Return Value

Inserted [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [PartDoc::InsertPart3](ms-its:sldworksapivb6.chm::/Sldworks~PartDoc~InsertPart3.html).

## Examples

[Modify Derived Part (VBA)](Modify_Derived_Part_Example_VB.htm)
[Modify Derived Part (VB.NET)](Modify_Derived_Part_Example_VBNET.htm)
[Modify Derived Part (C#)](Modify_Derived_Part_Example_CSharp.htm)

## Remarks

This method inserts the specified part at the origin of this part. To position the inserted part at a different location or orientation or both, use [IFeatureManager::InsertMoveCopyBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertMoveCopyBody2.html).

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IDerivedPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
