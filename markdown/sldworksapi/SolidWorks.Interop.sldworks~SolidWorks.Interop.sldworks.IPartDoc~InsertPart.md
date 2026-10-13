---
title: "InsertPart Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "InsertPart"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~InsertPart.html"
---

# InsertPart Method (IPartDoc)

Obsolete. Superseded by [IPartDoc::InsertPart2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~InsertPart2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertPart( _
   ByVal FileName As System.String, _
   ByVal ImportPlane As System.Boolean, _
   ByVal ImportAxis As System.Boolean, _
   ByVal ImportCThread As System.Boolean _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim FileName As System.String
Dim ImportPlane As System.Boolean
Dim ImportAxis As System.Boolean
Dim ImportCThread As System.Boolean
Dim value As Feature

value = instance.InsertPart(FileName, ImportPlane, ImportAxis, ImportCThread)
```

### C#

```csharp
Feature InsertPart(
   System.string FileName,
   System.bool ImportPlane,
   System.bool ImportAxis,
   System.bool ImportCThread
)
```

### C++/CLI

```cpp
Feature^ InsertPart(
   System.String^ FileName,
   System.bool ImportPlane,
   System.bool ImportAxis,
   System.bool ImportCThread
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Name of part file
- `ImportPlane`: True if the planes from the part should be imported into this part, false if not
- `ImportAxis`: True if the axes from the part should be imported into this part, false if not
- `ImportCThread`: True if the cosmetic threads from the part should be imported into this part, false if not

### Return Value

New [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [PartDoc::InsertPart](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~InsertPart.html).

## Remarks

This method inserts the specified part at the origin of this part. To position the insert part at a different location or orientation or both, use [IFeatureManager::InsertMoveCopyBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertMoveCopyBody2.html).

The interface returned by this method is [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html), which gives you access to the feature APIs such as [IFeature::Name](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~Name.html) to get or set the name of the feature.

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
