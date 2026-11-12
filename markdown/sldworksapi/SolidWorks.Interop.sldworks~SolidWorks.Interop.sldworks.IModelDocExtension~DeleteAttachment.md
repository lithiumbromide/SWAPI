---
title: "DeleteAttachment Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "DeleteAttachment"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteAttachment.html"
---

# DeleteAttachment Method (IModelDocExtension)

Deletes the specified file in the Attachments folder in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteAttachment( _
   ByVal FileName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim FileName As System.String
Dim value As System.Boolean

value = instance.DeleteAttachment(FileName)
```

### C#

```csharp
System.bool DeleteAttachment(
   System.string FileName
)
```

### C++/CLI

```cpp
System.bool DeleteAttachment(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Name of the file to delete from the Attachments folder in the FeatureManager design tree

### Return Value

True if the file is deleted, false if not

## VBA Syntax

See [ModelDocExtension::DeleteAttachment](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~DeleteAttachment.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::GetAttachmentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAttachmentCount.html)
[IModelDocExtension::GetAttachments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAttachments.html)
[IModelDocExtension::IGetAttachments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetAttachments.html)
[IModelDocExtension::InsertAttachment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertAttachment.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
